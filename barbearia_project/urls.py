from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from core import views as core_views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", core_views.landing, name="landing"),
    path("agendamento/", include("agendamento.urls")),
    path("cliente/", include("cliente.urls")),
    path("barbeiro/", include("barbeiro.urls")),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
