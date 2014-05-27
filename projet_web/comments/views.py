from django.shortcuts import render

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
		elif 'submit' in request.POST:
			c_id=request.POST['c_user']
			c_user= User.objects.get(id=c_id)
			c_member = Member.objects.get(user=c_user)
			project = get_object_or_404(Project, pk=projects_id)
comment = Comment(member_commenting=c_member, project_commenting_on=project, core_of_comment=request.POST["comment"])
			comment.save()
elif 'delete' in request.POST:
			d_id=request.POST['c_id']
			Comment.objects.get(pk=d_id).delete()
			
	project = get_object_or_404(Project, pk=projects_id)
	comments_list=Comment.objects.all()
	
	template = loader.get_template('projects/description.html')
	context = RequestContext(request, {
        'project': project,
		'comments_list': comments_list,
	})
	return HttpResponse(template.render(context))