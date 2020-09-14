from django import forms

from accounts.models import CustomUser
from .models import AdminProfile


class AdminProfileForm(forms.ModelForm):

    class Meta:
        model = AdminProfile
        fields = ['company','website','region','street','profile_pic',]