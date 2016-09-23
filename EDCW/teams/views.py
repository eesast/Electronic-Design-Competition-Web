# -*- coding: utf-8 -*-
from django.shortcuts import render, get_object_or_404
from .models import Team, Application
from django.http import HttpResponseRedirect, Http404
from django.urls import reverse
from .forms import CreateForm, AppForm
from django.contrib.auth.decorators import login_required
def if_in_team(user):
    in_team = False
    if user.is_authenticated:
        if user.in_team.all() or user.profile.is_leader:
            in_team = True
    return in_team

def get_user_info(user):
    if user.is_authenticated:
        in_team = if_in_team(user)
        is_leader = user.profile.is_leader
        team = ''
        if is_leader:
            team = user.leads
            app_list = team.application_set.all()
        else:
            teams = user.in_team.all()
            for t in teams:
                if user in t.members.all():
                    team = t
            app_list = []

        return {
                 'in_team': in_team,
                 'is_leader': is_leader,
                 'app_list': app_list,
                 'team': team,
                 'errors': [],
                 'note': '',
        }

    return None


def index(request):
    teams = Team.objects.all()
    usr = request.user
    note = ''
    if not usr.is_authenticated:
        in_team = False
        note = '请登录之后进行操作'
    else:
        in_team = if_in_team(usr)
        if usr.application_set.all():
            in_team = True
            note = '您已经提交申请，请等候队长答复'

    return render(request, 'teams/team_index.html',
                  {'teams': teams,
                   'in_team' : in_team,
                   'note': note
                  })



def info(request, team_id):
    team = get_object_or_404(Team, pk=team_id)
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
            team.save()
        HttpResponseRedirect(reverse('teams:my_team'))

    # specify the certain page
    user = request.user
    user_info_dict = get_user_info(user)

    if user_info_dict:
        print(user_info_dict)
        return render(request, 'teams/team_myteam.html', user_info_dict)

    return HttpResponseRedirect(reverse('teams:index'))


@login_required
def acceptOrReject(request):


    user_info_dict = get_user_info(request.user)

    if request.method == 'POST':
        app_id = request.POST['app_id']
        answer = request.POST['answer']
        app = get_object_or_404(Application, pk=app_id)
        team = app.team
        in_team = if_in_team(app.applicant)
        errors = []

        if answer == 'agree':
            if team.is_full:
                errors.append('本队伍已满, 该申请已自动删除')
            if in_team:
                errors.append('该同学已在某个队伍中，该申请已自动删除')

            if not errors:
                team.members.add(app.applicant)
                if team.members.count() >= 3:
                    team.is_full = True
                    team.save()
                # delete all the applications from this applicant
                Application.objects.filter(applicant=app.applicant).delete()


            user_info_dict['errors'] = errors

        elif answer == 'disagree':

            user_info_dict['note'] = '已拒绝该请求'

        app.delete()

        return render(request, 'teams/team_myteam.html', user_info_dict)

    raise Http404

@login_required
def application(request, team_id):
    team = get_object_or_404(Team, pk=team_id)
    user = request.user
    in_team = if_in_team(user)
    error = ''

    if in_team:
        return HttpResponseRedirect(reverse('teams:index'))


    if request.method =='POST':

        apps = user.application_set.filter(team=team)
        if apps.count():
            error = '您已经申请加入该队伍，请等候队长审核'

        else:
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
                      'in_team' : in_team,
                      'error' : error
                  })

@login_required
def create(request):
    errors = []
    if request.method == 'POST':
        form = CreateForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            name = cd['name']
            intro = cd['intro']
            if request.user.in_team.all() or request.user.profile.is_leader:
                errors.append('您已经在队伍中')

            exist = Team.objects.filter(name=name)
            if exist.count():
                errors.append('队名已被使用')

            if errors:
                return render(request, 'teams/team_create.html', {'errors' : errors })

            else:
                team = Team(name=name, intro=intro, leader=request.user)
                team.save()
                request.user.profile.is_leader = True
                request.user.profile.save()
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
