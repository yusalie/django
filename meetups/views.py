from django.shortcuts import render
from .models import Meetup

# Create your views here.
def index(request):
    meetups = Meetup.objects
    return render(request, 'meetups/index.html',{
        'show_meetups': True,
        'meetups': meetups
    })

def meetup_details(request, meetup_slug):
    print(meetup_slug)
    selected_meetups ={
            'title':'A first meetup', 
            'description':'this is the first meetup'
        }
    return render(request, 'meetups/meetup-details.html', {
        'meetup_title':selected_meetups['title'],
        'meetup_description': selected_meetups['description']
    })