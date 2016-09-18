# -*- coding: utf-8 -*-
from django.shortcuts import render
from .models import Team,Member
from django.http import HttpResponseRedirect
from django.urls import reverse
def index(request):
    teams = Team.objects.all()
    return render(request, 'teams/team_index.html', {'teams': teams})


def info(request, team_id):
    team = Team.objects.get(pk=team_id)
    return render(request, 'teams/team_info.html', {'team': team })

def my_team(request):
    return render(request, 'teams/team_myteam.html')


def join(request):


    if request.method =='POST':
        form = AppForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data



        HttpResponseRedirect(reverse('teams:index'))


    teams = Team.objects.all()
    return render(request, 'teams/team_index.html', { 'teams': teams })

def application(request, team_id):
    if request.method =='POST':
        form = AppForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
        # 增加一个application instance

    team = Team.objects.get(pk=team_id)
    return render(request, 'teams/team_join.html', {'team' : team})

def create(request):
    return render(request, 'teams/team_create.html')


