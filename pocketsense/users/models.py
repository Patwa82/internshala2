# users/models.py

from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    college = models.CharField(max_length=255)
    semester = models.IntegerField()
    default_payment_method = models.CharField(max_length=255, blank=True)

    # Update the related_name to avoid clashes
    groups = models.ManyToManyField(
        'auth.Group', 
        related_name='customuser_groups',  # Unique reverse relationship name
        blank=True,
    )
    
    user_permissions = models.ManyToManyField(
        'auth.Permission', 
        related_name='customuser_permissions',  # Unique reverse relationship name
        blank=True,
    )

    def __str__(self):
        return self.username
