from django.shortcuts import render
from django.conf.urls import include, url
from django.views.generic import CreateView, UpdateView, DetailView
from django.shortcuts import get_object_or_404
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.views.generic.list import ListView
from django.utils import timezone

from .models import Appointment, Emergency
from .forms import ScheduleAppointmentForm, EditAppointmentForm, EmergencyForm

class ScheduleAppointment(CreateView):
	model = Appointment
	form_class = ScheduleAppointmentForm
	template_name = 'appointments/schedule_appointment_form.html'

	def form_valid(self, form):
		self.object = form.save()
		return HttpResponseRedirect(self.get_success_url())

	def get_success_url(self):
		return reverse('appointment_details', kwargs={
			'pk': self.object.pk
			})

class EditAppointment(UpdateView):
	model = Appointment
	form_class = EditAppointmentForm
	template_name = 'appointments/edit_appointment_form.html'

	def form_valid(self, form):
		self.object = form.save()
		return HttpResponseRedirect(self.get_success_url())

	def get_success_url(self):
		return reverse('appointment_details', kwargs={
			'pk': self.object.pk
			})

class EmergencyAppointment(CreateView):
	model = Emergency
	form_class = EmergencyForm
	template_name = 'appointments/emergency_form.html'

	def form_valid(self, form):
		self.object = form.save()
		return HttpResponseRedirect(self.get_success_url())

	def get_success_url(self):
		return '/appointments/'

class AppointmentDetails(DetailView):
	model = Appointment
	template_name = 'appointments/details.html'
	def get_context_data(self, **kwargs):
		context = super(AppointmentDetails, self).get_context_data(**kwargs)
		return context


class AppointmentListView(ListView):

	model = Appointment

	def get_context_data(self, **kwargs):
		context = super(AppointmentListView, self).get_context_data(**kwargs)
		return context

def delete(request, id):
	appointment = get_object_or_404(Appointment, pk=id)
	patient_id = appointment.patient.pk
	appointment.delete()
	return HttpResponseRedirect('/patient/' + str(patient_id))