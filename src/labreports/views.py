from django.shortcuts import render
from .models import LabReport
from django.views.generic import CreateView, UpdateView, DetailView, ListView

# Create your views here.
class LabReportDetails(DetailView):
	model = LabReport
	template_name = 'labreports/details.html'
	def get_context_data(self, **kwargs):
		context = super(LabReportDetails, self).get_context_data(**kwargs)
		return context