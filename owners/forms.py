from django import forms

from accounts.models import CustomUser
from owners.models import OwnerProfile


class OwnerProfileForm(forms.ModelForm):

    class Meta:
        model = OwnerProfile
        fields = ['company','website','region','street','profile_pic',]