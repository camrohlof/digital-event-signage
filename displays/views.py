from django.shortcuts import render
from django.views import generic
from .models import Event
from datetime import *

# Create your views here.

class HomeView(generic.ListView):
    template_name = 'displays/index.html'
    context_object_name = 'current_events'
    
    def get_queryset(self):
        timeBefore = datetime.now() + timedelta(hours=-2)
        timeAfter = datetime.now() + timedelta(hours=2)
        queryset = Event.objects.all()
        queryset = queryset.filter(day=date.today())
        queryset = queryset.order_by("time")
        queryset = queryset.filter(time__range=(timeBefore, timeAfter))[:5]
        return queryset

class EventView(generic.ListView):
    template_name = 'displays/events.html'
    context_object_name = "current_events"

    def get_queryset(self):
        timeBefore = datetime.now() + timedelta(hours=-2)
        timeAfter = datetime.now() + timedelta(hours=2)
        queryset = Event.objects.all()
        queryset = queryset.filter(day=date.today())
        queryset = queryset.order_by("time")
        queryset = queryset.filter(time__range=(timeBefore, timeAfter))[:5]
        return queryset