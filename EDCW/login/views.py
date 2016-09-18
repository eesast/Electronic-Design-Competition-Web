# -*- coding: utf-8 -*-
from django.shortcuts import render, HttpResponseRedirect,render_to_response
from django.contrib.auth.models import User
from django.conf import settings
from login.models import Member
from .forms import LoginForm
import urllib
import json
from django.contrib.auth import authenticate, login,logout



def	get_access_token(username,password):
    auth_url = 'http://www.eesast.com/o/token/'
    body = urllib.parse.urlencode({
    'client_id':'HJjxmkjuD7yUyaYwqWYNRqxhsBDowOtmYfrVpMEi',
    'grant_type':'password',
    'username':username,
    'password':password,
    })
    body = body.encode('utf-8')
    headers = {'Content-Type':'application/x-www-form-urlencoded'}
    req = urllib.request.Request(auth_url, body, headers=headers)
    resp = urllib.request.urlopen(req)
    resp = resp.read()
    resp = resp.decode('utf-8')
    data = json.loads(resp)
    return data['access_token']

def get_user_info(access_token):
	if access_token:
		headers = {'Authorization': "Bearer %s" %access_token}
		userinfo_url = 'http://www.eesast.com/account/userinfo/'
		req = urllib.request.Request(userinfo_url,headers = headers)
		resp = urllib.request.urlopen(req)
		resp = resp.read()
		resp = resp.decode('utf-8')
		data = json.loads(resp)
		return data
	else:
		return none

def check_user(data):
    try:
        user1 = User.objects.get(username=data['name'])
        user1.profile.student_id = data['student_id']
        user1.profile.save()

        return user1
    except:
        user2 = User(username=data['name'])
        user2.save()
        member = Member(user=user2, student_id=data['student_ID'])
        member.save()
        return user2

def Login(request):
    error = ''
    access_token=''
    if_logout=''
    try:
        if_logout=request.POST.get('logout','')
        if if_logout=='zhuxiao':
            Logout(request)
    except Exception:
        pass
    if request.method =='POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            try:
                access_token = get_access_token(cd['username'],cd['password'])
                data = get_user_info(access_token)
                user = check_user(data)
                login(request,user)
            except Exception:
                error = '登录申请失败！请先注册！'
    else:
        form = LoginForm()
    return render(request, 'login.html', {'error':error})

def Logout(request):
	logout(request)
	return HttpResponseRedirect("/index")



def ResetPassword(request):


	return HttpResponseRedirect("www.EESAST/account/resetpasswordrequest")


















