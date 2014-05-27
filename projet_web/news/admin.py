from django.contrib import admin
from news.models import New, Image, Video

class InlineImage(admin.TabularInline):
	model = Image

class InlineVideo(admin.TabularInline):
	model = Video

class NewAdmin(admin.ModelAdmin):
	list_display = ('title', 'publication_date')
	inlines=[InlineImage, InlineVideo]

admin.site.register(New,NewAdmin)