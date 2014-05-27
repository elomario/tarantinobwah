from django.contrib import admin
from comments.models import Comment#, Response

class CommentAdmin(admin.ModelAdmin):
	list_display=('member_commenting','project_commenting_on','core_of_comment')
	
admin.site.register(Comment)