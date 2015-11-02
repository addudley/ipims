from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from .models import LabReport, LabTest
from patients.models import Patient
from django.views.generic import CreateView, UpdateView, DetailView, ListView
import datetime

from .forms import *

# Create your views here.
class LabReportDetails(DetailView):
	model = LabReport
	template_name = 'labreports/details.html'
	def get_context_data(self, **kwargs):
		context = super(LabReportDetails, self).get_context_data(**kwargs)
		return context

def requestLab(request, patient):

	if request.method == 'POST':
		form = RequestLabForm(request.POST)

		if form.is_valid():
			patient_instance = Patient.objects.get(pk=patient)
			lab_report = LabReport.objects.create(
				request_date=form.cleaned_data['request_date'], 
				doctor=request.user,
				patient=patient_instance, 
				lab_test=LabTest.objects.get(pk = request.POST.get("lab_test", "")),
				status='r',
				doctor_notes=form.cleaned_data['doctor_notes'],
				)
			return HttpResponseRedirect('/labs/' + str(lab_report.pk) )

		else:
			return render(request, 'labreports/request_lab_form.html', {
		'form': form,})
			
	data = {'patient': Patient.objects.get(pk=patient), 
			'doctor': request.user, 
			'request_date': datetime.datetime.now()}
	form = RequestLabForm(initial=data)


	return render(request, 'labreports/request_lab_form.html', {
		'form': form,
		'patient': Patient.objects.get(pk=patient)
	})

class EditLabRequestView(UpdateView):
	model = LabReport
	form_class = EditLabRequestForm
	template_name = 'labreports/edit_lab_request.html'

	def form_valid(self, form):
		self.object = form.save()
		return HttpResponseRedirect(self.get_success_url())

	def get_success_url(self):
		pk = self.object.pk
		return '/labs/' + str(pk) + '/'

class UpdateLabReportView(UpdateView):
	model = LabReport
	form_class = UpdateLabReportForm
	template_name = 'labreports/update_lab_report.html'

	def form_valid(self, form):
		self.object = form.save()
		return HttpResponseRedirect(self.get_success_url())

	def get_success_url(self):
		pk = self.object.pk
		return '/labs/' + str(pk) + '/'

def delete(request, pk):
	lab_report = get_object_or_404(LabReport, pk=pk)
	patient_pk = lab_report.patient.pk
	lab_report.delete()
	return HttpResponseRedirect('/patient/' + str(patient_pk))