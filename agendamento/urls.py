from django.urls import path
from . import views

app_name = "agendamento"
urlpatterns = [
    path("servicos/", views.services_list, name="services_list"),
    path("novo/", views.create_appointment, name="create_appointment"),
    path("<int:pk>/", views.appointment_detail, name="appointment_detail"),
]
