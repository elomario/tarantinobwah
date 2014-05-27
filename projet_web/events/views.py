from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.template import RequestContext, loader
from events.models import Event, Member
from django.contrib.auth.models import User
from ecomments.models import Ecomment

def index(request):
    latest_events_list = Event.objects.order_by('-name')[:5]
    template = loader.get_template('events/index.html')
    context = RequestContext(request, {
        'latest_events_list': latest_events_list,
    })
    return HttpResponse(template.render(context))

def detail(request, events_id):
	if request.method == 'POST':
		if 'participate' in request.POST:
			id=request.POST['user']
			user = User.objects.get(id=id)
			participant = Member.objects.get(user=user)
			event = get_object_or_404(Event, pk=events_id)
			event.participants.add(participant)
		
		elif 'abandon' in request.POST:
			a_id=request.POST['a_user']
			a_user = User.objects.get(id=a_id)
			a_participant = Member.objects.get(user=a_user)
			a_event = get_object_or_404(Event, pk=events_id)
			a_event.participants.remove(a_participant)
		elif 'submit' in request.POST:
			c_id=request.POST['c_user']
			c_user= User.objects.get(id=c_id)
			c_member = Member.objects.get(user=c_user)
			c_event = get_object_or_404(Event, pk=events_id)
			ecomment = Ecomment(member_commenting=c_member, event_commenting_on=c_event, core_of_comment=request.POST['comment'])
			ecomment.save()
		elif 'delete' in request.POST:
			d_id=request.POST['c_id']
			Ecomment.objects.get(pk=d_id).delete()
	
	event = get_object_or_404(Event, pk=events_id)
	ecomments_list=Ecomment.objects.all()
	
	template = loader.get_template('events/description.html')
	context = RequestContext(request, {
        'event': event,
		'ecomments_list': ecomments_list,
	})
	return HttpResponse(template.render(context))
	
def results(request, projects_title):
    return HttpResponse("You're looking at the results of event %s." % projects_title)