import csv
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import Election, Position, Partylist, Candidate, Voter, VoteRecord
from .serializers import (
    ElectionSerializer, PositionSerializer, PartylistSerializer,
    CandidateSerializer, VoterSerializer, VoteRecordSerializer
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
