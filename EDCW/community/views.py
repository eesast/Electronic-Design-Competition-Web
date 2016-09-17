from django.shortcuts import render, render_to_response,HttpResponseRedirect
from community import forms
from community.models import Post,PostFile,Comment,Category
from django.core.paginator import Paginator, InvalidPage, EmptyPage, PageNotAnInteger
from django.contrib.auth import authenticate, login
from community.forms import PostForm,CommentForm

def community_content(request,id):
	post = Post.objects.get(id=int(id))
	if 	request.user.is_authenticated() :
		if request.method=='POST':
			form = CommentForm(request.POST)
			if form.is_valid():
				cd = form.cleaned_data
				comment = Comment(content=cd['comment'],post = Post.objects.get(id=int(id)),replier=request.user)
				comment.save()
				comment.post.replycount+=1
			else:
				form = CommentForm()
		commentlist = post.p_comment.all()		
		return render(request,'community_content_after_login.html',{'post':post,'commentlist':commentlist})
	else:
		commentlist = post.p_comment.all()	
		return render(request,'community_content.html',{'post':post,'commentlist':commentlist})



def community_create(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            print (2)
            cd = form.cleaned_data
            post = Post(title=cd['title'],content=cd['body'],sender=request.user,summary=cd['outline'],category=cd['category'])
            post.save()
            return HttpResponseRedirect('/community_index')
    else:
        form = PostForm()
    return render(request,'community_create.html', {'form': form})
        




def community_index(request,page=1):
	post_list = Post.objects.all()
	paginator = Paginator(post_list,5)
	try:
		page = int (request.GET.get('page','1'))
	except ValueError:
		page = 1
	try:
		posts = paginator.page(page)
	except (EmptyPage,InvalidPage):
		posts = paginator.page(paginator.num_pages)
	for i in range(page,page+3):
		if i > paginator.num_pages:
			break
		maxpage = i
	for i in range(page,page-3,-1):
		if i < 1:
			break
		minpage = i
	pagerange=range(minpage,maxpage+1)
	if request.user.is_authenticated():
		return render(request,'community_index_after_login.html',{"posts":posts,"pagerange":pagerange,})
	else:
		return render(request,'community_index.html',{"posts":posts,"pagerange":pagerange,})



def delpost(request,id):
	post = Post.objects.get(id=int(id))
	post.delete()
	return Httpresponse()
	
def delcomment(request,id):
	comment = Comment.objects.get(id=int(id))
	comment.delete()
	return Httpresponse()




# Create your views here.
