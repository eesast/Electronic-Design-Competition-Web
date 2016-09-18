from django.conf.urls import url
from . import views

app_name = 'teams'

urlpatterns = [
    url(r'^index$', views.index , name='index'),
    url(r'^create$', views.create, name='create'),
    url(r'^info/(?P<team_id>[0-9]+)$', views.info, name='info'),
    url(r'^application/(?P<team_id>[0-9]+)$', views.application, name='application'),
    url(r'^myteam$', views.my_team, name='my_team'),
    url(r'^answer/(?P<app_id>[0-9]+)/(?P<answer>[0-9]+)$', views.acceptOrReject, name='answer'),
    url(r'^dismiss/(?P<team_id>[0-9]+)$', views.dismiss, name='dismiss')
]
