from django.shortcuts import render, redirect
from Events.models import Event
from Registrations.forms import RegistrationForm


def index(request):
    return render(request, 'index.html')

def get_template(request, template_name):
    events = Event.objects.all()
    context = {
        'events': events,
        'form': RegistrationForm()
    }
    return render(request, template_name, context)

def register_event(request, event_id):
    event = Event.objects.get(id=event_id)
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.instance.event = event
            form.save()
            return redirect('events.html')
    else:
        form = RegistrationForm()
    context = {
        'event': event,
        'form': form
    }
    return redirect('events.html')
