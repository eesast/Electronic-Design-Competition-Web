# -*- coding: utf-8 -*-
from django.shortcuts import render, get_object_or_404
from .models import Team, Application
from django.http import HttpResponseRedirect
from django.urls import reverse
from .forms import CreateForm, AppForm
def if_in_team(usr):
    in_team = False
    if usr.is_authenticated:
        if usr.in_team.all() or usr.profile.is_leader:
            in_team = True
    return in_team




def index(request):
    teams = Team.objects.all()
    usr = request.user
    in_team = if_in_team(usr)
    return render(request, 'teams/team_index.html',
                  {'teams': teams,
                   'in_team' : in_team,
                  })



def info(request, team_id):
    team = Team.objects.get(pk=team_id)
    usr = request.user
    in_team = if_in_team(usr)
    return render(request, 'teams/team_info.html',
                  {'team': team,
                   'in_team': in_team,
                  })

def my_team(request):

    # kickout a member in a certain team
    if request.method == 'POST':
        name = request.POST['name']
        team = request.user.leads
        thisone = team.members.get(username=name)
        team.members.remove(thisone)
        if team.members.count() < 3:
             team.is_full = False


    # specify the certain page
    user = request.user
    team = ''
    if user.is_authenticated:
        in_team = False
        is_leader = user.profile.is_leader
        if is_leader:
            team = user.leads
            app_list = team.application_set.all()
            in_team = True
        else:
            teams = user.in_team.all()
            for t in teams:
                if user in t.members.all():
                    team = t
                    in_team = True
            app_list = []


        return render(request, 'teams/team_myteam.html',
                      {'team': team,
                       'app_list': app_list,
                       'is_leader': is_leader,
                       'in_team': in_team,
                      })
    return HttpResponseRedirect(reverse('teams:index'))


def acceptOrReject(request):

    if request.method == 'POST':
        app_id = request.POST['app_id']
        answer = request.POST['answer']
        app = Application.objects.get(pk=app_id)
        team = app.team

        if answer == 'agree' and not team.is_full:
            team.members.add(app.applicant)

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

    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('login:login'))

    errors = []

    if request.method == 'POST':
        form = CreateForm(request.POST)
        if form.is_valid():
            print(1)
            cd = form.cleaned_data
            name = cd['name']
            intro = cd['intro']
            print(2)
            if request.user.in_team.all() or request.user.profile.is_leader:
                print(3)
                errors.append('您已经在队伍中')

            exist = Team.objects.filter(name=name)
            print(4)
            if exist.count():
                print(5)
                errors.append('队名已被使用')

            if errors:
                print(6)
                return render(request, 'teams/team_create.html', {'errors' : errors })

            else:
                print(7)
                team = Team(name=name, intro=intro, leader=request.user)
                team.save()
                request.user.profile.is_leader = True
                request.user.profile.save()
                return HttpResponseRedirect(reverse('teams:my_team'))
    print(8)
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
