from django.test import TestCase
from .models import Appointment

class ScheduleAppointmentViewTestCase(TestCase):
# Verify Schedule Appointment view loads successfully
	def test_schedule_appointment_view(self):
		resp = self.client.get('/appointments/add/')
		self.assertEqual(resp.status_code, 200)

class AppointmentDetailsViewTestCase(TestCase):
# Verify Schedule Appointment view loads successfully
	fixtures = ['appointments_testdata.json', 'patients_testdata.json'] # Load test data (appointments, Patient, User [doctors])
	def test_schedule_appointment(self):
		resp = self.client.get('/appointments/1/')
		appointment = resp.context['appointment']
		self.assertEqual(appointment.id, 1)
		self.assertEqual(resp.status_code, 200)

