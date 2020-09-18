from django.db.models.signals import pre_save
from django.dispatch import receiver

from .models import UserProfile


@receiver(pre_save, sender=UserProfile)
def delete_prev_profile_pic(sender, instance, **kwargs):
    if instance.pk:
        try:
            prev_profile = UserProfile.objects.get(
                pk=instance.pk).profile_pic
        except UserProfile.DoesNotExist:
            return
        else:
            new_profile = instance.profile_pic
            if prev_profile and prev_profile.url != new_profile.url:
                if prev_profile != 'profile_pics/user.png':
                    prev_profile.delete(save=False)
