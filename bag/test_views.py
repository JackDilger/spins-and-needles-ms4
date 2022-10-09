from django.test import TestCase


class TestViews(TestCase):
    """ Test correct bag template renders """
    def test_get_view_bag(self):
        response = self.client.get('/bag/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'bag/bag.html')
