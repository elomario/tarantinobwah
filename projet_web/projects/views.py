from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext, loader
from django.contrib.auth.models import User
from projects.models import Project, Member
from comments.models import Comment

# Create your views here.

def index(request):
    latest_projects_list = Project.objects.order_by('-title')
    template = loader.get_template('projects/index.html')
    context = RequestContext(request, {
        'latest_projects_list': latest_projects_list,
    })
    return HttpResponse(template.render(context))

def detail(request, projects_id):
	if request.method == 'POST':
		if 'participate' in request.POST:
			id=request.POST['user']
			user = User.objects.get(id=id)
			member = Member.objects.get(user=user)
			project = get_object_or_404(Project, pk=projects_id)
			project.members.add(member)
		
		elif 'abandon' in request.POST:
			a_id=request.POST['a_user']
			a_user = User.objects.get(id=a_id)
			a_member = Member.objects.get(user=a_user)
			a_project = get_object_or_404(Project, pk=projects_id)
			a_project.members.remove(a_member)
	project = get_object_or_404(Project, pk=projects_id)
	#comment_list=Comment.objects.all()
	
	template = loader.get_template('projects/description.html')
	context = RequestContext(request, {
        'project': project,
	#	'comment_list': comment_list,
	})
	return HttpResponse(template.render(context))

#def participe(request, projects_id):
	#requests.post

def results(request, projects_title):
    return HttpResponse("You're looking at the results of project %s." % projects_title)


