from django.forms import ModelForm
from .models import Prescription, Medication
from django.contrib.auth.models import User
from django import forms

class PrescribeForm(forms.Form):
	def __init__(self, *args, **kwargs):
		super(PrescribeForm, self).__init__(*args, **kwargs)
		instance = getattr(self, 'instance', None)
		self.fields['patient'].widget.attrs['readonly'] = True 
		self.fields['doctor'].widget.attrs['disabled'] = 'disabled' 
		self.fields['date'].widget.attrs['readonly'] = True


	date = forms.DateTimeField()
	patient = forms.CharField()
	medication	= forms.ModelChoiceField(queryset=Medication.objects.all())
	dosage = forms.IntegerField()
	quantity = forms.IntegerField()
	doctor = forms.ModelChoiceField(queryset=User.objects.all())

class EditPrescriptionForm(ModelForm):
	readonly_patient = forms.CharField(label="Patient")
	class Meta:
		model = Prescription
		widgets = {'patient': forms.HiddenInput()}
		fields = 'date', 'readonly_patient', 'medication', 'dosage', 'quantity', 'doctor', 'patient'
	def __init__(self, *args, **kwargs):
		super(EditPrescriptionForm, self).__init__(*args, **kwargs)
		instance = getattr(self, 'instance', None)
		self.fields['readonly_patient'].initial = instance.patient
		self.fields['readonly_patient'].widget.attrs['readonly'] = True
		self.fields['date'].widget.attrs['readonly'] = True
		self.fields['doctor'].widget.attrs['disabled'] = 'disabled' 