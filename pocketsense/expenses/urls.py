# expenses/urls.py

from django.urls import path
from .views import ExpenseListCreateView, CategoryListView

urlpatterns = [
    path('expenses/', ExpenseListCreateView.as_view(), name='expense-list-create'),
    path('categories/', CategoryListView.as_view(), name='category-list'),
]
