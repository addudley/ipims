from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from .models import LabReport, LabTest
from patients.models import Patient
from django.contrib.auth.models import User
from django.views.generic import CreateView, UpdateView, DetailView, ListView
from notifications import notify
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
		form.instance.lab_technician = self.request.user
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
		form.instance.update_date = datetime.datetime.now().date().isoformat()
		form.instance.lab_technician = self.request.user
		self.object = form.save()
		print(self.object.doctor)
		if self.object.status == 'c':
			notify.send(self.request.user, recipient=self.object.doctor, verb='%s\'s %s lab report is ready!' % (self.object.patient.get_full_name(), self.object.lab_test), level='success')

		return HttpResponseRedirect(self.get_success_url())

	def get_success_url(self):
		pk = self.object.pk
		return '/labs/' + str(pk) + '/'

def delete(request, pk):
	lab_report = get_object_or_404(LabReport, pk=pk)
	patient_pk = lab_report.patient.pk
	lab_report.delete()
	return HttpResponseRedirect('/patient/' + str(patient_pk))

def labDashboard(request):
	lab_reports_in_progress = LabReport.objects.filter(status='ip').order_by('update_date').reverse()
	lab_reports_requested = LabReport.objects.filter(status='r').order_by('request_date')
	lab_reports_completed = LabReport.objects.filter(status='c').order_by('update_date').reverse()
	context = {'lab_reports_in_progress': lab_reports_in_progress, 
				'lab_reports_requested': lab_reports_requested,
				'lab_reports_completed': lab_reports_completed}
	return render(request, 'labreports/lab_dashboard.html', context)