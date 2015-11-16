from django import forms
from django.forms import ModelForm
from .models import LabTest, LabReport
import datetime

class RequestLabForm(forms.Form):
	def __init__(self, *args, **kwargs):
		super(RequestLabForm, self).__init__(*args, **kwargs)
		instance = getattr(self, 'instance', None)
		self.fields['patient'].widget.attrs['readonly'] = True
		self.fields['request_date'].widget.attrs['readonly'] = True
		self.fields['doctor'].widget.attrs['readonly'] = True

	patient = forms.CharField()
	request_date = forms.DateField()
	doctor = forms.CharField()
	lab_test = forms.ModelChoiceField(queryset=LabTest.objects.all())
	doctor_notes  = forms.CharField(widget=forms.Textarea)

class EditLabRequestForm(ModelForm):
	readonly_doctor = forms.CharField(label="Doctor")
	class Meta:
		model = LabReport
		fields = 'patient', 'request_date', 'readonly_doctor', 'lab_test', 'status', 'doctor_notes', 'doctor'
		widgets={'doctor': forms.HiddenInput()}
	def __init__(self, *args, **kwargs):
		super(EditLabRequestForm, self).__init__(*args, **kwargs)
		instance = getattr(self, 'instance', None)
		self.fields['readonly_doctor'].initial = instance.doctor
		self.fields['patient'].widget.attrs['readonly'] = True
		self.fields['request_date'].widget.attrs['readonly'] = True
		self.fields['readonly_doctor'].widget.attrs['readonly'] = True

# For Pharmacists: Add/Update the Results field, update_date field, lab_technician field, and status.
class UpdateLabReportForm(ModelForm):
	readonly_doctor = forms.CharField(label="Doctor")
	readonly_lab_test = forms.CharField(label="Lab test")
	class Meta:
		model = LabReport
		fields = 'patient', 'request_date', 'readonly_doctor', 'readonly_lab_test', 'lab_test', 'status', 'doctor_notes', 'doctor', 'results', 'update_date'
		widgets={'doctor': forms.HiddenInput(), 
				'lab_test': forms.HiddenInput(),
				'lab_technician': forms.HiddenInput(),
				'update_date': forms.HiddenInput()}
	def __init__(self, *args, **kwargs):
		super(UpdateLabReportForm, self).__init__(*args, **kwargs)
		instance = getattr(self, 'instance', None)

		self.fields['readonly_doctor'].initial = instance.doctor
		self.fields['readonly_lab_test'].initial = instance.lab_test
		self.fields['patient'].widget.attrs['readonly'] = True
		self.fields['request_date'].widget.attrs['readonly'] = True
		self.fields['readonly_doctor'].widget.attrs['readonly'] = True
		self.fields['readonly_lab_test'].widget.attrs['readonly'] = True
		self.fields['doctor_notes'].widget.attrs['readonly'] = True