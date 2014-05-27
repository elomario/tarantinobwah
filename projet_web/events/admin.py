from django.contrib import admin
from events.models import Event

class EventAdmin(admin.ModelAdmin):
	list_display=('name','date')
	
admin.site.register(Event, EventAdmin)