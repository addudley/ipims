from django.forms import ModelForm
from .models import HealthCondition, Appointment, Emergency
from django import forms
from django.contrib.auth.models import User
from default.widgets import UserFullnameChoiceField
from datetimewidget.widgets import DateTimeWidget

class ScheduleAppointmentForm(forms.Form):
	"""Form for scheduling appointments """
	def __init__(self, *args, **kwargs):
		super(ScheduleAppointmentForm, self).__init__(*args, **kwargs)
		# Set patient field to readonly. 
		self.fields['patient'].widget.attrs['readonly'] = True

	# Declare form fields
	patient = forms.CharField()
	date = forms.DateTimeField(widget=DateTimeWidget(attrs={'id':"yourdatetimeid"}, usel10n = True, bootstrap_version=3, 
													options= {
													'format': 'dd/mm/yyyy HH:ii P',
													'autoclose': True,
													'showMeridian' : True,
													'clearBtn': False
													}))
	health_condition = forms.ModelChoiceField(queryset=HealthCondition.objects.all())
	doctor = forms.ModelChoiceField(queryset=User.objects.all())

class EditAppointmentForm(ModelForm):
	"""Form for editing existing appointment """
	readonly_doctor = UserFullnameChoiceField(queryset=User.objects.all(), label="Doctor")
	class Meta:
		model = Appointment
		fields = 'patient', 'date', 'health_condition', 'doctor', 'readonly_doctor'
		widgets = {'patient': forms.HiddenInput(),
					'doctor': forms.HiddenInput(),
					'date': DateTimeWidget(attrs={'id':"yourdatetimeid"}, usel10n = True, bootstrap_version=3, 
													options= {
													'format': 'dd/mm/yyyy HH:ii P',
													'autoclose': True,
													'showMeridian' : True,
													'clearBtn': False
													})} # Hide patient form. 
	def __init__(self, *args, **kwargs):
		super(EditAppointmentForm, self).__init__(*args, **kwargs)
		instance = getattr(self, 'instance', None)
		self.fields['readonly_doctor'].initial = instance.doctor
		self.fields['doctor'].widget.attrs['disabled'] = 'disabled'
		self.fields['readonly_doctor'].widget.attrs['disabled'] = 'disabled' 
		self.fields['health_condition'].widget.attrs['disabled'] = 'disabled' 

class EmergencyForm(forms.Form):
	"""Form for alerting emergency room staff of incoming patient """
	def __init__(self, *args, **kwargs):
		super(EmergencyForm, self).__init__(*args, **kwargs)
		# Set patient field to readonly. 
		self.fields['patient'].widget.attrs['readonly'] = True

	# Declare form fields
	patient = forms.CharField()
	health_condition = forms.ModelChoiceField(queryset=HealthCondition.objects.all())
	doctor = forms.ModelChoiceField(queryset=User.objects.all())

