from django.conf.urls import patterns, url

from members import views

urlpatterns = patterns('',	
    url(r'^home', views.home, name='home'),
	url(r'^presentation/', views.presentation, name='presentation'),
	url(r'^shell/', views.shell, name='shell'),
	url(r'^$', views.member_login, name='login'),
	url(r'^logout/$', views.member_logout, name='logout'),
)
