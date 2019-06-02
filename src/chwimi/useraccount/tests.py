from django.http import HttpRequest
from django.test import Client, TestCase
from django.urls import resolve
from django.contrib import auth
from django.contrib.auth.models import User
from .models import Profile
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
            'input_userpw_check':'1234k5678',
            'input_email':'helloworld@gmail.com'
        })
        user = User.objects.get(username = 'helloworld')
        profile = Profile.objects.get(user = user)
        
        self.assertTrue(user)
        
class LoginTest(TestCase):
    def setUp(self):
        # 회원가입을 기본값으로 제공
        cli = self.client
        response = cli.post('/account/signup/', data={
            'input_userid':'helloworld',
            'input_userpw':'1234k5678',
            'input_userpw_check':'1234k5678',
            'input_email':'helloworld@gmail.com'
        })
        
    def test_login_page(self):
        cli = self.client
        response = cli.get('/account/login/')
        self.assertTemplateUsed(response, 'login.html')
        
    def test_login_redirects_successfully(self):
        cli = self.client
        login_res = cli.post('/account/login/', data={
            'input_userid': 'helloworld',
            'input_userpw': '1234k5678'
        })
    
        self.assertEqual(login_res.status_code, 302)

    def test_login_with_existing_info(self):
        cli = self.client
        
        _login = cli.login(username='helloworld', password='1234k5678')
        login_wrong_id = cli.login(username='wrong', password='1234k5678')
        login_wrong_pw = cli.login(username='helloworld', password='wrong')
        
        self.assertTrue(_login) 
        self.assertTrue(not login_wrong_id)
        self.assertTrue(not login_wrong_pw)

