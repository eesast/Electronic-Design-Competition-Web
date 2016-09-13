from django.conf.urls import url, include
from . import views
import contact
app_name = 'index'

urlpatterns = [
    url(r'^$', views.welcome, name='welcome'),
    url(r'^index$', views.index, name='index'),
    url(r'^notice$', views.noticeIndex, name='notice'),
    url(r'^download/(?P<notice_id>[0-9]+)', views.download, name='download'),
]
