from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.template import RequestContext, loader
from projects.models import Project

# Create your views here.

def home(request):
	return render(request,'pic_site/home.html')
def presentation(request):
	return render(request,'pic_site/presentation.html')
def actualites(request):
	return render(request,'pic_site/actualites.html')
def shell(request):
	return render(request,'pic_site/shell.html')