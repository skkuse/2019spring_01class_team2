from django.test import TestCase
from django.urls import resolve
from main.views import home

class HomePageTest(TestCase):
    def test_root_url_resolves_to_home_page_view(self):
        found = resolve('/') # 해당 루트와 일치하는 함수 호출
        self.assertEqual(found.func, home)