from django.db import models
from django.utils.crypto import get_random_string

class Election(models.Model):
    STATUS_CHOICES = (
        ('DRAFT', 'Draft'),
        ('ACTIVE', 'Active'),
        ('COMPLETED', 'Completed'),
    )
    title = models.CharField(max_length=255)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='DRAFT')

    def __str__(self):
        return self.title

class Position(models.Model):
    election = models.ForeignKey(Election, on_delete=models.CASCADE, related_name='positions')
    name = models.CharField(max_length=150)
    max_votes_allowed = models.IntegerField(default=1)
    hierarchy_order = models.IntegerField(default=0)

    class Meta:
        ordering = ['hierarchy_order']

    def __str__(self):
        return f"{self.name} - {self.election.title}"

class Partylist(models.Model):
    election = models.ForeignKey(Election, on_delete=models.CASCADE, related_name='partylists')
    name = models.CharField(max_length=150)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

class Candidate(models.Model):
    position = models.ForeignKey(Position, on_delete=models.CASCADE, related_name='candidates')
    partylist = models.ForeignKey(Partylist, on_delete=models.SET_NULL, null=True, blank=True, related_name='candidates')
    name = models.CharField(max_length=255)
    photo = models.ImageField(upload_to='candidate_photos/', blank=True, null=True)
    platform_statement = models.TextField(blank=True, null=True)
    course_and_year = models.CharField(max_length=150, blank=True, null=True)

    def __str__(self):
        return self.name

class Voter(models.Model):
    student_id = models.CharField(max_length=50, unique=True)
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    unique_voting_token = models.CharField(max_length=64, unique=True, blank=True)
    has_voted = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        if not self.unique_voting_token:
            self.unique_voting_token = get_random_string(32)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.name} ({self.student_id})"

class VoteRecord(models.Model):
    election = models.ForeignKey(Election, on_delete=models.CASCADE, related_name='votes')
    position = models.ForeignKey(Position, on_delete=models.CASCADE, related_name='votes')
    candidate = models.ForeignKey(Candidate, on_delete=models.CASCADE, related_name='votes')
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Vote for {self.candidate.name} under {self.position.name}"
