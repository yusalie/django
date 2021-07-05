from django.shortcuts import render, redirect
from .models import Meetup, Participant
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
               user_email = registration_form.cleaned_data['email']
               participant, was_created= Participant.objects.get_or_create(email=user_email)
               selected_meetups.participant.add(participant)
               return redirect('confirm-registration', meetup_slug=meetup_slug)

    except Exception as e:
        return render(request, 'meetups/meetup-details.html', {
            'meetup_found':False
        })

def confirm_registration(request, meetup_slug):
    meetup = Meetup.objects.get(slug=meetup_slug)
    return render(request, 'registration-success.html',{
        'organizer_email':meetup.organizer_email
    })