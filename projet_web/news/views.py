from django.shortcuts import render, get_object_or_404

from django.http import HttpResponse

from django.template import RequestContext, loader

from news.models import New, Video, Image

# Create your views here.

def index(request):
	latest_news_list = New.objects.order_by('-publication_date')[:3]
	video_list = Video.objects.all()
	image_list = Image.objects.all()
	template = loader.get_template('news/index.html')
	context = RequestContext(request, {
			'latest_news_list': latest_news_list,
			'video_list': video_list,
			'image_list': image_list,
			})
	return HttpResponse(template.render(context))
