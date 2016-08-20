from django.conf.urls import url
from . import views

app_name = 'index'

urlpatterns = [
    url(r'^$', views.welcome, name='welcome'),
    url(r'^index', views.index, name='index'),
    url(r'^notice', views.noticeIndex, name='notice'),
]
