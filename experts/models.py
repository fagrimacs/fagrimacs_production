from uuid import uuid4

from django.db import models
from django.urls import reverse

from accounts.models import CustomUser
from django.core.validators import URLValidator


def profile_pic_filename(instance, filename):
    ext = filename.split('.')[1]
    new_filename = f'{uuid4()}.{ext}'
    return f'profile_pics/{new_filename}'


class ExpertProfile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, primary_key=True)
    profile_pic = models.ImageField(verbose_name='Profile Picture', default='profile_pics/user.png', upload_to=profile_pic_filename)
    company = models.CharField(max_length=256, verbose_name='Company Name', blank=True)
    website = models.CharField(validators=[URLValidator()], blank=True, max_length=254)
    region = models.CharField(max_length=254)
    street = models.CharField(max_length=254)

    def __str__(self):
        return f'{self.user.name} Profile'

    def get_absolute_url(self):
        return reverse('experts:profile', kwargs={'pk': self.user_id})

    def get_profile_update_url(self):
        return reverse('experts:update-profile', kwargs={'pk': self.user_id})
