from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.template import RequestContext, loader
from news.models import New, Video, Image
# Create your views here.

def home(request):
	latest_news_list = New.objects.order_by('-publication_date')[:3]
	video_list = Video.objects.all()
	image_list = Image.objects.all()
	template = loader.get_template('pic_site/home.html')
	context = RequestContext(request, {
			'latest_news_list': latest_news_list,
			'video_list': video_list,
			'image_list': image_list,
			})
	return render(request,'pic_site/home.html', context)
def presentation(request):
	return render(request,'pic_site/presentation.html')
def actualites(request):
	return render(request,'pic_site/actualites.html')
def shell(request):
	return render(request,'pic_site/shell.html')