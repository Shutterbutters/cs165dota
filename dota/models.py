from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class Team(models.Model):
    TeamID = models.IntegerField(primary_key = True)
    TeamName = models.CharField(max_length = 30)
    Wins = models.IntegerField()
    Losses = models.IntegerField()

class Match(models.Model):
    MatchID = models.IntegerField(primary_key = True)
    MatchResult = models.CharField(max_length = 30)
    Team1ID = models.ForeignKey(Team, on_delete=models.CASCADE, related_name = 'one')
    Team2ID = models.ForeignKey(Team, on_delete=models.CASCADE, related_name = 'two')

class Player(models.Model):
    PlayerID = models.IntegerField(primary_key = True)
    Player_Name = models.CharField(max_length = 30)
    Is_Captain = models.IntegerField()
    Team_Mem = models.ForeignKey(Team, on_delete=models.CASCADE)
