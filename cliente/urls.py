from django.urls import path
from . import views

app_name = "cliente"

urlpatterns = [
    path("", views.dashboard, name="dashboard"),
    path("perfil/", views.profile, name="profile"),
]
