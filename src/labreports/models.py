from django.db import models
from patients.models import Patient
from django.contrib.auth.models import User
import datetime

class LabTest(models.Model):
	name = models.CharField(max_length = 128)
	def __str__(self):
		return self.name

# Create your models here.
class LabReport(models.Model):
	REQUESTED = 'r'
	IN_PROGRESS = 'ip'
	COMPLETE = 'c'

	STATUS_CHOICES = ((REQUESTED, 'Requested'), (IN_PROGRESS, 'In Progress'), (COMPLETE, 'Complete'))

	request_date = models.DateField(("Date"), default=datetime.date.today)
	doctor = models.ForeignKey(User, related_name="doctor")
	patient = models.ForeignKey(Patient)
	lab_test = models.ForeignKey('LabTest')
	status = models.CharField(max_length=2, choices=STATUS_CHOICES)
	doctor_notes = models.TextField(blank=True, null=True)
	results = models.TextField(blank=True, null=True)
	lab_technician = models.ForeignKey(User, blank=True, null=True, related_name="lab_technician")
	update_date = models.DateField(("Date"), blank=True, null=True)

	def __str__(self):
		return 'lab_report_' + str(self.pk)