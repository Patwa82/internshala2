# expenses/views.py

from rest_framework import generics
from .models import Expense, Category
from .serializers import ExpenseSerializer, CategorySerializer

class ExpenseListCreateView(generics.ListCreateAPIView):
    queryset = Expense.objects.all()
    serializer_class = ExpenseSerializer

class CategoryListView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
