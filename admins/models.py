from uuid import uuid4

from django.db import models
from django.urls import reverse

from accounts.models import CustomUser


def profile_pic_filename(instance, filename):
    ext = filename.split('.')[1]
    new_filename = f'{uuid4()}.{ext}'
    return f'profile_pics/{new_filename}'


class AdminProfile(models.Model):
    user = models.OneToOneField(
        CustomUser, on_delete=models.CASCADE, primary_key=True)
    profile_pic = models.ImageField(verbose_name='Profile Picture',
                                    default='profile_pics/user.png',
                                    upload_to=profile_pic_filename)
    company = models.CharField(
        max_length=200, verbose_name='Company Name', blank=True)
    website = models.URLField(blank=True, max_length=200)
    region = models.CharField(max_length=200)
    street = models.CharField(max_length=200)

    def __str__(self):
        return f'{self.user.name} Profile'

    def get_absolute_url(self):
        return reverse('admins:profile', kwargs={'pk': self.user_id})

    def get_profile_update_url(self):
        return reverse('admins:update-profile', kwargs={'pk': self.user_id})
