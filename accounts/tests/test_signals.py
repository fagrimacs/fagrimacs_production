from django.test import TestCase
from django.urls import reverse
from django.core.files.images import ImageFile

from accounts.factories import UserFactory
from accounts.models import UserProfile


class TestAccountsSignals(TestCase):

    def test_prev_profile_pic_deleted_when_new_uploaded(self):
        """
        Test if the previous profile picture is deleted when user
        uploads new profile picture.
        """
        user = UserFactory(is_active=True)
        profile = UserProfile.objects.create(user=user)

        self.assertEqual(profile.profile_pic.url,
                         '/media/profile_pics/user.png')

        # to-do
        # user updates his/her profile
        url = reverse('accounts:user-profile-update', kwargs={
            'slug': profile.slug,
        })

        # with open(,'rb') as f:
        #     profile.profile_pic = ImageFile(f, name='tempo.png')
        #     profile.update()

        #     self.client.login(user.email)
        #     response = self.client.post(url, {'profile_pic': ImageFile(f)})

        #     self.assertEqual(response.status_code, 302)
        #     self.assertRedirects(response, '')
