from django.db import models
from patients.models import Patient
from django.contrib.auth.models import User
from smart_selects.db_fields import ChainedForeignKey

# Create your models here.
class Appointment(models.Model):
	""" Appointment model

	Dependencies: HealthCondition
	 """
	patient = models.ForeignKey(Patient)
	date = models.DateTimeField();
	health_condition = models.ForeignKey('HealthCondition')
	doctor = models.ForeignKey(User)
	def __str__(self):
		return str(self.pk)

class Emergency(models.Model):
	""" Emergency model

	Dependencies: HealthCondition
	"""
	patient = models.ForeignKey(Patient)
	date = models.DateTimeField();
	health_condition = models.ForeignKey('HealthCondition')
	doctor = models.ForeignKey(User)
	def __str__(self):
		return str(self.pk)


class HealthCondition(models.Model):
	""" HealthCondition model

	Links doctors to the specific health conditions that they treat.
	Used in Medical Records, as well.
	"""
	description = models.CharField(max_length = 64)
	doctors = models.ManyToManyField(User, blank=True)
	def __str__(self):
		return self.description