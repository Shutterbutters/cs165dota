from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.contrib.auth import authenticate, login

from .models import Team, Match, Player
from .forms import TeamNew, MatchNew, PlayerNew

# Create your views here.
def index(request):
    template = loader.get_template('dota/index.html')
    context = {}
    return HttpResponse(template.render(context, request))

def teams(request):
    teamlist = Team.objects.order_by('TeamID')
    template = loader.get_template('dota/teams.html')
    context = {
        'teamlist':teamlist,
    }
    return HttpResponse(template.render(context, request))

def matches(request):
    teamlist = Team.objects.order_by('TeamID')
    matchlist = Match.objects.order_by('MatchID')
    template = loader.get_template('dota/matches.html')
    context = {
        'teamlist': teamlist,
        'matchlist': matchlist,
    }
    return HttpResponse(template.render(context, request))

def players(request):
    teamlist = Team.objects.order_by('TeamID')
    playerlist = Player.objects.order_by('PlayerID')
    template = loader.get_template('dota/players.html')
    context = {
        'teamlist': teamlist,
        'playerlist': playerlist,
    }
    return HttpResponse(template.render(context, request))

def teamDetail(request, TeamID):
    thisTeam = Team.objects.get(TeamID = TeamID)
    playerlist = Player.objects.filter(Team_Mem = TeamID)
    matchlist1 = Match.objects.filter(Team1ID = TeamID)
    matchlist2 = Match.objects.filter(Team2ID = TeamID)
    template = loader.get_template('dota/teamDetail.html')
    context = {
        'thisTeam':thisTeam,
        'playerlist':playerlist,
        'matchlist1':matchlist1,
        'matchlist2':matchlist2,
        'tid':TeamID,
    }
    return HttpResponse(template.render(context, request))

def matchDetail(request, MatchID):
    match = Match.objects.get(MatchID = MatchID)
    playerlist1 = Player.objects.filter(Team_Mem = match.Team1ID)
    playerlist2 = Player.objects.filter(Team_Mem = match.Team2ID)
    template = loader.get_template('dota/matchDetail.html')
    context = {
        'match':match,
        'radiant':playerlist1,
        'dire':playerlist2,
    }
    return HttpResponse(template.render(context, request))

def playerDetail(request, PlayerID):
    thisPlayer = Player.objects.get(PlayerID = PlayerID)
    TeamID = thisPlayer.Team_Mem.TeamID
    matchlist1 = Match.objects.filter(Team1ID = TeamID)
    matchlist2 = Match.objects.filter(Team2ID = TeamID)
    template = loader.get_template('dota/playerDetail.html')
    context = {
        'thisPlayer':thisPlayer,
        'm1' : matchlist1,
        'm2' : matchlist2,
    }
    return HttpResponse(template.render(context, request))

def teamCreate(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = TeamNew(request.POST)
        # check whether it's valid:
        if form.is_valid():
            teamName = form.cleaned_data['teamName']
            teamWins = form.cleaned_data['teamWins']
            teamLosses = form.cleaned_data['teamLosses']
            teamID = Team.objects.all().order_by("-TeamID")[0].TeamID + 1
            newTeam = Team(TeamID = teamID, TeamName = teamName, Wins = teamWins, Losses = teamLosses)
            newTeam.save()
            return HttpResponseRedirect('/dota/teams/')
    # if a GET (or any other method) we'll create a blank form
    else:
        form = TeamNew()

    return render(request, 'dota/teamCreate.html', {'form': form})

def playerCreate(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = PlayerNew(request.POST)
        # check whether it's valid:
        if form.is_valid():
            playerName = form.cleaned_data['playerName']
            isCap = form.cleaned_data['isCap']
            if(isCap != 0):
                isCap = 1
            teamID = form.cleaned_data['teamID']
            if Team.objects.filter(TeamID = teamID).count() > 0:
                team = Team.objects.get(TeamID = teamID)
                pid = Player.objects.all().order_by("-PlayerID")[0].PlayerID + 1
                newPlayer = Player(PlayerID = pid, Player_Name = playerName, Is_Captain = isCap, Team_Mem = team)
                newPlayer.save()
                return HttpResponseRedirect('/dota/players/')
            else:
                return HttpResponseRedirect('/dota/noteam')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = PlayerNew()
    return render(request, 'dota/playerCreate.html', {'form': form})

def noteam(request):
    template = loader.get_template('dota/noteam.html')
    context = {}
    return HttpResponse(template.render(context, request))

def matchCreate(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = MatchNew(request.POST)
        # check whether it's valid:
        if form.is_valid():
            matchResult = form.cleaned_data['matchResult']
            team1ID = form.cleaned_data['team1ID']
            team2ID = form.cleaned_data['team2ID']
            if Team.objects.filter(TeamID = team1ID).count() > 0 and Team.objects.filter(TeamID = team2ID).count() > 0:
                team1 = Team.objects.get(TeamID = team1ID)
                team2 = Team.objects.get(TeamID = team2ID)
                mid = Match.objects.all().order_by("-MatchID")[0].MatchID + 1
                newMatch = Match(MatchID = mid, MatchResult = matchResult, Team1ID = team1, Team2ID = team2)
                newMatch.save()
                return HttpResponseRedirect('/dota/matches/')
            else:
                return HttpResponseRedirect('/dota/noteam')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = MatchNew()
    return render(request, 'dota/matchCreate.html', {'form': form})

def matchEdit(request, MatchID):
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = MatchNew(request.POST)
        # check whether it's valid:
        if form.is_valid():
            matchResult = form.cleaned_data['matchResult']
            team1ID = form.cleaned_data['team1ID']
            team2ID = form.cleaned_data['team2ID']
            if Team.objects.filter(TeamID = team1ID).count() > 0 and Team.objects.filter(TeamID = team2ID).count() > 0:
                team1 = Team.objects.get(TeamID = team1ID)
                team2 = Team.objects.get(TeamID = team2ID)
                mid = MatchID
                newMatch = Match(MatchID = mid, MatchResult = matchResult, Team1ID = team1, Team2ID = team2)
                newMatch.save()
                return HttpResponseRedirect('/dota/matches/')
            else:
                return HttpResponseRedirect('/dota/noteam')

    # if a GET (or any other method) we'll create a blank form
    else:
        match = Match.objects.get(MatchID = MatchID)
        form = MatchNew()
        context = {
            'form':form,
            'match':match,
        }
    return render(request, 'dota/matchEdit.html', context)

def playerEdit(request, PlayerID):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = PlayerNew(request.POST)
        # check whether it's valid:
        if form.is_valid():
            playerName = form.cleaned_data['playerName']
            isCap = form.cleaned_data['isCap']
            if(isCap != 0):
                isCap = 1
            teamID = form.cleaned_data['teamID']
            if Team.objects.filter(TeamID = teamID).count() > 0:
                team = Team.objects.get(TeamID = teamID)
                pid = PlayerID
                Player.objects.filter(PlayerID=PlayerID).update(Player_Name = playerName, Is_Captain = isCap, Team_Mem = team)
                return HttpResponseRedirect('/dota/players/')
            else:
                return HttpResponseRedirect('/dota/noteam')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = PlayerNew()
        thisPlayer = Player.objects.get(PlayerID = PlayerID)
        context = {
            'form':form,
            'thisPlayer':thisPlayer,
        }
    return render(request, 'dota/playerEdit.html', context)

def teamEdit(request, TeamID):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = TeamNew(request.POST)
        # check whether it's valid:
        if form.is_valid():
            teamName = form.cleaned_data['teamName']
            teamWins = form.cleaned_data['teamWins']
            teamLosses = form.cleaned_data['teamLosses']
            Team.objects.filter(TeamID=TeamID).update(TeamName = teamName, Wins = teamWins, Losses = teamLosses)
            return HttpResponseRedirect('/dota/teams/')
    # if a GET (or any other method) we'll create a blank form
    else:
        form = TeamNew()
        thisTeam = Team.objects.get(TeamID = TeamID)
        context = {
            'form':form,
            'thisTeam':thisTeam,
        }
    return render(request, 'dota/teamEdit.html', context)

def teamDelete(request, TeamID):
    team = Team.objects.get(TeamID = TeamID)
    team.delete()
    return HttpResponseRedirect('/dota/teams')

def matchDelete(request, MatchID):
    match = Match.objects.get(MatchID = MatchID)
    match.delete()
    return HttpResponseRedirect('/dota/matches')

def playerDelete(request, PlayerID):
    player = Player.objects.get(PlayerID = PlayerID)
    player.delete()
    return HttpResponseRedirect('/dota/players')
