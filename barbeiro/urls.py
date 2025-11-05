from django.urls import path
from . import views

app_name = "barbeiro"

urlpatterns = [
    path("", views.agenda, name="agenda"),
]
