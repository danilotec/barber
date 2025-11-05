from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Service, Appointment
from .forms import AppointmentForm
from django.contrib import messages

def services_list(request):
    services = Service.objects.filter(active=True)
    return render(request, "agendamento/services_list.html", {"services": services})

@login_required
def create_appointment(request):
    if request.method == "POST":
        form = AppointmentForm(request.POST)
        if form.is_valid():
            appt = form.save(commit=False)
            appt.cliente = request.user
            appt.save()
            messages.success(request, "Agendamento criado.")
            return redirect("cliente:dashboard")
    else:
        form = AppointmentForm()
    return render(request, "agendamento/appointment_form.html", {"form": form})

@login_required
def appointment_detail(request, pk):
    appt = get_object_or_404(Appointment, pk=pk, cliente=request.user)
    return render(request, "agendamento/appointment_detail.html", {"appointment": appt})
