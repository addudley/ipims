from django.db import models

# Create your models here.
from django.utils.translation import ugettext as _
from localflavor.us.models import USStateField
from localflavor.us.models import PhoneNumberField

class MedicalBackgroundChoice(models.Model):
	description = models.CharField(max_length=128)
	def __str__(self):
		return self.description

class Allergy(models.Model):
	description = models.CharField(max_length=128)
	def __str__(self):
		return self.description

class Patient(models.Model):
	first_name = models.CharField(max_length = 30)
	last_name = models.CharField(max_length = 30)
	dob = models.DateField()
	ssn = models.CharField(max_length = 11)
	phone_number = PhoneNumberField(default = 'null')
	email = models.EmailField(default = 'null')

	# Address Info
	address = models.CharField(max_length = 128)
	city = models.CharField(max_length=64)
	state = USStateField()
	zip_code = models.PositiveIntegerField()

	# Health Insurance
	health_insurance_provider = models.CharField(max_length = 64)
	health_insurance_id = models.CharField(max_length = 30)

	# Medical History
	medical_background_information = models.ManyToManyField(MedicalBackgroundChoice, blank=True)
	allergies = models.ManyToManyField(Allergy, blank=True)

	def get_full_name(self):
		# returns the patient's full name (ex: Doe, John)
		return '%s, %s' % (self.last_name, self.first_name)