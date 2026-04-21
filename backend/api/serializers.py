from rest_framework import serializers
from .models import Election, Position, Partylist, Candidate, Voter, VoteRecord

class ElectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Election
        fields = '__all__'

class PositionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Position
        fields = '__all__'

class PartylistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Partylist
        fields = '__all__'

class CandidateSerializer(serializers.ModelSerializer):
    position_name = serializers.CharField(source='position.name', read_only=True)
    partylist_name = serializers.CharField(source='partylist.name', read_only=True)
    
    class Meta:
        model = Candidate
        fields = '__all__'

class VoterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Voter
        fields = ['id', 'student_id', 'name', 'email', 'has_voted']
        # Note: Do not expose unique_voting_token directly in standard serializer

class VoteRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = VoteRecord
        fields = '__all__'
