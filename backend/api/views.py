import csv
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from .models import Election, Position, Partylist, Candidate, Voter, VoteRecord
from .serializers import (
    ElectionSerializer, PositionSerializer, PartylistSerializer,
    CandidateSerializer, VoterSerializer, VoteRecordSerializer,
    SubmitVoteSerializer
)

class ElectionViewSet(viewsets.ModelViewSet):
    queryset = Election.objects.all()
    serializer_class = ElectionSerializer
    permission_classes = [IsAuthenticated]

class PositionViewSet(viewsets.ModelViewSet):
    queryset = Position.objects.all()
    serializer_class = PositionSerializer
    permission_classes = [IsAuthenticated]

class PartylistViewSet(viewsets.ModelViewSet):
    queryset = Partylist.objects.all()
    serializer_class = PartylistSerializer
    permission_classes = [IsAuthenticated]

class CandidateViewSet(viewsets.ModelViewSet):
    queryset = Candidate.objects.all()
    serializer_class = CandidateSerializer
    permission_classes = [IsAuthenticated]

class VoterViewSet(viewsets.ModelViewSet):
    queryset = Voter.objects.all()
    serializer_class = VoterSerializer
    permission_classes = [IsAuthenticated]

    @action(detail=False, methods=['POST'], url_path='import')
    def import_voters(self, request):
        file_obj = request.FILES.get('file', None)
        if not file_obj:
            return Response({'error': 'No file uploaded'}, status=status.HTTP_400_BAD_REQUEST)
        
        try:
            # Assuming CSV with columns: student_id, name, email
            decoded_file = file_obj.read().decode('utf-8').splitlines()
            reader = csv.DictReader(decoded_file)
            
            created_count = 0
            for row in reader:
                _, created = Voter.objects.get_or_create(
                    student_id=row['student_id'],
                    defaults={
                        'name': row['name'],
                        'email': row['email']
                    }
                )
                if created:
                    created_count += 1
            
            return Response({'success': f'{created_count} voters imported successfully'}, status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

class VoteRecordViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = VoteRecord.objects.all()
    serializer_class = VoteRecordSerializer
    permission_classes = [IsAuthenticated]

class DashboardStatsView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        stats = {
            'active_elections': Election.objects.filter(status='ACTIVE').count(),
            'total_candidates': Candidate.objects.count(),
            'total_voters': Voter.objects.count(),
            'total_votes': VoteRecord.objects.count(),
        }
        return Response(stats)

class VoterLoginView(APIView):
    permission_classes = []  # Publicly accessible for login

    def post(self, request):
        student_id = request.data.get('student_id')
        token = request.data.get('token')

        if not student_id or not token:
            return Response({'error': 'Student ID and Token are required'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            voter = Voter.objects.get(student_id=student_id, unique_voting_token=token)
            if voter.has_voted:
                return Response({'error': 'You have already cast your vote'}, status=status.HTTP_403_FORBIDDEN)
            
            serializer = VoterSerializer(voter)
            return Response(serializer.data)
        except Voter.DoesNotExist:
            return Response({'error': 'Invalid Student ID or Token'}, status=status.HTTP_401_UNAUTHORIZED)

class ActiveElectionViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Election.objects.filter(status='ACTIVE')
    serializer_class = ElectionSerializer
    permission_classes = [] # In a real app, use token-based auth for voters

    @action(detail=True, methods=['GET'])
    def ballot(self, request, pk=None):
        election = self.get_object()
        positions = Position.objects.filter(election=election)
        
        data = []
        for pos in positions:
            candidates = Candidate.objects.filter(position=pos)
            pos_data = PositionSerializer(pos).data
            pos_data['candidates'] = CandidateSerializer(candidates, many=True).data
            data.append(pos_data)
            
        return Response(data)

class BallotSubmissionView(APIView):
    permission_classes = [] # In a real app, use token-based auth for voters

    def post(self, request):
        student_id = request.data.get('student_id')
        token = request.data.get('token')
        election_id = request.data.get('election_id')
        selections = request.data.get('selections') # List of candidate IDs

        try:
            voter = Voter.objects.get(student_id=student_id, unique_voting_token=token)
            if voter.has_voted:
                return Response({'error': 'Vote already cast'}, status=status.HTTP_403_FORBIDDEN)
            
            election = Election.objects.get(id=election_id, status='ACTIVE')
            
            # Create VoteRecords
            for candidate_id in selections:
                candidate = Candidate.objects.get(id=candidate_id)
                VoteRecord.objects.create(
                    election=election,
                    position=candidate.position,
                    candidate=candidate
                )
            
            voter.has_voted = True
            voter.save()
            
            return Response({'success': 'Vote cast successfully'}, status=status.HTTP_201_CREATED)
        except (Voter.DoesNotExist, Election.DoesNotExist, Candidate.DoesNotExist) as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
