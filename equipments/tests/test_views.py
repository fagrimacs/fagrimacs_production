from django.test import TestCase
from django.urls import reverse

from equipments import models, factories


class TestEquipmentsViews(TestCase):

    def test_tractor_list_view_works(self):
        """Test if the view show approved tractors only and
        owners have accepted terms and conditions.
        """
        factories.TractorFactory.create_batch(
            3, agree_terms=True, approved=True)
        factories.TractorFactory.create_batch(
            2, agree_terms=True, approved=False)
        factories.TractorFactory.create_batch(
            4, agree_terms=False, approved=True)

        tractors = models.Tractor.objects.filter(agree_terms=True,
                                                 approved=True)

        response = self.client.get(reverse('equipments:tractors-list'))

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['object_list'], tractors)
