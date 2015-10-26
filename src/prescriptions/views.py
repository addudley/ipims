from django.shortcuts import render, get_object_or_404
from django.views.generic import CreateView, UpdateView, DetailView, ListView
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.shortcuts import render_to_response	
from django.contrib.auth.models import User
from .models import *
from .forms import *

# Create your views here.
def prescribe(request, patient):
	if request.method == 'POST':
		form = PrescribeForm(request.POST)

		if form.is_valid():
			patient_instance = Patient.objects.get(pk=patient)
			p = Prescription.objects.create(date=form.cleaned_data['date'], 
				patient=patient_instance, 
				medication=Medication.objects.get(pk = request.POST.get("medication", "")),
				dosage=form.cleaned_data['dosage'],
				quantity=form.cleaned_data['quantity'],
				doctor=request.user)
			return render(request, 'prescriptions/prescribe_form.html', {
        'form': form,
    })

		else:
			return render(request, 'prescriptions/prescribe_form.html', {
        'form': form,})
			
	data = {'patient': Patient.objects.get(pk=patient), 'doctor': request.user}
	form = PrescribeForm(initial=data)

	def get_success_url(self):
		pk = self.object.pk
		return '/prescriptions/' + str(pk) + '/'

	return render(request, 'prescriptions/prescribe_form.html', {
        'form': form,
    })

class EditPrescriptionView(UpdateView):
	model = Prescription
	form_class = EditPrescriptionForm
	template_name = 'prescriptions/edit_prescription_form.html'

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