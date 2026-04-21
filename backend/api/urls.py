from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    ElectionViewSet, PositionViewSet, PartylistViewSet,
    CandidateViewSet, VoterViewSet, VoteRecordViewSet,
    DashboardStatsView, VoterLoginView, ActiveElectionViewSet,
    BallotSubmissionView
)

router = DefaultRouter()
router.register(r'elections', ElectionViewSet)
router.register(r'positions', PositionViewSet)
router.register(r'partylists', PartylistViewSet)
router.register(r'candidates', CandidateViewSet)
router.register(r'voters', VoterViewSet)
router.register(r'votes', VoteRecordViewSet)
router.register(r'active-elections', ActiveElectionViewSet, basename='active-elections')

urlpatterns = [
    path('', include(router.urls)),
    path('dashboard-stats/', DashboardStatsView.as_view(), name='dashboard-stats'),
    path('voter/login/', VoterLoginView.as_view(), name='voter-login'),
    path('voter/submit-vote/', BallotSubmissionView.as_view(), name='submit-vote'),
]
