from django.shortcuts import render
from django.http import HttpResponseRedirect, StreamingHttpResponse
from django.urls import reverse
from .models import Notification
def index(request):

    return render(request, 'index/index.html')

def welcome(request):

    return render(request, 'index/Welcome.html')


def noticeIndex(request):

    notice_list = Notification.objects.all()
    return render(request, 'index/notice.html', {'notice_list' : notice_list})

def download(request):

    def file_iterator(file_name, chunk_size=512):
        with open(file_name) as f:
            while True:
                c = f.read(chunk_size)
                if c:
                    yield c
                else:
                    break

    the_partial_file_name = Notification.objects.get(pk=request.POST['choice']).file_attached.name
    the_file_name = u'/home/alxl/' + the_partial_file_name

    response = StreamingHttpResponse(file_iterator(the_file_name))
    response['Content-Type'] = 'application/octet-stream'
    response['Content-Disposition'] = 'attachment;filename="{0}"'.format(the_file_name)

    return response
#    with open(the_file_name) as f:
#        c = f.read()
#    return HttpResponse(c)
