from django.shortcuts import render, HttpResponseRedirect,render_to_response
from django.contrib.auth.models import User
from login.models import Member
import urllib


EESAST_CLIENTID = settings.EESAST_CLIENTID
EESAST_CLIENSECRET = settings.EESAST_CLIENTSECRET
EESAST_CALLBACK = settings.EESAST_CALLBACK
EESAST_AUTHORIZE_URL = settings.EESAST_AUTHORIZE_URL


def	get_access_token(username,password):
	auth_url = 'http://www.eesast.com/o/token'
	body = urllib.parse.urlencode({
		'client_id':EESAST_CLIENTID,
		'grant_type':'password',
		'username':username,
		'password':password,
		})
	body = urllib.parse.urlencode(body)
	body = body.encode('utf-8')
	headers = {'Content-Type':'application/x-www-form-urlencoded'}
	req = urllib.request.Request(url, body, headers)
	resp = urllib.request.urlopen(req)
	resp = resp.read()
	resp = resp.decode('utf-8')
	data = json.loads(resp)
	return data['access_token']
	
def get_user_info(access_token):
	if access_token:
		headers = {'Authorization': Access_Token}
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
		user1 = User.objects.get(username=data[username])
		return user1
	except:
		user2 = User.objects.get.create_user(username=data[username],
		password=data[password])
		user2.save()
		member = Member(user=user2,group="管理员")
		member.save()
		return user2
		
def login(request):
	if request.method =='POST':
		form = LoginForm(request.Post)
		if form.os_valid():
			cd = form.cleaned_data
			try:
				access_token = get_access_token(cd['username'],cd['password'])
				data = get_user_info(access_token)
				user = check_user(data)
				login(request, user)
				return render_to_response('logindone.html',{'mes':"您已成功登陆！"})
			except:
				error = '登录申请失败！请先注册！'
	else:
		form = LoginForm()
	return render_to_response('login.html',{'form':form},{'error':error})
				
def Logout(request):
	logout(request)
	return HttpResponseRedirect("/index")



def ResetPassword(request):
	return HttpResponseRedirect("www.EESAST/account/resetpasswordrequest")
	
	
	
	
	
	
	
	
	
	
	
	
	
	

	
	

# Create your views here.
