from django import forms
from django.forms import ModelForm
from .models import Record
from appointments.models import HealthCondition

class AddRecordForm(forms.Form):
	def __init__(self, *args, **kwargs):
		super(AddRecordForm, self).__init__(*args, **kwargs)
		self.fields['patient'].widget.attrs['readonly'] = True
		self.fields['date_created'].widget.attrs['readonly'] = True
		self.fields['doctor'].widget.attrs['readonly'] = True
		self.fields['resolved'].initial = 0
	
	patient = forms.CharField()
	date_created = forms.DateField()
	doctor = forms.CharField()
	health_condition = forms.ModelChoiceField(queryset=HealthCondition.objects.all())
	notes = forms.CharField(widget=forms.Textarea, required = False)
	resolved = forms.BooleanField(required=False)

class UpdateRecordForm(ModelForm):
	readonly_doctor = forms.CharField(label="Doctor")
	readonly_patient = forms.CharField(label="Patient")
	class Meta:
		model = Record
		fields = 'patient', 'readonly_patient', 'date_created', 'doctor', 'readonly_doctor', 'health_condition', 'notes', 'resolved'
		widgets={'doctor': forms.HiddenInput(),
				 'patient': forms.HiddenInput()}
	def __init__(self, *args, **kwargs):
		super(UpdateRecordForm, self).__init__(*args, **kwargs)
		instance = getattr(self, 'instance', None)
		self.fields['readonly_doctor'].initial = instance.doctor
		self.fields['readonly_patient'].initial = instance.patient
		self.fields['readonly_patient'].widget.attrs['readonly'] = True
		self.fields['date_created'].widget.attrs['readonly'] = True
		self.fields['readonly_doctor'].widget.attrs['readonly'] = True