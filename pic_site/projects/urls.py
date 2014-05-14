from django.conf.urls import patterns, url

from projects import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
	# ex: /projects/myproject/
    url(r'^(?P<projects_title>\d+)/$', views.detail, name='detail'),
    # ex: /projects/myproject/results/
    url(r'^(?P<projects_title>\d+)/results/$', views.results, name='results'),
)
