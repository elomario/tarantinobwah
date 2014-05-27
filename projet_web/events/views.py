from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.template import RequestContext, loader
from events.models import Event, Member
from django.contrib.auth.models import User
# Create your views here.

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
	event = get_object_or_404(Event, pk=events_id)
	return render(request, 'events/description.html', {'event': event})
	
def results(request, projects_title):
    return HttpResponse("You're looking at the results of event %s." % projects_title)



# Create your views here.
