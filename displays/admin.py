from django.contrib import admin

from .models import Location, EventType, Event

# Register your models here.

#admin.site.register(Event)
admin.site.register(Location)
admin.site.register(EventType)

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    date_hierarchy = 'dayTime'
    list_display = ('name', 'dayTime', 'location')
    search_fields = ['name']