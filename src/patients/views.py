from django.shortcuts import render, render_to_response, RequestContext
from haystack.query import SearchQuerySet
from haystack.forms import SearchForm
from .forms import PatientRegistrationForm
from django.core.urlresolvers import reverse
# Create your views here.

from django.views.generic import CreateView, UpdateView, DetailView
from haystack.generic_views import SearchView
from .models import Patient

class PatientNew(CreateView):
	model = Patient
	form_class = PatientRegistrationForm
	def get_success_url(self):
		return reverse('patient_profile', kwargs={
			'pk': self.object.pk
			})

class PatientUpdate(UpdateView):
	model = Patient
	template_name_suffix = '_update_form'
	form_class = PatientRegistrationForm
	def get_success_url(self):
		return reverse('patient_profile', kwargs={
			'pk': self.object.pk
			})


def patientProfile(request, pk):
    patient = Patient.objects.get(pk=pk)
    allergies = patient.allergies.all()
    medical_history = patient.medical_background_information.all()
    context = {'patient': patient, 'allergies': allergies, 'medical_history': medical_history}
    return render(request, 'patients/patient_profile.html', context)

class PatientSearchView(SearchView):
    template_name = 'search/search.html'
    queryset = SearchQuerySet()

