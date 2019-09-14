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
        queryset = queryset.filter(dayTime=date.today())
        queryset = queryset.order_by("dayTime")
        queryset = queryset.filter(dayTime__range=(timeBefore, timeAfter))[:6]
        return queryset

class EventView(generic.ListView):
    template_name = 'displays/events.html'
    context_object_name = "current_events"

    def get_queryset(self):
        timeBefore = datetime.now() + timedelta(hours=-1)
        timeAfter = datetime.now() + timedelta(hours=2)
        queryset = Event.objects.all()
        queryset = queryset.order_by("dayTime")
        queryset = queryset.filter(dayTime__range=(timeBefore, timeAfter))[:6]
        return queryset