# settlements/models.py

from django.db import models
from users.models import CustomUser  # Assuming you have CustomUser model
from expenses.models import Expense  # Assuming you have Expense model

class PaymentStatus(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Settlement(models.Model):
    expense = models.ForeignKey(Expense, on_delete=models.CASCADE)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    status = models.ForeignKey(PaymentStatus, on_delete=models.SET_NULL, null=True)
    due_date = models.DateField()

    def __str__(self):
        return f'Settlement for {self.expense} - {self.user}'
