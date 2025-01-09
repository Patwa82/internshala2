# settlements/urls.py

from django.urls import path
from .views import SettlementListCreateView, PaymentStatusListView

urlpatterns = [
    path('settlements/', SettlementListCreateView.as_view(), name='settlement-list-create'),
    path('payment-status/', PaymentStatusListView.as_view(), name='payment-status-list'),
]
