from django.test import TestCase, Client
from django.urls import reverse
from accounts.models import *
from django.contrib.auth.models import User
import json

class BaseTest(TestCase):
    def setUp(self):
        self.register_url = reverse('register')
        self.login_url = reverse('login')
        self.user = {
            'username': 'username',
            'email': 'test@gmail.com',
            'password': 'password',
            'password2': 'password',
        }
        return super().setUp()

class TestRegister(BaseTest):
    def test_can_view_register_page(self):
        response = self.client.get(self.register_url)
        self.assertEqual(response.status_code, 200)# test1: check if the url of register page is visible 
        self.assertTemplateUsed(response,'accounts/register.html')# test2: check if correct templlate is used
        print("running1")


    #test to se if the user can register themselves or not
    def test_user_can_register(self):
        response = self.client.post(self.register_url,self.user,format='text/html')
        self.assertEqual(response.status_code, 200)
        print("running2")

    '''
        Test cases covered in frontend 
        4. user creation with invalid email address
        5. user creation with unmatching passwords
        6. user creation with short passwords
        7. link to login page if the user is already registered
    '''

    '''
        Remaining TestCase
        1. user cant register with same email
    '''

    '''
        Code Refactoring
        register page available to both admin and users
    '''

class LoginTest(BaseTest):
    def test_user_can_view_login(self):
        response = self.client.get(self.login_url)
        self.assertEqual(response.status_code,200)#test1 check if the url of login page is visible and returns
        self.assertTemplateUsed(response,'accounts/login.html')#test2 check if login page is visible
        print('running3')

    def test_login_success(self):#test3 check if login is a success
        self.client.post(self.register_url,self.user,format='text/html')
        user=User.objects.filter(email=self.user['email']).first()
        user.is_active=True
        user.save()
        response= self.client.post(self.login_url,self.user,format='text/html')
        self.assertEqual(response.status_code,302)
        print('running4')


    def test_cantlogin_with_unverified_email(self):#test4 user logging in with an unverified email
        self.client.post(self.register_url,self.user,format='text/html')
        response= self.client.post(self.login_url,self.user,format='text/html')
        self.assertEqual(response.status_code,200)
        print('running5')