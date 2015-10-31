from django import forms
from django.forms import ModelForm
from .models import LabTest, LabReport

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
	readonly_doctor = forms.CharField()
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