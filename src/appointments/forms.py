from django.forms import ModelForm
from .models import HealthCondition, Appointment


class ScheduleAppointmentForm(ModelForm):
    class Meta:
        model = Appointment
        fields = '__all__'