from django.forms import ModelForm
from patients.models import Patient
from django.forms.widgets import CheckboxSelectMultiple, RadioSelect
from django.utils.safestring import mark_safe
from django import forms

# Create the form class.

class PatientRegistrationForm(ModelForm):

	class Meta:
		model = Patient
		exclude = 'nausea_level', 'headache_level', 'sore_throat_level', 'abdominal_pain_level', 'constipation_level', 'lack_of_appetite_level', 'sleepiness_level', 'insomnia_level'

		widgets = {
			'medical_background_information': CheckboxSelectMultiple,
			'allergies': CheckboxSelectMultiple
		}

class CurrentHealthConditionForm(ModelForm):
	class Meta:
		model = Patient
		fields = 'nausea_level', 'headache_level', 'sore_throat_level', 'abdominal_pain_level', 'constipation_level', 'lack_of_appetite_level', 'sleepiness_level', 'insomnia_level'

		widgets = {
			'nausea_level': RadioSelect,
			'headache_level': RadioSelect,
			'sore_throat_level': RadioSelect,
			'abdominal_pain_level': RadioSelect,
			'constipation_level': RadioSelect,
			'lack_of_appetite_level': RadioSelect,
			'sleepiness_level': RadioSelect,
			'insomnia_level': RadioSelect,
		}
