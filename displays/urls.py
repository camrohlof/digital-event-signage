from django.urls import path

from . import views

urlpatterns = [
    path('', views.HomeView.as_view(), name="index"),
    path('events.html', views.EventView.as_view(), name='events'),
]