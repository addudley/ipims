from django.shortcuts import render, render_to_response, RequestContext
from haystack.query import SearchQuerySet
from haystack.forms import SearchForm
from .forms import PatientRegistrationForm, CurrentHealthConditionForm
from django.core.urlresolvers import reverse

from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from django.views.generic import CreateView, UpdateView, DetailView, ListView
from haystack.generic_views import SearchView
from .models import Patient

from appointments.models import Appointment
from prescriptions.models import Prescription
from labreports.models import LabReport
from records.models import Record

from notifications import notify
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect



class PatientNew(CreateView):
	model = Patient
	form_class = PatientRegistrationForm

	def get_success_url(self):
		return reverse('patient_profile', kwargs={
			'pk': self.object.pk
			})

class PatientUpdate(UpdateView):
	model = Patient
	form_class = PatientRegistrationForm
	def get_success_url(self):
		return reverse('patient_profile', kwargs={
			'pk': self.object.pk
			})

class CurrentHealthCondition(UpdateView):
	model = Patient
	template_name_suffix = '_update_form'
	form_class = CurrentHealthConditionForm

	def form_valid(self, form):
		self.object = form.save()
		calculate_health_condition(self, form)
		return HttpResponseRedirect(self.get_success_url())

	def get_success_url(self):
		return reverse('patient_profile', kwargs={
			'pk': self.object.pk
			})

def calculate_health_condition(self, form):
	user = self.request.user
	patient = self.object
	total = 0
	current_health_condition_levels = {'Nausea level': patient.nausea_level, 'Headache level': patient.headache_level, 'Sore Throat level': patient.sore_throat_level, 'Abdominal Pain level': patient.abdominal_pain_level, 'Constipation level': patient.constipation_level, 'Lack of Appetite level': patient.lack_of_appetite_level, 'sleepiness_level': patient.sleepiness_level, 'insomnia_level': patient.insomnia_level}
	for level in current_health_condition_levels:
		total += int(current_health_condition_levels[level])
		if int(current_health_condition_levels[level]) >= 7:
			notify.send(user, recipient=user, verb='%s %s\'s %s is %s' % (patient.first_name, patient.last_name, level, current_health_condition_levels[level]), level='warning')
	if total >= 50:
		notify.send(user, recipient=user, verb='%s\'s health condition is urgent (Level: %s)' % (patient.get_full_name(), total), level='danger')


# class PatientProfileView(DetailView):
# 	model = Patient
# 	template_name = 'patients/patient_profile.html'

# 	def get_queryset(self):
# 		self.publisher = get_object_or_404(Publisher, name=self.args[0])
# 		return Book.objects.filter(publisher=self.publisher)

# 	def get_context_data(self, **kwargs):
# 		context = super(PatientProfileView, self).get_context_data(**kwargs)
# 		current_health_condition = {'nausea_level': self.patient.nausea_level, 'headache_level': self.patient.headache_level, 'sore_throat_level': self.patient.sore_throat_level, 'abdominal_pain_level': self.patient.abdominal_pain_level, 'constipation_level': self.patient.constipation_level, 'lack_of_appetite_level': self.patient.lack_of_appetite_level, 'sleepiness_level': self.patient.sleepiness_level, 'insomnia_level': self.patient.insomnia_level}
# 		context['current_health_condition'] = current_health_condition
# 		context['appointments'] = Appointment.objects.all()
# 		return context

def patientProfile(request, pk):
	patient = Patient.objects.get(pk=pk)
	allergies = patient.allergies.all()
	medical_history = patient.medical_background_information.all()
	current_health_condition = {'nausea_level': ['Nauseous', int(patient.nausea_level)], 
								'headache_level': ['Headache', int(patient.headache_level)], 
								'sore_throat_level': ['Sore throat', int(patient.sore_throat_level)], 
								'abdominal_pain_level': ['Abdominal pain', int(patient.abdominal_pain_level)], 
								'constipation_level': ['Constipated', int(patient.constipation_level)], 
								'lack_of_appetite_level': ['Lack of appetite', int(patient.lack_of_appetite_level)], 
								'sleepiness_level': ['Sleepy', int(patient.sleepiness_level)], 
								'insomnia_level': ['Insomnia', int(patient.insomnia_level)]
								}
	appointments = Appointment.objects.filter(patient=pk).order_by('date').reverse()
	prescriptions = Prescription.objects.filter(patient=pk).order_by('date').reverse()
	lab_reports = LabReport.objects.filter(patient=pk).order_by('request_date').reverse()
	records = Record.objects.filter(patient=pk).order_by('date_created').reverse()
	context = {'patient': patient, 'allergies': allergies, 
				'medical_history': medical_history, 
				'current_health_condition': current_health_condition,
				'appointments': appointments,
				'prescriptions': prescriptions,
				'lab_reports': lab_reports,
				'records': records
				}
	return render(request, 'patients/patient_profile.html', context)

class PatientSearchView(SearchView):
	template_name = 'search/search.html'
	queryset = SearchQuerySet()