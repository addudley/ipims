from django.shortcuts import render
from django.conf.urls import include, url
from django.views.generic import CreateView, UpdateView, DetailView

from .models import Appointment
from .forms import ScheduleAppointmentForm

class ScheduleAppointment(CreateView):
	model = Appointment
	form_class = ScheduleAppointmentForm
	template_name = 'appointments/schedule_appointment_form.html'
	def get_success_url(self):
		return '/'