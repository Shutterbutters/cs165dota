from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login, name='login'),
    path('teams/', views.teams, name='teams'),
    path('teams/<int:TeamID>/', views.teamDetail, name='teamDetail'),
    path('matches/', views.matches, name='matches'),
    path('matches/<int:MatchID>/', views.matchDetail, name='matchDetail'),
    path('players/', views.players, name='players'),
    path('players/<int:PlayerID>/', views.playerDetail, name='playerDetail'),
    path('teams/create', views.teamCreate, name='teamCreate'),
    path('matches/create', views.matchCreate, name='matchCreate'),
    path('players/create', views.playerCreate, name='playerCreate'),
    path('teams/<int:TeamID>/edit', views.teamEdit, name='teamEdit'),
    path('matches/<int:MatchID>/edit', views.matchEdit, name='matchEdit'),
    path('players/<int:PlayerID>/edit', views.playerEdit, name='playerEdit'),
    path('teams/<int:TeamID>/delete', views.teamDelete, name='teamDelete'),
    path('matches/<int:MatchID>/delete', views.matchDelete, name='matchDelete'),
    path('players/<int:PlayerID>/delete', views.playerDelete, name='playerDelete'),
    path('noteam',views.noteam, name='noteam'),

]
