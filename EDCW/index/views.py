# -*- coding: utf-8 -*-
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, StreamingHttpResponse
from django.urls import reverse
from .models import Notification
from django.conf import settings
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

    def file_iterator(file_name, chunk_size=512):
        with open(file_name, 'rb') as f:
            while True:
                c = f.read(chunk_size)
                if c:
                    yield c
                else:
                    break

    notice = get_object_or_404(Notification, pk=notice_id)
    the_partial_file_name = notice.file_attached.name
    the_file_name = os.path.join(settings.MEDIA_ROOT, the_partial_file_name)

    response = StreamingHttpResponse(file_iterator(the_file_name))
    response['Content-Type'] = 'application/octet-stream'
    response['Content-Disposition'] = 'attachment;filename="{0}"'.format(the_file_name)

    return response
#    with open(the_file_name) as f:
#        c = f.read()
#    return HttpResponse(c)
