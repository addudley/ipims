from django.shortcuts import render
from patients.models import Patient

from .analysis_funcs import PatientData, AdmissionData, HealthOutcomesData

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
	###################################
	#       Patient Info Pie Charts
	###################################
	data = PatientData.check_patient_data() # returns patient data
	total_patients = data['total']
	admission_data = AdmissionData.check_admission_data()
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
	title = [{"text": 'Sex'}, {"text": 'Ethnicity'}, {"text": 'Age group'}]

	###################################
	#      Admission Line Chart
	###################################
	admission_csv = AdmissionData.check_admission_data()
	admission_series = [{"name": 'Admissions', "data" : admission_csv}]

	###################################
	#       Line Chart
	###################################
	health_outcomes_data = HealthOutcomesData.check_health_outcomes_data() # returns patient data
	# Require one entry in series list for each graph
	health_outcomes_series = [
	{"name": 'Overall Health Outcomes', "data" : health_outcomes_data['overall']},
		]

	health_outcomes_series_length = len(health_outcomes_series) # length of series - used to iteratively create divs and jQuery in analysis template 

	# Generate a chartID for each chart in series
	# Used as div id / jQuery selector in analysis template
	health_outcomes_chartID = [] 
	for i in range(0, health_outcomes_series_length):
		health_outcomes_chartID.append("health_outcomes_chart_" + str(i))

	# Generate a chart for each chart in series
	# Used as a field in highcharts
	health_outcomes_chart = []
	for i in range(0, health_outcomes_series_length):
		health_outcomes_chart.append({"renderTo": health_outcomes_chartID[i], "type": chart_type})

	# List of titles for each chart
	health_outcomes_title = [{"text": 'Overall'}]


	###################################
	#    Return data to template
	###################################
	return render(request, 'stats/analysis.html', 
							{'chartID': chartID, 
							'series_length': series_length, 
							'chart': chart, 
							'series': series, 
							'title': title, 

							'admission_csv': admission_csv,
							'total_patients': total_patients,

							'health_outcomes_chartID': health_outcomes_chartID,
							'health_outcomes_chart': health_outcomes_chart,
							'health_outcomes_series_length': health_outcomes_series_length,
							'health_outcomes_series': health_outcomes_series,
							'health_outcomes_title': health_outcomes_title

							})