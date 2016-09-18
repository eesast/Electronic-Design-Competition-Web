from django.conf.urls import url
from . import views

app_name = 'community'

urlpatterns = [
    url(r'^community_create$',views.community_create,name='community_create'),
    url(r'^community_index$',views.community_index,name='community_index'),
    url(r'^community_index?page=([0-9]+)$',views.community_index,name='community_index'),
    url(r'^community_index_tongzhi$',views.community_index_tongzhi,name='community_index_tongzhi'),
    url(r'^community_index_tongzhi?page=([0-9]+)$',views.community_index_tongzhi,name='community_index_tongzhi'),
    url(r'^community_index_jishu$',views.community_index_jishu,name='community_index_jishu'),
    url(r'^community_index_jishu?page=([0-9]+)$',views.community_index_jishu,name='community_index_jishu'),
    url(r'^community_index_shuitie$',views.community_index_shuitie,name='community_index_shuitie'),
    url(r'^community_index_shuitie?page=([0-9]+)$',views.community_index_shuitie,name='community_index_shuitie'),
    url(r'^community_index_mypost$',views.community_index_mypost,name='community_index_mypost'),
    url(r'^community_index_mypost?page=([0-9]+)$',views.community_index_mypost,name='community_index_mypost'),
    url(r'^community_content/(?P<id>[0-9]+)',views.community_content),
]
# Create your views here.
