from django.test import TestCase
from django.urls import reverse

# Index page
    # test that index page returns a 200
class IndexPageTestCase(TestCase):

    # test that index page returns a 200
    def test_index_page(self):
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)

    # test that index page use index.
    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'story/index.html')
