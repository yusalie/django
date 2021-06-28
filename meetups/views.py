from django.shortcuts import render
from .models import Meetup

# Create your views here.
def index(request):
    # try:
    meetups = Meetup.objects.all()
    return render(request, 'meetups/index.html',  {
        'meetups': meetups
    })
    # except Exception as e:
    #     print(e)

def meetup_details(request, meetup_slug):
    try:
        selected_meetups = Meetup.objects.get(slug=meetup_slug)
        return render(request, 'meetups/meetup-details.html', {
            'meetup_found':True,
            'meetup_title':selected_meetups.title,
            'meetup_description': selected_meetups.description
        })
    except Exception as e:
        return render(request, 'meetups/meetup-details.html', {
            'meetup_found':False
        })