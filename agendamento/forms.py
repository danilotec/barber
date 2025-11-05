from django import forms
from .models import Appointment

class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ["service", "barbeiro", "start", "end"]
        widgets = {
            "start": forms.DateTimeInput(attrs={"type": "datetime-local"}),
            "end": forms.DateTimeInput(attrs={"type": "datetime-local"}),
        }
