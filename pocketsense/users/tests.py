# users/tests.py

from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from .models import CustomUser

class UserTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user_data = {
            'username': 'testuser',
            'password': 'password123',
            'college': 'ABC University',
            'semester': 3,
            'default_payment_method': 'UPI'
        }

    def test_register_user(self):
        response = self.client.post('/api/register/', self.user_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_login_user(self):
        self.client.post('/api/register/', self.user_data, format='json')  # Register user
        login_data = {'username': 'testuser', 'password': 'password123'}
        response = self.client.post('/api/login/', login_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('access_token', response.data)
        self.assertIn('refresh_token', response.data)
