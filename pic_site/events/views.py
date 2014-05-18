from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.template import RequestContext, loader
from events.models import Event

# Create your views here.

def index(request):
    latest_events_list = Event.objects.order_by('-name')[:5]
    template = loader.get_template('events/index.html')
    context = RequestContext(request, {
        'latest_events_list': latest_events_list,
    })
    return HttpResponse(template.render(context))

def detail(request, events_id):
	event = get_object_or_404(Event, pk=events_id)
	return render(request, 'events/description.html', {'event': event})
	
def results(request, projects_title):
    return HttpResponse("You're looking at the results of event %s." % projects_title)



# Create your views here.
