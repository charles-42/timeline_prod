from django.test import TestCase
from django.urls import reverse

# Create your tests here.

# Index page
    # test that index page returns a 200
class IndexPageTestCase(TestCase):
    def test_index_page(self):
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)

class FrisePageTestCase(TestCase):
    def test_index_page(self):
        response = self.client.get(reverse('frise'))
        self.assertEqual(response.status_code, 200)
