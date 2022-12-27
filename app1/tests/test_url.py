from django.test import SimpleTestCase
from django.urls import resolve, reverse
from app1.views import index

class TestUrls(SimpleTestCase):

    def test_app1_index_is_resolved(self):
        url = reverse('index')
        self.assertEquals(resolve(url).func,index)