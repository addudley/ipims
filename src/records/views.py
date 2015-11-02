from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.views.generic import CreateView, UpdateView, DetailView
import datetime

from appointments.models import HealthCondition
from patients.models import Patient
from django.contrib.auth.models import User
from .models import Record


# Create your views here.
def addRecord(request, patient):
	if request.method == 'POST':
		form = AddRecordForm(request.POST)

		if form.is_valid():
			patient_instance = Patient.objects.get(pk=patient)
			record = LabReport.objects.create(
				date_created=datetime.datetime.now(),
				patient=patient_instance, 
				doctor=request.user,
				health_condition=HealthCondition.objects.get(pk = request.POST.get("health_condition", "")),
				notes = form.cleaned_data['notes'],
				status = form.cleaned_data['status']
				)
			return HttpResponseRedirect('/records/' + str(record.pk) )

		else:
			return render(request, 'records/add_record_form.html', {
		'form': form,})
			
	data = {'patient': Patient.objects.get(pk=patient), 
			'doctor': request.user, 
			'date_created': datetime.datetime.now()}
	form = RequestLabForm(initial=data)

class RecordDetails(DetailView):
	model = Record
	template_name = 'records/details.html'
	def get_context_data(self, **kwargs):
		context = super(RecordDetails, self).get_context_data(**kwargs)
		return context