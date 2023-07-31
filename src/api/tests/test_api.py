from django.conf import settings
from django.test import TestCase
from django.urls import reverse


class TestAPI(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.url = reverse('api:index')

    def test_index_route(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, settings.API_NAME)
