from django.contrib import admin
from events.models import Event

class EventAdmin(admin.ModelAdmin):
	list_display=('name','date')
	
# Register your models here.
admin.site.register(Event, EventAdmin)
