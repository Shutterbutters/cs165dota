from django import forms

class TeamNew(forms.Form):
    teamName = forms.CharField(label='Team Name', max_length=30)
    teamWins = forms.IntegerField(label='Wins')
    teamLosses = forms.IntegerField(label='Losses')

class MatchNew(forms.Form):
    matchResult = forms.CharField(label='Match Result', max_length=30)
    team1ID = forms.IntegerField(label='Radiant TeamID')
    team2ID = forms.IntegerField(label='Dire TeamID')

class PlayerNew(forms.Form):
    playerName = forms.CharField(label='Player Name', max_length=30)
    isCap = forms.IntegerField(label='Is Captain')
    teamID = forms.IntegerField(label='Team ID') 
