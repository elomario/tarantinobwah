from django.conf.urls import patterns, url
from events import views

urlpatterns = patterns('',
	url(r'^$', views.index, name='index'),
    url(r'^(?P<events_id>\d+)/$', views.detail, name='detail'), 
    url(r'^(?P<events_title>\d+)/results/$', views.results, name='results'),
)