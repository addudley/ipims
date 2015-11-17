from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.auth.decorators import login_required

from appointments import views

urlpatterns = [
	# Add Appointment
	url(r'^add/(?P<patient_pk>[0-9]+)/$', 
    	login_required(views.scheduleAppointment), name='schedule_appointment_form'),

	# Edit Appointment 
	url(r'^(?P<pk>[0-9]+)/edit', 
    	login_required(views.EditAppointment.as_view(success_url="/")), name='schedule_appointment_form'),

	# Add Emergency appointment
	url(r'^emergency/(?P<patient_pk>[0-9]+)/$', 
    	login_required(views.emergencyAppointment), name='emergency_form'),
	# Emergency notification sent successfully
	url(r'^emergency/success/(?P<pk>[0-9]+)/$', 
    	login_required(views.emergencyNotificationSent), name='emergency_notification_sent'),
	# Appointment Details
	url(r'^(?P<pk>[0-9]+)/$',
		login_required(views.AppointmentDetails.as_view()),name='appointment_details'),

	# Obsolete - AppointmentListView
	# url(r'^$', login_required(views.AppointmentListView.as_view()), name='appointment-list'),

	#Delete Patient 
	#SCHEDULED FOR REMOVAL - NOT USED
	url(r'^(?P<id>\d+)/delete', login_required(views.delete)),
]