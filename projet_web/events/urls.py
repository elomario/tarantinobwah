from django.conf.urls import patterns, url

from events import views

urlpatterns = patterns('',
    # ex: /events/
	url(r'^$', views.index, name='index'),
	# ex: /events/myevents/
    url(r'^(?P<events_id>\d+)/$', views.detail, name='detail'),
    # ex: /projects/myproject/results/
    url(r'^(?P<events_title>\d+)/results/$', views.results, name='results'),
)
