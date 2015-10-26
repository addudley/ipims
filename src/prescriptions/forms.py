from django.forms import ModelForm
from .models import Prescription
from django import forms


class PrescribeForm(ModelForm):

	class Meta:
		model = Prescription
		exclude = 'filled_on',
		widgets = {}
	def __init__(self, *args, **kwargs):
		super(PrescribeForm, self).__init__(*args, **kwargs)
		instance = getattr(self, 'instance', None)
		if instance and instance.pk:
			self.fields['patient'].widget.attrs['readonly'] = True

	def clean_sku(self):
		instance = getattr(self, 'instance', None)
		if instance and instance.pk:
			return instance.patient
		else:
			return self.cleaned_data['sku']