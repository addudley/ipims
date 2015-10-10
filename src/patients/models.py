from django.db import models

# Create your models here.
from django.utils.translation import ugettext as _
from localflavor.us.models import USStateField


class Patient(models.Model):
	first_name = models.CharField(max_length = 30)
	last_name = models.CharField(max_length = 30)
	dob = models.DateField()
	ssn = models.CharField(max_length = 11)

	# Address Info
	address = models.CharField(max_length = 128)
	city = models.CharField(max_length=64)
	state = USStateField()
	zip_code = models.PositiveIntegerField()

	# Health Insurance
	health_insurance_provider = models.CharField(max_length = 64)
	health_insurance_id = models.CharField(max_length = 30)

	def get_full_name(self):
		# returns the patient's full name (ex: Doe, John)
		return '%s, %s' % (self.last_name, self.first_name)