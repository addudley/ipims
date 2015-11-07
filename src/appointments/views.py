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
	"""View for scheduling a new appointment.

	Template: appointments/schedule_appointment_form.html
	Form: appointments/forms.py → ScheduleAppointmentForm()
	"""
	if request.method == 'POST':
		''' When the user clicks Submit '''
		# Load data from the form
		form = ScheduleAppointmentForm(request.POST)

		if form.is_valid():
			'''If the data from the form is valid, create a appointment object with the data from the fields.

			Redirect user to the details page for new appointment 
			'''
			patient_instance = Patient.objects.get(pk=patient_pk) # get patient object using the patient's primary key (from URL argument)
			p = Appointment.objects.create(
				patient=patient_instance, 
				date=form.cleaned_data['date'], 
				health_condition=HealthCondition.objects.get(pk = request.POST.get("health_condition", "")), # Sets health condition object using pk from health condition field
				doctor=form.cleaned_data['doctor'])
			return HttpResponseRedirect('/appointments/' + str(p.pk) )

		else:
			# If the form contains invalid fields, reload form with the same values and display errors.
			return render(request, 'appointments/schedule_appointment_form.html', {
		'form': form,})
			

	''' When form first loads '''
	# Generate initial field values (They're readonly, so can't be changed by user)
	data = {'patient': Patient.objects.get(pk=patient_pk), 
			'date': datetime.datetime.now()}
	# Create form
	form = ScheduleAppointmentForm(initial=data)

	# Display the Schedule Appointment form.
	return render(request, 'appointments/schedule_appointment_form.html', {
		'form': form,
		'patient': Patient.objects.get(pk=patient_pk)
	})

class EditAppointment(UpdateView):
	"""View for editing an existing appointment

	Template: appointments/edit_appointment_form.html
	Form: appointment/forms.py → EditAppointmentForm

	"""
	model = Appointment
	form_class = EditAppointmentForm
	template_name = 'appointments/edit_appointment_form.html'

	def form_valid(self, form):
		'''If the form fields are valid, update the Appointment model.

		Return to the Appointment 
		'''
		self.object = form.save()
		return HttpResponseRedirect(self.get_success_url())

	def get_success_url(self):
		return reverse('appointment_details', kwargs={
			'pk': self.object.pk
			})

class EmergencyAppointment(CreateView):
	""" View for Creating an Emergency appointment

	Model: Emergency
	Template: appointments/emergency_form.html
	Form: appointments/forms.py → EmergencyForm

	"""
	model = Emergency
	form_class = EmergencyForm
	template_name = 'appointments/emergency_form.html'

	def form_valid(self, form):
		'''If the form fields are valid, create Emergency model.

		Redirect user 

		'''
		self.object = form.save()
		return HttpResponseRedirect(self.get_success_url())

	def get_success_url(self):
		return '/appointments/' + str(self.object.pk)

class AppointmentDetails(DetailView):
	"""View for the Appointment Details

	Model: Appointment
	Template: appointmentments/details.html

	"""
	model = Appointment
	template_name = 'appointments/details.html'
	def get_context_data(self, **kwargs):
		context = super(AppointmentDetails, self).get_context_data(**kwargs)
		return context

""" OBSOLETE - Delete? """
# class AppointmentListView(ListView):

# 	model = Appointment

# 	def get_context_data(self, **kwargs):
# 		context = super(AppointmentListView, self).get_context_data(**kwargs)
# 		return context


def delete(request, id):
	""" Delete patient (pk = id)

	"""
	appointment = get_object_or_404(Appointment, pk=id)
	patient_id = appointment.patient.pk
	appointment.delete()
	return HttpResponseRedirect('/search')