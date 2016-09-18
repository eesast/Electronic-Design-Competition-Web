from django.conf.urls import url
from . import views

app_name = 'community'

urlpatterns = [
    url(r'^community_create$',views.community_create,name='community_create'),
    url(r'^community_index$',views.community_index,name='community_index'),
    url(r'^community_index?page=([0-9]+)$',views.community_index,name='community_index'),
    url(r'^community_content_after_login/(?P<id>[0-9]+)',views.community_content),
    url(r'^community_content_after_login/delpost/(?P<id>[0-9]+)',views.delpost),
    url(r'^community_content_after_login/delcomment(?P<id>[0-9]+)',views.community_content),
]
# Create your views here.
