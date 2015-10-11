from django.forms import ModelForm
from patients.models import Patient
from django.forms.widgets import CheckboxSelectMultiple
# Create the form class.

class PatientRegistrationForm(ModelForm):

	class Meta:
		model = Patient
		fields = '__all__'

		widgets = {
			'medical_background_information': CheckboxSelectMultiple,
			'allergies': CheckboxSelectMultiple
		}