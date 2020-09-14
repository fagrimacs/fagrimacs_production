from django import forms

from accounts.models import CustomUser
from .models import ExpertProfile


class ExpertProfileForm(forms.ModelForm):

    class Meta:
        model = ExpertProfile
        fields = ['company','website','region','street','profile_pic',]