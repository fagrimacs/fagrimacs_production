from uuid import uuid4

from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse

User = get_user_model()


def profile_pic_filename(instance, filename):
    ext = filename.split('.')[1]
    new_filename = f'{uuid4()}.{ext}'
    return f'profile_pics/{new_filename}'


class OwnerProfile(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, primary_key=True)
    profile_pic = models.ImageField(verbose_name='Profile Picture',
                                    default='profile_pics/user.png',
                                    upload_to=profile_pic_filename)
    company = models.CharField(
        max_length=200, verbose_name='Company Name', blank=True)
    website = models.URLField(blank=True, max_length=254)
    region = models.CharField(max_length=200)
    street = models.CharField(max_length=200)

    def __str__(self):
        return f'{self.user.name} Profile'

    def get_absolute_url(self):
        return reverse('owners:profile', kwargs={'pk': self.user_id})

    def get_profile_update_url(self):
        return reverse('owners:update-profile', kwargs={'pk': self.user_id})
