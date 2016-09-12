from django.shortcuts import render, render_to_response
from community import forms
from community import models
from django.core.paginator import Paginator, InvalidPage, EmptyPage, PageNotAnInteger



def community_content(request):
    return render(request,'community_content.html')



def community_create(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            cd.save()
            return HttpResponseRedirect('/community_index')
    else:
        form = PostForm()
    return render_to_response('community_create.html', {'form': form})





def community_index(request):
    post_list = Post.objects.all()
    paginator = Paginator(post_list,5)
    try:
        page = int(request,GET.get('page','1'))
    except ValueError:
        page = 1
    try:
        posts = paginator.page(page)
    except(EmptyPage,InvalidPage):
        posts = (paginator.num_pages,PageNotAnInteger)
    if page >= after_range_num:
        page_range = paginator.page_range[page-after_range_num:page+before_range_num]
    else:
        page_range = paginator.page_range[0:int(page)+before_range_num]
        template_var["page_range"] = page_range

    return render_to_response('community_index',{"posts":posts})








# Create your views here.
