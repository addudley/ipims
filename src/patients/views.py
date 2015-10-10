from django.shortcuts import render, render_to_response, RequestContext
from haystack.query import SearchQuerySet
from haystack.forms import SearchForm

# Create your views here.

from django.views.generic import CreateView, UpdateView
from haystack.generic_views import SearchView
from .models import Patient

class PatientNew(CreateView):
	model = Patient
	fields = ('__all__')

class PatientUpdate(UpdateView):
	model = Patient
	fields = ('__all__')
	template_name_suffix = '_update_form'

def profile(request, pk):
    patient = Patient.objects.get(pk=pk)
    context = {'patient': patient}
    return render(request, 'patients/patient_profile.html', context)

class PatientSearchView(SearchView):
    template_name = 'search/search.html'
    queryset = SearchQuerySet()

