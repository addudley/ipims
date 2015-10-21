from django.forms import ModelForm
from .models import HealthCondition, Appointment, Emergency


class ScheduleAppointmentForm(ModelForm):
    class Meta:
        model = Appointment
        fields = '__all__'

class EmergencyForm(ModelForm):
    class Meta:
        model = Emergency
        fields = '__all__'