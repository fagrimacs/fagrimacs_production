from django import forms

from farmers.models import FarmerProfile


class FarmerProfileForm(forms.ModelForm):

    class Meta:
        model = FarmerProfile
        fields = ['company', 'website', 'region', 'street', 'profile_pic', ]
