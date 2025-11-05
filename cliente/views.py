from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from agendamento.models import Appointment

@login_required
def dashboard(request):
    appointments = request.user.appointments.filter(canceled=False)
    return render(request, "cliente/dashboard.html", {"appointments": appointments})

@login_required
def profile(request):
    return render(request, "cliente/profile.html")
