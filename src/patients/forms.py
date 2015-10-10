from django.forms import ModelForm
from patients.models import Patient

# Create the form class.
class PatientForm(ModelForm):
	class Meta:
		model = Patient
		fields = '__all__'

