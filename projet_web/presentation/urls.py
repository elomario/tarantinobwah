from django.conf.urls import patterns, url
from presentation import views

urlpatterns = patterns('',
		url(r'^presentation', views.presentation, name='presentation'),
		url(r'^shell', views.shell, name='shell'),)
