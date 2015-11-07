from __future__ import division
from django.test import TestCase, RequestFactory
from django.contrib.auth.models import User, Group
from django.test.client import Client
from django.shortcuts import redirect, get_object_or_404
# Import more modules here
from patients.models import Patient
from appointments.models import Appointment

from patients.views import patientProfile

import os # Used to clear screen

class IntegrationTest(TestCase):
	fixtures = ['patients_integration_data.json']
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


	def test_ServiceToDoctorsFeature(self):

		'''Doctors can access each patient cases from IPIMS'''
		print("\n\n")
		print("----------------------------")
		print("SERVICE TO DOCTORS")
		print("----------------------------")
		#Login as doctor
		self.client.login(username='doctor', password='password')
		print("Login to Doctor: SUCCESSFUL")
		print("Doctors can access each patient case from IPIMS")
		response = self.client.get('/patient/9/')

		# Try to access the patient's profile
		if (self.assertEquals(response.status_code, 200) == None):
			print("\tAccess Patient Profile: SUCCESSFUL")
		else: print("\tAccess Patient Profile: FAILED")

		# Verify that Doctor can view patient's appointments
		if (self.assertContains(response, 'Appointments') == None):
			print("\tAccess patient's appointment list: SUCCESSFUL")
		else: print("\tAccess patient's appointment list: FAILED")

		# Verify that Doctor can add Medical Records for patient
		if (self.assertContains(response, 'Add Medical Record') == None):
			# Add Medical Record button is visible
			add_medical_record_response = self.client.get('/records/add/9/')
			if (self.assertEquals(add_medical_record_response.status_code, 200) == None):
				print("\tAccess Add Medical Record form: SUCCESSFUL")
				# Submit a medical record using POST and verify that it is added successfully
				# ....
			else: print("\tAccess Add Medical Record form: FAILED")


	def test_ServiceToStaffFeature(self):
		self.client.login(username='pharmacist', password='password')
		response = self.client.get('/patient/9/')

		self.assertEquals(response.context['user'], self.pharmacist)

""" EXAMPLE CODE FROM GROUP 6 - Keep in mind that their code is very very different from ours, so 
this will only provide so much help """
	# def test_AppointmentFeature(self):
	# 	print '\n\n\n----------------------------------------------------------\nINTEGRATION TEST FOR SCHEDULE FUNCTIONALITY\n-----------------------------------------------------------'


	# 	self.patient_health_conditions = PatientHealthConditions.objects.create(

	# 		user = self.patient_object,
	# 		nausea_level = 10,
	# 		hunger_level = 8,
	# 		anxiety_level = 1, 
	# 		stomach_level = 3,
	# 		body_ache_level = 1,
	# 		chest_pain_level = 4
	# 		)
	# 	self.patient_health_conditions.save()


	# 	#Request an appointment to the healthcare provider
	# 	print '\t-Currently requesting a medical appointment from Dr. %s %s' %(self.doctor_obj.doctor_first_name, self.doctor_obj.doctor_last_name)

	# 	print '\t-Currently requesting an appointment for patient: %s %s' %(self.fill_patient_application.first_name, self.fill_patient_application.last_name)
	# 	print '\t-Appointment Details:'
	# 	print '\t\t+Date: %s'%("02/20/2016")
	# 	print '\t\t+Doctor: Dr. %s %s'%(self.doctor_obj.doctor_first_name, self.doctor_obj.doctor_last_name)
	# 	print '\t\t+Pain Level: %d'%(10)
	# 	print '\t\t+Medical Conditions: xanax'
	# 	print '\t\t+Allergies: %s'%(self.fill_patient_application.allergies)
	# 	print '\t\t+Patient: %s %s'%(self.fill_patient_application.first_name, self.fill_patient_application.last_name)
	# 	print '\t\t+Current Health Conditions: %d %d %d %d %d %d'%(self.patient_health_conditions.anxiety_level,
	# 															self.patient_health_conditions.stomach_level, 
	# 															self.patient_health_conditions.body_ache_level, 
	# 															self.patient_health_conditions.anxiety_level, 
	# 															self.patient_health_conditions.chest_pain_level, 
	# 															self.patient_health_conditions.hunger_level 
	# 															)

	# 	#Schedule an appointment
	# 	medical_appointment_1 = PatientAppt.objects.create(
	# 		date = "02/20/2016",
	# 		doctor = self.doctor_obj,
	# 		pain_level = 10,
	# 		medical_conditions = "chest pain and stomach issues",
	# 		allergies = self.fill_patient_application.allergies,
	# 		user = self.patient_object,
	# 		current_health_conditions = self.patient_health_conditions
	# 		)
	# 	medical_appointment_1.save()

	# 	print '\033[1;32m\nPATIENT APPOINTMENT (#1) CREATED SUCCESSFULLY!\033[0m\n'

	# 	print '\t-Test changing status of the appointment from not resolved to resolved'

	# 	#Change resolution status of appointment
	# 	medical_appointment_1.resolved = 1

	# 	self.assertEqual(1, medical_appointment_1.resolved)

	# 	print '\t-Medical appointment resolved successfully'

	# 	print '\033[1;32m\nPATIENT APPOINTMENT RESOLVED SUCCESSFULLY!\033[0m\n'

	# 	print '\t-Attempting to view all the currently scheduled appointments for patient %s %s' %(self.fill_patient_application.first_name, self.fill_patient_application.last_name)

	# 	print '\t-There are currently (%d) appointments in the database' %(PatientAppt.objects.all().count())

	# 	#Query appointment for the patient
	# 	current_appointment = PatientAppt.objects.filter(user = self.patient_object).get()

	# 	#Check appt. existence.
	# 	if (PatientAppt.objects.filter(user = self.patient_object).exists()):
	# 		print '\t-Appointment for patient has been found; Attempting to view appointment details'

	# 		#Retrieve appt data. (view)
	# 		current_appt = PatientAppt.objects.filter(user = self.patient_object).get()
	# 		print '\t-Appointment object is %s' %(current_appt)
	# 		print '\t\t+Date: %s'%(current_appt.date)
	# 		print '\t\t+Doctor: Dr. %s %s'%(current_appt.doctor.doctor_first_name, current_appt.doctor.doctor_last_name)
	# 		print '\t\t+Pain Level: %d'%(10)
	# 		print '\t\t+Medical Conditions: xanax'
	# 		print '\t\t+Allergies: %s'%(current_appt.allergies)
	# 		print '\t\t+Patient: %s %s'%(current_appt.user.fill_from_application.first_name, current_appt.user.fill_from_application.last_name)
	# 		print '\t\t+Current Health Conditions: %d %d %d %d %d %d'%(current_appt.current_health_conditions.anxiety_level,
	# 																current_appt.current_health_conditions.stomach_level, 
	# 																current_appt.current_health_conditions.body_ache_level, 
	# 																current_appt.current_health_conditions.anxiety_level, 
	# 																current_appt.current_health_conditions.chest_pain_level, 
	# 																current_appt.current_health_conditions.hunger_level 
	# 																)

	# 		print '\033[1;32m\nPATIENT APPOINTMENT VIEWED SUCCESSFULLY!\033[0m\n'

	# 	print '\tTesting the manage portion of the appointments scheduler..'
	# 	print '\tAttempting to change the date of the appointment'
	# 	print '\tCurrent appointment date: %s' %(current_appt.date)

	# 	#Updating appt. data
	# 	current_appt.date = "03/14/2015"

	# 	print '\tCurrent appointment date: %s' %(current_appt.date)

	# 	#Assert change was valid
	# 	self.assertEqual(current_appt.date, "03/14/2015")

	# 	print '\033[1;32m\nPATIENT APPOINTMENT DATE CHANGED SUCCESSFULLY!\033[0m\n'

	# 	print '\tTesting the manage portion of the appointments scheduler..'
	# 	print '\tAttempting to delete the appointment'

	# 	#Remove appt.
	# 	current_appt.delete()

	# 	#Assert positive removal
	# 	self.assertEqual(0, PatientAppt.objects.all().count())

	# 	print '\033[1;32m\nPATIENT APPOINTMENT DELETED SUCCESSFULLY!\033[0m\n'

	# 	#summary of the integration test that was ran
	# 	print '\033[30;42m\nSCHEDULE APPOINTMENT FEATURE INTEGRATION TEST SUMMARY:\033[0m'
	# 	print '\033[30;42m\n-Successful Patient Appointment Creation (Doctor Chosen based on health)\033[0m',
	# 	print '\033[30;42m\n-Successful Patient Appointment Resolution By Doctor\033[0m',
	# 	print '\033[30;42m\n-Successful Patient Appointment Viewed/Retrieved\033[0m',
	# 	print '\033[30;42m\n-Successful Patient Appoinment Managed (Updated/Removed)\033[0m'