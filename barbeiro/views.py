from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from agendamento.models import Appointment

@login_required
def agenda(request):
    appointments = Appointment.objects.filter(barbeiro=request.user, canceled=False)
    return render(request, "barbeiro/agenda.html", {"appointments": appointments})
