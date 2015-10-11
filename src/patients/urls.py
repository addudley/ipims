   
from django.conf.urls import include, url
from django.contrib import admin
from patients import views

urlpatterns = [
	url(r'^(?P<pk>[0-9]+)/$',
        views.patientProfile,
        name='patient_profile'),
    url(r'^(?P<pk>[0-9]+)/update/$',
    	views.PatientUpdate.as_view(success_url="/"), name='patient_update_form'),
    url(r'^add/$', 
    	views.PatientNew.as_view(success_url="/"), name='patient_registration_form'),
]