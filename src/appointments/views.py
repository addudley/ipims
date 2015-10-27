from django.shortcuts import render
from django.conf.urls import include, url
from django.views.generic import CreateView, UpdateView, DetailView
from django.shortcuts import get_object_or_404
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.views.generic.list import ListView
from django.utils import timezone

import datetime

from .models import Appointment, Emergency, HealthCondition
from patients.models import Patient
from .forms import ScheduleAppointmentForm, EditAppointmentForm, EmergencyForm

def scheduleAppointment(request, patient_pk):
	if request.method == 'POST':
		form = ScheduleAppointmentForm(request.POST)

		if form.is_valid():
			patient_instance = Patient.objects.get(pk=patient_pk)
			p = Appointment.objects.create(
				patient=patient_instance, 
				date=form.cleaned_data['date'], 
				health_condition=HealthCondition.objects.get(pk = request.POST.get("health_condition", "")),
				doctor=form.cleaned_data['doctor'])
			return HttpResponseRedirect('/appointments/' + str(p.pk) )

		else:
			return render(request, 'appointments/schedule_appointment_form.html', {
		'form': form,})
			
	data = {'patient': Patient.objects.get(pk=patient_pk), 
			'date': datetime.datetime.now()}
	form = ScheduleAppointmentForm(initial=data)

	return render(request, 'appointments/schedule_appointment_form.html', {
		'form': form,
		'patient': Patient.objects.get(pk=patient_pk)
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