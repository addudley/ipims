from django.forms import ModelForm
from .models import HealthCondition, Appointment, Emergency
from django import forms


class ScheduleAppointmentForm(ModelForm):
	class Meta:
		model = Appointment
		fields = '__all__'

class EditAppointmentForm(ModelForm):


	class Meta:
		model = Appointment
		fields = '__all__'
		widgets = {'patient': forms.HiddenInput()}


class EmergencyForm(ModelForm):
	class Meta:
		model = Emergency
		fields = '__all__'