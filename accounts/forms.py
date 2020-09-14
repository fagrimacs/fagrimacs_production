from django import forms
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.db import transaction

from .models import CustomUser

ROLE_CHOICES = [
        ('', 'Please select'),
        ('farmer', 'Farmer'),
        ('owner', 'Equipment Owner'),
        ('expert', 'Expert'),
    ]

class UserCreationForm(forms.ModelForm):
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)
    role = forms.ChoiceField(
        widget=forms.Select,
        choices=ROLE_CHOICES,
        label='What is your primary role in platform?'
    )

    class Meta:
        model = CustomUser
        fields = ('name', 'email', 'phone', 'role', 'hear_about_us', )
        

    def clean_password2(self):
        # Check that the two password entries match
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        if len(password1) < 8:
            raise forms.ValidationError('Password too short, It must be 8 character or more')
        return password2

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user


class UserChangeForm(forms.ModelForm):

    password = ReadOnlyPasswordHashField()

    class Meta:
        model = CustomUser
        fields = ('email', 'password', 'name', 'is_active',)

    def clean_password(self):
        # Regardless of what the user provides, return the initial value.
        # This is done here, rather than on the field, because the
        # field does not have access to the initial value
        return self.initial["password"]


class SignUpForm(UserCreationForm):

    class Meta(UserCreationForm.Meta):
        model = CustomUser


class UserUpdateForm(forms.ModelForm):

    class Meta:
        model = CustomUser
        fields = ['name', 'email', 'phone', ]
