from django.test import TestCase, Client
from django.urls import reverse
from accounts.models import *
import json

class BaseTest(TestCase):
    def setUp(self):
        self.register_url = reverse('register')
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
        self.assertEqual(response.status_code, 200)# test1: check if the url page is visible 
        self.assertTemplateUsed(response,'accounts/register.html')# test2: check if correct templlate is used
        print("running1")


    #test to se if the user can register themselves or not
    def test_user_can_register(self):
        response = self.client.post(self.register_url,self.user,format='text/html')
        self.assertEqual(response.status_code, 200)
        print("running2")

    '''
        Other test cases covered in frontend 
        1. user creation with invalid email address
        2. user creation with unmatching passwords
        3. user creation with short passwords
        4. link to login page if the user is already registered
    '''