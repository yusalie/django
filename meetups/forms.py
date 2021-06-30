from django import forms
from .models import Participant

class RegistrationForm(forms.ModelForm):
    class Meta:
        model = Participant
        field = ['email']