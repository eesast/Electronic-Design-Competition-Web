from django.conf.urls import url
from . import views

app_name = 'teams'

urlpatterns = [
    url(r'^index$', views.index , name='index'),
    url(r'^create$', views.create, name='create'),
    url(r'^info/(?P<team_id>[0-9]+)$', views.info, name='info'),
    url(r'^application/(?P<team_id>[0-9]+)$', views.application, name='application'),
    url(r'^myteam$', views.my_team, name='my_team'),
    url(r'^answer$', views.acceptOrReject, name='acceptOrReject'),
    url(r'^dismiss$', views.dismiss, name='dismiss'),
    url(r'group$', views.group, name='group'),
    url(r'choose_first_time$', views.choose_first_time, name='choose_first_time')
]
