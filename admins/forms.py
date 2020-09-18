from django import forms
from django.contrib.auth import get_user_model

from .models import AdminProfile

User = get_user_model()


class AdminProfileForm(forms.ModelForm):
    class Meta:
        model = AdminProfile
        fields = ['company', 'website', 'region', 'street',
                  'profile_pic',]
