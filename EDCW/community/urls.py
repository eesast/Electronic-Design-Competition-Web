from django.conf.urls import url
from . import views

app_name = 'community'

urlpatterns = [
    url(r'^community_content$',views.community_content,name='community_content'),
    url(r'^community_create$',views.community_create,name='community_create'),
    url(r'^community_index$',views.community_index,name='community_index'),
	]
# Create your views here.
