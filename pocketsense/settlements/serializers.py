# settlements/serializers.py

from rest_framework import serializers
from .models import Settlement, PaymentStatus
from expenses.models import Expense
from users.models import CustomUser

class SettlementSerializer(serializers.ModelSerializer):
    expense = serializers.PrimaryKeyRelatedField(queryset=Expense.objects.all())
    user = serializers.PrimaryKeyRelatedField(queryset=CustomUser.objects.all())
    status = serializers.PrimaryKeyRelatedField(queryset=PaymentStatus.objects.all())

    class Meta:
        model = Settlement
        fields = ['id', 'expense', 'user', 'status', 'due_date']


class PaymentStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = PaymentStatus
        fields = ['id', 'name']
