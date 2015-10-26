from django.shortcuts import render, get_object_or_404
from django.views.generic import CreateView, UpdateView, DetailView, ListView
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

from .models import *
from .forms import *

# Create your views here.
class Prescribe(CreateView):
	model = Prescription
	form_class = PrescribeForm
	template_name = 'prescriptions/prescribe_form.html'

	#current_patient = request.GET.get('patient', '')

	def form_valid(self, form):
		self.object = form.save()
		return HttpResponseRedirect(self.get_success_url())

	def get_success_url(self):
		pk = self.object.pk
		return '/prescriptions/' + str(pk) + '/'

	def get_initial(self):
		patient = get_object_or_404(Patient, pk = self.kwargs.get('patient'))
		return { 'patient': patient.first_name }

class EditPrescriptionView(UpdateView):
	model = Prescription
	form_class = PrescribeForm
	template_name = 'prescriptions/prescribe_form.html'

	def form_valid(self, form):
		self.object = form.save()
		return HttpResponseRedirect(self.get_success_url())

	def get_success_url(self):
		pk = self.object.pk
		return '/prescriptions/' + str(pk) + '/'

class PrescriptionDetailsView(DetailView):
	model = Prescription
	template_name = 'prescriptions/prescription_details.html'
	def get_context_data(self, **kwargs):
		context = super(PrescriptionDetailsView, self).get_context_data(**kwargs)
		return context

class PrescriptionListView(ListView):

	model = Prescription

	def get_context_data(self, **kwargs):
		context = super(PrescriptionListView, self).get_context_data(**kwargs)
		return context

def delete(request, id):
	prescription = get_object_or_404(Prescription, pk=id)
	patient_id = prescription.patient.pk
	prescription.delete()
	return HttpResponseRedirect('/patient/' + str(patient_id))