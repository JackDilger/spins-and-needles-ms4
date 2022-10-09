from django.test import TestCase


class TestViews(TestCase):
    """ Test correct home template renders """
    def test_get_index(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home/index.html')
