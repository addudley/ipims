from django.forms import ModelForm
from .models import HealthCondition, Appointment, Emergency
from django import forms
from django.contrib.auth.models import User


class ScheduleAppointmentForm(forms.Form):
	"""Form for scheduling appointments """
	def __init__(self, *args, **kwargs):
		super(ScheduleAppointmentForm, self).__init__(*args, **kwargs)
		# Set patient field to readonly. 
		self.fields['patient'].widget.attrs['readonly'] = True

	# Declare form fields
	patient = forms.CharField()
	date = forms.DateTimeField()
	health_condition = forms.ModelChoiceField(queryset=HealthCondition.objects.all())
	doctor = forms.ModelChoiceField(queryset=User.objects.all())

class EditAppointmentForm(ModelForm):
	"""Form for editing existing appointment """

	class Meta:

		model = Appointment
		fields = '__all__'
		widgets = {'patient': forms.HiddenInput()} # Hide patient form. 


class EmergencyForm(ModelForm):
	class Meta:
		model = Emergency
		fields = '__all__'