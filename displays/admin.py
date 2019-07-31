from django.contrib import admin

from .models import Location, EventType, Event

# Register your models here.

admin.site.register(Event)
admin.site.register(Location)
admin.site.register(EventType)