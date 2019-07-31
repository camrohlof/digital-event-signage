from django.shortcuts import render
from django.views import generic
from .models import Event

# Create your views here.
class IndexView(generic.ListView):
    template_name = 'displays/index.html'
    context_object_name = 'current_events'
    
    def get_queryset(self):
        return Event.objects.order_by('time')
