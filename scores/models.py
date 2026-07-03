from django.db import models
from django.contrib.auth.models import User

class Match(models.Model):
    STATUS_CHOICES = [
        ('Upcoming', 'Upcoming'),
        ('Live', 'Live'),
        ('Completed', 'Completed'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE) # Tracks who created the tracker entry
    team_one = models.CharField(max_length=100)
    team_two = models.CharField(max_length=100)
    team_one_score = models.IntegerField(default=0)
    team_two_score = models.IntegerField(default=0)
    match_status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Upcoming')
    match_date = models.DateTimeField()

    def __str__(self):
        return f"{self.team_one} vs {self.team_two}"