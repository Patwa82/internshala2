# settlements/tests.py

from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from .models import Settlement, PaymentStatus
from users.models import CustomUser
from expenses.models import Expense, Category

class SettlementTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = CustomUser.objects.create_user(username='testuser', password='password123')
        self.category = Category.objects.create(name='Food')
        self.expense = Expense.objects.create(amount=20.00, category=self.category, split_type='equal')
        self.payment_status = PaymentStatus.objects.create(name='Paid')
        self.settlement_data = {
            'expense': self.expense.id,
            'user': self.user.id,
            'status': self.payment_status.id,
            'due_date': '2025-01-01'
        }

    def test_create_settlement(self):
        response = self.client.post('/api/settlements/', self.settlement_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_get_settlements(self):
        Settlement.objects.create(expense=self.expense, user=self.user, status=self.payment_status, due_date='2025-01-01')
        response = self.client.get('/api/settlements/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
