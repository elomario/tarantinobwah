from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader
from projects.models import Project
# Create your views here.

def index(request):
    latest_projects_list = Project.objects.order_by('-title')[:5]
    template = loader.get_template('projects/index.html')
    context = RequestContext(request, {
        'latest_projects_list': latest_projects_list,
    })
    return HttpResponse(template.render(context))

def detail(request, projects_title):
    latest_projects_list = Project.objects.order_by('-title')[:5]
    output = ', '.join([p.title for p in latest_projects_list])
    return HttpResponse(output)
	
def results(request, projects_title):
    return HttpResponse("You're looking at the results of project %s." % projects_title)


