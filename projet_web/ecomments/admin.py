from django.contrib import admin
from ecomments.models import Ecomment#, Response

class EcommentAdmin(admin.ModelAdmin):
	list_display=('member_commenting','event_commenting_on', 'core_of_comment')
	#inline=[Response]

#class Response(admin.TabularInline):
#	model=Response
# Register your models here.
admin.site.register(Ecomment, EcommentAdmin)
