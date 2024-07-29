from .models import User
from rest_framework.test import APITestCase
from rest_framework import status
from rest_framework_simplejwt.tokens import AccessToken
import time


class AuthenticationTests(APITestCase):
    def setUp(self):
        self.registration_url = '/auth/register'
        self.login_url = '/auth/login'

    def test_user_registration(self):
        response = self.client.post(self.registration_url, {
            'email': 'newuser@example.com',
            'password': 'newpassword',
            'firstName': 'New',
            'lastName': 'User',
            'phone': '1234567890'
        })
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertIn('accessToken', response.data['data'])
        self.assertEqual(response.data['data']['user']['email'], 'newuser@example.com')

        # Verify the creation of the associated organisation
        user = User.objects.get(email='newuser@example.com')
        self.assertTrue(user.organisations.exists())
        org = user.organisations.first()
        self.assertEqual(org.name, "New's Organisation")

    def test_user_login(self):
        User.objects.create_user(
            email='loginuser@example.com',
            password='loginpassword',
            firstName='Login',
            lastName='User'
        )
        response = self.client.post(self.login_url, {
            'email': 'loginuser@example.com',
            'password': 'loginpassword'
        })
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('accessToken', response.data['data'])
        self.assertEqual(response.data['data']['user']['email'], 'loginuser@example.com')

    def test_token_expiration(self):
        user = User.objects.create_user(
            email='tokenuser@example.com',
            password='tokenpassword',
            firstName='Token',
            lastName='User'
        )
        response = self.client.post(self.login_url, {
            'email': 'tokenuser@example.com',
            'password': 'tokenpassword'
        })
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        access_token = response.data['data']['accessToken']

        # Convert the token string to an AccessToken object
        access_token_obj = AccessToken(access_token)

        # Verify token expiration
        self.assertGreater(access_token_obj['exp'], time.time())
