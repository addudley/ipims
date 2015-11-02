from django.conf.urls import include, url
from django.contrib.auth.decorators import login_required

from records import views

urlpatterns = [
	url(r'^(?P<pk>[0-9]+)/$',
		login_required(views.RecordDetails.as_view()),
		name='record_details'),
	# url(r'^add/(?P<patient>[0-9]+)/$', 
	# 	login_required(views.requestLab), name='request_lab_form'),
	# url(r'^(?P<pk>[0-9]+)/delete/$',
	# 	login_required(views.delete), name="delete_lab_report"),
	# url(r'^(?P<pk>[0-9]+)/edit/$',
	# 	login_required(views.EditLabRequestView.as_view()), name="edit_lab_request"),
	# url(r'^(?P<pk>[0-9]+)/update/$',
	# 	login_required(views.UpdateLabReportView.as_view()), name="update_lab_report")
	# url(r'^(?P<pk>[0-9]+)/health/$',
	# 	login_required(views.CurrentHealthCondition.as_view()), name='patient_health_condition_form'),
]