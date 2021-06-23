from django.urls import path
from . import views

urlpatterns = [
    path('meetups/', views.index, name='all-meetups'), #our-domain/meetups/
    path('meetups/<slug:meetup_slug>', views.meetup_details, name='meetup-detail'), #our-domain/meetups/<dynamic-path-segment>
]
