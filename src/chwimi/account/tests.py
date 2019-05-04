from django.test import TestCase
from django.urls import resolve
from account.views import signup

class SignupTest(TestCase):
    def test_signup_url_resolves_to_signup_page_view(self):
        found = resolve('/account/signup/')
        self.assertEqual(found.func, signup)
        
