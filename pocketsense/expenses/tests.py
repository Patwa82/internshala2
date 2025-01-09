# expenses/tests.py

from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from .models import Expense, Category
from users.models import CustomUser

class ExpenseTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = CustomUser.objects.create_user(username='testuser', password='password')
        self.category = Category.objects.create(name='Food')
        self.expense_data = {
            'amount': 20.00,
            'category': self.category.id,
            'split_type': 'equal',
            'users': [self.user.id]
        }

    def test_create_expense(self):
        response = self.client.post('/api/expenses/', self.expense_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_get_expenses(self):
        Expense.objects.create(amount=30.00, category=self.category, split_type='equal')
        response = self.client.get('/api/expenses/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
