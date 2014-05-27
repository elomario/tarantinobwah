from django.contrib import admin
from presentation.models import Presentation, Image, Video

class InlineImage(admin.TabularInline):
	model = Image

class InlineVideo(admin.TabularInline):
	model = Video

class PresentationAdmin(admin.ModelAdmin):
	list_display = ('title', 'text')
	inlines=[InlineImage, InlineVideo]

# Register your models here.
admin.site.register(Presentation,PresentationAdmin)