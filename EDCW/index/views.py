# -*- coding: utf-8 -*-
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, StreamingHttpResponse, HttpResponse
from django.urls import reverse
from .models import Notification
from django.conf import settings
from wsgiref.util import FileWrapper
import os
def introduction(request):

    return render(request, 'index/introduction.html')

def index(request):

    return render(request, 'index/index.html')

def rule(request):

    return render(request, 'index/rule.html')

def noticeIndex(request):

    notice_list = Notification.objects.all()
    return render(request, 'index/notice.html', {'notice_list' : notice_list})

def download(request, notice_id):


    notice = get_object_or_404(Notification, pk=notice_id)
    path = notice.file_attached.path
    name = notice.file_attached.name

    wrapper = FileWrapper(open(path, 'rb'))
    response = HttpResponse(wrapper, content_type='text/plain')
    response['Content-Length'] = os.path.getsize(path)
#    response = StreamingHttpResponse(file_iterator(the_file_name))
#    response['Content-Type'] = 'application/octet-stream'
    response['Content-Disposition'] = 'attachment;filename="{0}"'.format(os.path.split(name)[-1])
    return response

#    with open(the_file_name) as f:
#        c = f.read()
#    return HttpResponse(c)
