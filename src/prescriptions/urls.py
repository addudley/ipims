from django.conf.urls import include, url
from django.contrib import admin
from prescriptions import views
from django.core.urlresolvers import reverse

from django.contrib.auth.decorators import login_required

urlpatterns = [
	url(r'^prescribe/(?P<patient>[0-9]+)/$',
		login_required(views.prescribe), name='prescribe_form'),
	url(r'^(?P<pk>[0-9]+)/$',
		login_required(views.PrescriptionDetailsView.as_view()), name='prescription_details'),
	url(r'^(?P<pk>[0-9]+)/edit/$',
		login_required(views.EditPrescriptionView.as_view()), name='edit_prescription'),
		url(r'^(?P<id>\d+)/delete', login_required(views.delete)),
		url(r'^(?P<id>\d+)/fill', login_required(views.fill)),
]