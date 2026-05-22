from django.db import models
from django.contrib.auth.models import User

"""Contains the Profile model which links users to their
role (vendor or buyer) within the ecommerce system."""


class Profile(models.Model):

    ROLE_CHOICES = [
        ("vendor", "Vendor"),
        ("buyer", "Buyer"),
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=10, choices=ROLE_CHOICES)

    def __str__(self):
        return f"{self.user.username} - {self.role}"
