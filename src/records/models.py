from django.db import models
from patients.models import Patient
from django.contrib.auth.models import User
from smart_selects.db_fields import ChainedForeignKey
from appointments.models import HealthCondition

# Create your models here.
class Record(models.Model):
	patient = models.ForeignKey(Patient)
	date_created = models.DateTimeField();
	doctor = models.ForeignKey(User)
	health_condition = models.ForeignKey(HealthCondition)
	notes = models.TextField(blank=True, null=True)
	resolved = models.BooleanField(default=False)

	def __str__(self):
		return str(self.pk)