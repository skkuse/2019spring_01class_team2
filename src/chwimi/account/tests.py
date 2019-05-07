from django.http import HttpRequest
from django.test import Client, TestCase
from django.urls import resolve

from django.contrib.auth.models import User
from account.views import login, signup

'''
Test용 
ID: helloworld
PW: 1234k5678
Email: helloworld@gmail.com
Gender: M
Phone: 01012341234
'''

class SignupTest(TestCase):
    def test_signup_page(self):
        cli = self.client
        response = cli.get('/account/signup/')
        self.assertTemplateUsed(response, 'signup.html')
    
    def test_signup_with_userid_and_password(self):
        cli = self.client
        response = cli.post('/account/signup/', data={
            'input_userid':'helloworld',
            'input_userpw':'1234k5678',
            'input_userpw_check':'1234k5678'
        })

        user = User.objects.get(username = 'helloworld')
        self.assertTrue(user)
        
class LoginTest(TestCase):
    def test_login_page(self):
        cli = self.client
        response = cli.get('/account/login/')
        self.assertTemplateUsed(response, 'login.html')
