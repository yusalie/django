from django.shortcuts import render
from .models import Meetup
from .forms import RegistrationForm

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
        if request.method == 'GET':
            selected_meetups = Meetup.objects.get(slug=meetup_slug)
            registration_form = RegistrationForm
            return render(request, 'meetups/meetup-details.html', {
                'meetup_found':True,
                'meetup':selected_meetups,
                'forms': registration_form
        })
        else:
            registration_form = RegistrationForm(request.POST)
            if registration_form.is_valid():
               particpant = registration_form.save()
               selected_meetups.participant.add(particpant)

    except Exception as e:
        return render(request, 'meetups/meetup-details.html', {
            'meetup_found':False
        })

def confirm_registration(request):
    return render(request, 'registration-success.html')