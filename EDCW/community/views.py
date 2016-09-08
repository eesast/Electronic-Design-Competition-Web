from django.shortcuts import render, render_to_response
from community import forms
from community import models
import os


def community_content(request):

    return render(request,'community_content.html')

def community_create(request):
    errors = []
    if request.method == 'POST':
        if not request.POST.get('title', ''):
            errors.append('Enter a title.')
        if not request.POST.get('body', ''):
            errors.append('Enter a body.')
        if not errors:
            post = Post(title=request.POST.get('title', ''),content=request.POST.get('body', ''),summary=request.POST.get('outline', ''),)
            return HttpResponseRedirect('/community_index')
    return render_to_response('community_create.html', {
        'errors': errors,
        'title': request.POST.get('title', ''),
        'outline': request.POST.get('outline', ''),
        'body': request.POST.get('body', ''),
    })


    
	
def community_index(request):

    return render(request,'community_index.html')
	
def handle_upload_file(f,request): 
    base_img_upload_path = 'static/Uploads'
    user_path = "%s/%s" % (base_img_upload_path,request.user.userprofile.id)
    if not os.path.exists(user_path):
        os.mkdir(user_path)
    with open('%s/%s'% (user_path,f.name),'wb+') as destinations:
        for chunk in f.chunks():
            destinations.write(chunk)

	
	
def new_Post(request):
    category_list = models.Category.objects.all()
    if request.method == 'Post':
        form = PostForm(request.POST,request.FILES)
        if form.is_valid():
            form_data = form.cleaned_data
            form_data['sender_id'] = request.user.userprofile.id
            new_img_path = handle_upload_file(request.FILES['head_img'],request)
            form_data['head_img'] = new_img_path
            new_post_obj = models.Post(**form_data)
            new_post_obj.save()
            return render(request,'community_create.html',{'new_article_obj':new_article_obj})
        else:
            print (form.errors)
			
    return render(request,'new_post.html',{'category_list':category_list})
# Create your views here.
