from django.shortcuts import render
from patients.models import Patient

from .analysis_funcs import ChartData

# Create your views here.
def statisticalAnalysis(request):
	patients = Patient.objects.all()
	context = {'values': [['Male', 0], ['Female', 0]]}
	for patient in patients:
		if patient.sex == patient.MALE:
			context['values'][0][1] += 1
		else:
			context['values'][1][1] += 1
	return render(request, 'stats/statistical_analysis_report.html', context)

###################################################
#       plot(): generates data for highcharts
###################################################
def plot(request, chart_type='pie'):

	data = ChartData.check_patient_data() # returns patient data
	
	# Require one entry in series list for each graph
	series = [
	{"name": 'Sex', "data" : data['sex']},
	{"name": 'Ethnicity', "data" : data['ethnicity']},
	{"name": 'Age group', "data" : data['age_group']}
	]

	series_length = len(series) # length of series - used to iteratively create divs and jQuery in analysis template 

	# Generate a chartID for each chart in series
	# Used as div id / jQuery selector in analysis template
	chartID = [] 
	for i in range(0, series_length):
		chartID.append("chart_" + str(i))

	# Generate a chart for each chart in series
	# Used as a field in highcharts
	chart = []
	for i in range(0, series_length):
		chart.append({"renderTo": chartID[i], "type": chart_type})

	# List of titles for each chart
	title = [{"text": 'Male vs Female'}, {"text": 'Ethnicity'}, {"text": 'Age group'}]


	return render(request, 'stats/analysis.html', {'chartID': chartID, 'series_length': series_length, 'chart': chart, 'series': series, 'title': title})

