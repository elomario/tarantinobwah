from django.contrib import admin
from members.models import Member
from members.models import Team

class MemberAdmin(admin.ModelAdmin):
	list_display=('user','department','phone_number')

class TeamAdmin(admin.ModelAdmin):
	list_display=('team_name','team_manager')

admin.site.register(Member,MemberAdmin)
admin.site.register(Team,TeamAdmin)