from __future__ import division
from django.test import TestCase, RequestFactory
from django.contrib.auth.models import User, Group
from django.test.client import Client
from django.shortcuts import redirect, get_object_or_404
from django.test import TestCase, SimpleTestCase
# Import more modules here
from patients.models import Patient
from appointments.models import Appointment, HealthCondition

from patients.views import patientProfile

import datetime

import os

class IntegrationTest(TestCase):
	fixtures = ['patients_integration_data.json', 'healthconditions_testdata.json']
	# Clear Screen 
	os.system('cls' if os.name == 'nt' else 'clear')

	def setUp(self):
		# See https://docs.djangoproject.com/en/1.8/topics/testing/advanced/
		self.factory = RequestFactory()

		self.client = Client()

		''' Create a user from each role, and assign them to the group for their role '''
		# Doctor
		self.doctor = User.objects.create_user(username="doctor", email="fake@email.com", password="password")
		self.doctor.save()
		self.doctor_group = Group.objects.create(name="doctor")
		self.doctor_group.user_set.add(self.doctor)
		self.doctor_group.save()

		# Lab Technician
		self.lab_technician = User.objects.create_user(username="lab_technician", password="password")
		self.lab_technician.save()
		self.lab_technician_group = Group.objects.create(name="lab_technician")
		self.lab_technician_group.user_set.add(self.lab_technician)
		self.lab_technician_group.save()

		# Nurse
		self.nurse = User.objects.create_user(username="nurse", password="password")
		self.nurse_group = Group.objects.create(name="nurse")
		self.nurse_group.user_set.add(self.nurse)
		self.nurse_group.save()

		# Doctor
		self.staff = User.objects.create_user(username="staff", password="password")
		self.staff.save()
		self.staff_group = Group.objects.create(name="staff")
		self.staff_group.user_set.add(self.staff)
		self.staff_group.save()

		# Pharmacist
		self.pharmacist = User.objects.create_user(username="pharmacist", password="password")
		self.pharmacist.save()
		self.pharmacist_group = Group.objects.create(name="pharmacist")
		self.pharmacist_group.user_set.add(self.pharmacist)
		self.pharmacist_group.save()

	def test_patientProfile(self):
		self.client.login(username='doctor', password='password')
		print("\n\nLOADING PATIENT PROFILE")
		start = datetime.datetime.now() # Get current time
		response = self.client.get('/patient/9/') # Load patient profile page
		self.assertEquals(response.status_code, 200) # Verify that valid page loaded
		end = datetime.datetime.now() # Get current time
		total_time = (end-start).total_seconds() # Calculate total time for process
		print('\tElapsed time:', total_time, 'seconds')

	def test_ScheduleAppointment(self):
		self.client.login(username='doctor', password='password')
		print("\n\nSCHEDULING APPOINTMENT")
		start = datetime.datetime.now()
		count_before = Appointment.objects.all().count()
		response = self.client.post('/appointments/add/13/', {'patient':Patient.objects.get(pk=13), 'date':datetime.datetime.now(), 'health_condition':1, 'doctor':1}, follow=True)
		count_after = Appointment.objects.all().count()
		self.assertEquals(response.status_code, 200) # Verify that response landed on a valid page
		self.assertTemplateUsed(response, 'appointments/details.html') # Verify that we landed on an appointment details page
		end = datetime.datetime.now() # Get current time
		total_time = (end-start).total_seconds() # Calculate total time for process
		print('\tElapsed time:', total_time, 'seconds')

