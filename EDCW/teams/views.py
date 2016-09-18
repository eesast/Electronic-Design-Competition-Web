# -*- coding: utf-8 -*-
from django.shortcuts import render, get_object_or_404
from .models import Team, Application
from django.http import HttpResponseRedirect
from django.urls import reverse
from .forms import CreateForm, AppForm
def index(request):
    teams = Team.objects.all()
    return render(request, 'teams/team_index.html', {'teams': teams})


def info(request, team_id):
    team = Team.objects.get(pk=team_id)
    return render(request, 'teams/team_info.html', {'team': team })

def my_team(request):

    # kickout a member in a certain team
    if request.method == 'POST':
        try:
            name = request.POST['name']
            team = request.user.leads
            thisone = team.members.get(username=name)
            team.members.remove(thisone)
            if team.members.count() < 3:
                team.is_full = False
        except Exception:
            pass

    # specify the certain page
    if request.user.is_authenticated:
        try:
            is_leader = request.user.profile.is_leader
            if is_leader:
                team = request.user.leads
                app_list = team.application_set.all()
            else:
                team = request.user.in_team.get(pk=1)
                app_list = []

            return render(request, 'teams/team_myteam.html',
                          {'team': team,
                           'app_list': app_list,
                           'is_leader': is_leader,
                          })

        except Exception:
            # print you're not in a team
            return HttpResponseRedirect(reverse('teams:index'))

    # print you're not registered
    return HttpResponseRedirect(reverse('teams:index'))


def acceptOrReject(request):

    if request.method == 'POST':
        app_id = request.POST['app_id']
        answer = request.POST['answer']
        app = Application.objects.get(pk=app_id)
        team = app.team

        if answer == 'agree' and not team.is_full:
            team.members.add(request.user)

            if team.members.count() >= 3:
                team.is_full = True

        app.delete()

    return HttpResponseRedirect(reverse('teams:my_team'))



def application(request, team_id):
    team = get_object_or_404(Team, pk=team_id)

    if request.method =='POST':
        form = AppForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            reason = cd['reason']
            app = Application(applicant=request.user, team=team, reason=reason)
            app.save()
            return HttpResponseRedirect(reverse('teams:index'))



    return render(request, 'teams/team_join.html',
                  {
                      'team' : team,
                      'username' : request.user.username,
                  }
                  )

def create(request):

    if request.method == 'POST':
        form = CreateForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            name = cd['name']
            intro = cd['intro']
            team = Team(name=name, intro=intro, leader=request.user)
            team.save()
            request.user.profile.is_leader = True
            return HttpResponseRedirect(reverse('teams:my_team'))

    return render(request, 'teams/team_create.html')

def dismiss(request):

    if request.method == 'POST':
        user = request.user
        team_id = request.POST['team_id']
        team = get_object_or_404(Team, pk=team_id)
        team.members.clear()
        team.delete()
        user.profile.is_leader = False
        user.profile.save()

    return HttpResponseRedirect(reverse('teams:index'))
