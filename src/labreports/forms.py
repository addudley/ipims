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