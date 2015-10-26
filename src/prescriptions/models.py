from django.db import models

from patients.models import Patient
from django.contrib.auth.models import User
from django.utils import timezone
import datetime

# Create your models here.

class Medication(models.Model):
	name = models.CharField(max_length=128)
	def __str__(self):
		return self.name

class Prescription(models.Model):
	date = models.DateField(("Date"), default=datetime.date.today)
	patient = models.ForeignKey(Patient)
	medication = models.ForeignKey('Medication')
	dosage = models.PositiveIntegerField('Dosage (mg)')
	quantity = models.PositiveIntegerField()
	doctor = models.ForeignKey(User)
	filled_on = models.DateField(blank=True, null=True)

	def __str__(self):
		return self.medication
