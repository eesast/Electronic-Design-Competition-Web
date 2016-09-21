# -*- coding: utf-8 -*-
from django.shortcuts import render, HttpResponseRedirect,render_to_response
from django.contrib.auth.models import User
from django.conf import settings
from django.urls import reverse
from login.models import Member
from .forms import LoginForm
import urllib
import urllib.request
import json
import os
from django.contrib.auth import login,logout



def	get_access_token(username,password):
    auth_url = 'https://www.eesast.com/o/token/'
    body = urllib.parse.urlencode({
    'client_id':settings.EESAST_CLIENTID,
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
		userinfo_url = 'https://www.eesast.com/account/userinfo/'
		req = urllib.request.Request(userinfo_url,headers = headers)
		resp = urllib.request.urlopen(req)
		resp = resp.read()
		resp = resp.decode('utf-8')
		data = json.loads(resp)
		return data
	else:
		return none

def check_user(data):
    if not 'name' in data or not 'student_ID' in data:
        raise Exception
    try:
        user1 = User.objects.get(username=data['name'])
        user1.profile.student_id = data['student_ID']
        user1.profile.save()
        return user1
    except User.DoesNotExist :
        user2 = User(username=data['name'])
        user2.save()
        member = Member(user=user2, student_id=data['student_ID'])
        member.save()
        return user2

def Login(request):
    error = ''
    access_token=''
    if_logout=''


    if request.method =='POST':

        if request.user.is_authenticated:
            if 'logout' in request.POST:
                Logout(request)
            else:
                error = Get_Image(request)
                return render(request, 'login/login.html', {'error':error})

        else:
            form = LoginForm(request.POST)
            if form.is_valid():
                cd = form.cleaned_data
                try:
                    access_token = get_access_token(cd['username'],cd['password'])
                    data = get_user_info(access_token)
                    user = check_user(data)
                    login(request,user)
                except Exception:
                    error = '登录申请失败！请确认用户名与密码是否正确，以及学号与姓名信息是否完整!'
    else:
        form = LoginForm()
        print(error)
    return render(request, 'login/login.html', {'error':error})

def Get_Image(request):
    profile=request.user.profile
    old_name = request.user.profile.image.name

    if not 'image' in request.FILES:
        return '请上传一个文件'

    photo=request.FILES['image']
    name=photo.name.lower()
    if not name.endswith(('.jpg', '.png', '.jpeg', '.gif')):
        return '请上传一个规范格式的图片'

    profile.image=photo
    profile.save()
    if old_name != 'custom.png':
        try:
            os.remove(settings.MEDIA_ROOT+old_name)
        except Exception:
            pass

    initial_path=profile.image.path

    tye = name.split('.')[-1]
    profile.image.name=os.path.join('/' , 'head_images', 'user_%s_%s.%s' %(request.user.username,request.user.id,tye))
    new_path=settings.MEDIA_ROOT + profile.image.name
    os.rename(initial_path,new_path)
    profile.save()






def Logout(request):
	logout(request)
	return HttpResponseRedirect("/index")



def ResetPassword(request):


	return HttpResponseRedirect("www.EESAST/account/resetpasswordrequest")


















