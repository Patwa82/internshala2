# expenses/serializers.py

from rest_framework import serializers
from .models import Expense, Category
from users.models import CustomUser

class ExpenseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Expense
        fields = ['id', 'amount', 'category', 'split_type', 'date', 'receipt_image', 'users']

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']
