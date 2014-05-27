from django.shortcuts import render, get_object_or_404

from django.http import HttpResponse

from django.template import RequestContext, loader

from presentation.models import Presentation, Video, Image

# Create your views here.

def presentation(request):
	presentation = Presentation.objects.get(title='Presentation')
	video_list = Video.objects.filter(presentation=presentation)
	image_list = Image.objects.filter(presentation=presentation)
	template = loader.get_template('presentation/presentation.html')
	context = RequestContext(request, {
			'presentation': presentation,
			'video_list': video_list,
			'image_list': image_list,
			})
	return HttpResponse(template.render(context))

def shell(request):
	presentation = Presentation.objects.get(title='Shell eco-marathon')
	video_list = Video.objects.filter(presentation=presentation)
	image_list = Image.objects.filter(presentation=presentation)
	template = loader.get_template('presentation/shell.html')
	context = RequestContext(request, {
			'presentation': presentation,
			'video_list': video_list,
			'image_list': image_list,
			})
	return HttpResponse(template.render(context))