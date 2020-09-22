from django.test import TestCase

from accounts.factories import UserFactory
from equipments import factories


class TestEquipmentsModels(TestCase):

    def test_tractor_model_can_save(self):
        """Test if the Tractor model is saved and associate user when saved."""
        user = UserFactory()
        tractor = factories.TractorFactory(user=user, agree_terms=True)

        self.assertEqual(user.tractor_set.count(), 1)

    def test_users_can_add_tractors(self):
        """Test if different users can add tractors."""
        user1 = UserFactory()
        user2 = UserFactory()
        tractor1 = factories.TractorFactory(user=user1, agree_terms=True)
        tractor2 = factories.TractorFactory(user=user2, agree_terms=True)

        self.assertEqual(tractor1.user, user1)
        self.assertEqual(tractor2.user, user2)

    def test_implement_model_can_save(self):
        """Test if Implement model is saved and associate user when saved."""
        user = UserFactory()
        implement = factories.ImplementFactory(user=user,
                                               operator=True,
                                               agree_terms=True)

        self.assertEqual(user.implement_set.count(), 1)
