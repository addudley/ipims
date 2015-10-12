from django.shortcuts import render
from django.conf.urls import include, url
from django.views.generic import CreateView, UpdateView, DetailView
from django.core.urlresolvers import reverse


from .models import Appointment
from .forms import ScheduleAppointmentForm

class ScheduleAppointment(CreateView):
	model = Appointment
	form_class = ScheduleAppointmentForm
	template_name = 'appointments/schedule_appointment_form.html'
	def get_success_url(self):
		return reverse('appointment_details', kwargs={
			'pk': self.object.pk
			})

class AppointmentDetails(DetailView):
	model = Appointment
	template_name = 'appointments/details.html'
	def get_context_data(self, **kwargs):
		context = super(AppointmentDetails, self).get_context_data(**kwargs)
		return context