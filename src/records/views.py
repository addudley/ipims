from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.views.generic import CreateView, UpdateView, DetailView
import datetime

from appointments.models import HealthCondition
from patients.models import Patient
from django.contrib.auth.models import User
from .models import Record
from .forms import AddRecordForm, UpdateRecordForm


# Create your views here.
def addRecord(request, patient):
	if request.method == 'POST':
		form = AddRecordForm(request.POST)

		if form.is_valid():
			patient_instance = Patient.objects.get(pk=patient)
			record = Record.objects.create(
				date_created=datetime.datetime.now(),
				patient=patient_instance, 
				doctor=request.user,
				health_condition=HealthCondition.objects.get(pk = request.POST.get("health_condition", "")),
				notes = form.cleaned_data['notes'],
				resolved = form.cleaned_data['resolved']
				)
			return HttpResponseRedirect('/records/' + str(record.pk) )

		else:
			return render(request, 'records/add_record_form.html', {
		'form': form,})
			
	data = {'patient': Patient.objects.get(pk=patient), 
			'doctor': request.user, 
			'date_created': datetime.datetime.now(),
			'resolved': False}
	form = AddRecordForm(initial=data)

	return render(request, 'records/add_record_form.html', {
		'form': form,
		'patient': Patient.objects.get(pk=patient)
	})


class RecordDetails(DetailView):
	model = Record
	template_name = 'records/details.html'
	def get_context_data(self, **kwargs):
		context = super(RecordDetails, self).get_context_data(**kwargs)
		return context

class UpdateRecordView(UpdateView):
	model = Record
	form_class = UpdateRecordForm
	template_name = 'records/update_record_form.html'

	def form_valid(self, form):
		self.object = form.save()
		return HttpResponseRedirect(self.get_success_url())

	def get_success_url(self):
		pk = self.object.pk
		return '/records/' + str(pk) + '/'