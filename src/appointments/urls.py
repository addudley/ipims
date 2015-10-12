from django.conf.urls import include, url
from django.contrib import admin

from appointments import views

urlpatterns = [
	url(r'^add/$', 
    	views.ScheduleAppointment.as_view(success_url="/"), name='patient_registration_form'),
	url(r'^chaining/', include('smart_selects.urls')),
]