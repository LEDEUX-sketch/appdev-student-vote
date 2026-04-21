from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    ElectionViewSet, PositionViewSet, PartylistViewSet,
    CandidateViewSet, VoterViewSet, VoteRecordViewSet
)

router = DefaultRouter()
router.register(r'elections', ElectionViewSet)
router.register(r'positions', PositionViewSet)
router.register(r'partylists', PartylistViewSet)
router.register(r'candidates', CandidateViewSet)
router.register(r'voters', VoterViewSet)
router.register(r'votes', VoteRecordViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
