from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    is_barbeiro = models.BooleanField(default=False)
    is_cliente = models.BooleanField(default=False)
    phone = models.CharField(max_length=20, blank=True, null=True)

    def __str__(self):
        return self.username
