from django.db import models

# Create your models here.
class MainDisplayManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(eventType='normal')

class Location(models.Model):
    party_area = models.CharField(max_length=20)

    def __str__(self):
       return self.party_area 

class EventType(models.Model):
    type_of_event = models.CharField(max_length=20)

    def __str__(self):
        return self.type_of_event

class Event(models.Model):
    name = models.CharField(max_length=25)
    dayTime = models.DateTimeField()
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    eventType = models.ForeignKey(EventType, on_delete=models.CASCADE)

    def __str__(self):
        return self.name




