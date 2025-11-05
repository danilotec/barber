from django.db import models
from django.conf import settings

class Service(models.Model):
    name = models.CharField(max_length=100)
    duration_minutes = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.name} ({self.duration_minutes}m)"

class Appointment(models.Model):
    cliente = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="appointments")
    barbeiro = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True, related_name="appointments_as_barbeiro")
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    start = models.DateTimeField()
    end = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    canceled = models.BooleanField(default=False)

    class Meta:
        ordering = ["-start"]
        unique_together = ("barbeiro", "start")  

    def __str__(self):
        return f"{self.service} para {self.cliente} em {self.start}"
