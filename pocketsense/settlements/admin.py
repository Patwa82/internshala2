# settlements/admin.py

from django.contrib import admin
from .models import Settlement, PaymentStatus

admin.site.register(Settlement)
admin.site.register(PaymentStatus)
