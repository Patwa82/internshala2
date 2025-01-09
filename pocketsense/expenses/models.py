# expenses/models.py

from django.db import models
from users.models import CustomUser  # Assuming you have CustomUser model

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Expense(models.Model):
    AMOUNT_CHOICES = (
        ('equal', 'Equal'),
        ('custom', 'Custom'),
    )

    amount = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    split_type = models.CharField(max_length=10, choices=AMOUNT_CHOICES)
    date = models.DateTimeField(auto_now_add=True)
    receipt_image = models.ImageField(upload_to='receipts/', null=True, blank=True)
    users = models.ManyToManyField(CustomUser)

    def __str__(self):
        return f'{self.category} - {self.amount}'
