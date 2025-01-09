# settlements/views.py

from rest_framework import generics
from .models import Settlement, PaymentStatus
from .serializers import SettlementSerializer, PaymentStatusSerializer
from rest_framework.permissions import IsAuthenticated

class SettlementListCreateView(generics.ListCreateAPIView):
    queryset = Settlement.objects.all()
    serializer_class = SettlementSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class PaymentStatusListView(generics.ListAPIView):
    queryset = PaymentStatus.objects.all()
    serializer_class = PaymentStatusSerializer
    permission_classes = [IsAuthenticated]
