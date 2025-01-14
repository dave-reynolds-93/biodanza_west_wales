from django.shortcuts import render, get_object_or_404
from .models import Event
import datetime


# Create your views here.

def all_events(request):
    """ A view to show all events, including sorting """

    events = Event.objects.all()
    location = None
    # date = None
    teacher = None

    if request.GET:
        if 'location' in request.GET:
            location = request.GET['location']
            events = Event.objects.filter(location=location)

        if 'teacher' in request.GET:
            teacher = request.GET['teacher']
            events = Event.objects.filter(teacher=teacher)

        # if 'date' in request.GET:
        #     date = request.GET['date']
        #     events = Event.objects.filter(date<datetime.date.today())

    context = {
        'events': events,
    }

    return render(request, 'events/events.html', context)


def event_detail(request, event_id):
    """ A view to show individual product details """

    event = get_object_or_404(Event, pk=event_id)

    context = {
        'event': event,
    }

    return render(request, 'events/event_detail.html', context)