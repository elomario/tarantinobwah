from django.conf.urls import patterns, url

from news import views

urlpatterns = patterns('',
# ex: /news/
		url(r'^$', views.index, name='index'),
)
