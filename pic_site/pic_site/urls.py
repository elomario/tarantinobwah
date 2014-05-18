from django.conf.urls import patterns, include, url

from django.contrib import admin
from pic_site import views
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'pic_site.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
	url(r'^home/', 'pic_site.views.home', name='home'),
	url(r'^presentation/', views.presentation, name='presentation'),
	url(r'^actualites/', views.actualites, name='actualites'),
	url(r'^shell/', views.shell, name='shell'),
	
	url(r'^projects/', include('projects.urls')),
	url(r'^events/', include('events.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
