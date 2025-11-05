from django.contrib import admin
from .models import Service, Appointment

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ("name", "duration_minutes", "price", "active")

@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    list_display = ("service", "cliente", "barbeiro", "start", "end", "canceled")
    list_filter = ("canceled", "service")
    search_fields = ("cliente__username", "barbeiro__username")
