from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=25)
    phone_number = models.CharField(max_length=12)
    card_number = models.CharField(max_length=16, null=True)

    def __str__(self):
        return self.name