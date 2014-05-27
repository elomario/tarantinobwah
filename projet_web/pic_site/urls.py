from django.conf.urls import patterns, include, url

from django.contrib import admin
from pic_site import views
from presentation import views
admin.autodiscover()

urlpatterns = patterns('',
	url(r'^home/', 'pic_site.views.home', name='home'),	

	url(r'^actualites/', include('news.urls')),
	url(r'', include('presentation.urls')),
	url(r'^members/', include('members.urls')),
	url(r'^projects/', include('projects.urls')),
	url(r'^events/', include('events.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
