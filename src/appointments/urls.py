from django.conf.urls import include, url
from django.contrib import admin

from appointments import views

urlpatterns = [
	url(r'^add/$', 
    	views.ScheduleAppointment.as_view(success_url="/"), name='schedule_appointment_form'),
	url(r'^emergency/$', 
    	views.EmergencyAppointment.as_view(success_url="/"), name='emergency_form'),
	url(r'^(?P<pk>[0-9]+)/$',
		views.AppointmentDetails.as_view(),name='appointment_details'),
	url(r'^$', views.AppointmentListView.as_view(), name='appointment-list'),
]