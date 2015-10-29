from django.conf.urls import include, url
from django.contrib import admin
from labreports import views
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required

urlpatterns = [
	url(r'^(?P<pk>[0-9]+)/$',
		login_required(views.LabReportDetails.as_view()),
		name='lab_report_details'),
	# url(r'^(?P<pk>[0-9]+)/update/$',
	# 	login_required(views.PatientUpdate.as_view()), name='patient_update_form'),
	# url(r'^add/$', 
	# 	login_required(views.PatientNew.as_view(success_url="/")), name='patient_registration_form'),
	# url(r'^(?P<pk>[0-9]+)/health/$',
	# 	login_required(views.CurrentHealthCondition.as_view()), name='patient_health_condition_form'),
]