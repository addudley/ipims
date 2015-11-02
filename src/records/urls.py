from django.conf.urls import include, url
from django.contrib.auth.decorators import login_required

from records import views

urlpatterns = [
	url(r'^(?P<pk>[0-9]+)/$',
		login_required(views.RecordDetails.as_view()),
		name='record_details'),
	url(r'^add/(?P<patient>[0-9]+)/$', 
		login_required(views.addRecord), name='add_record_form'),
	# url(r'^(?P<pk>[0-9]+)/delete/$',
	# 	login_required(views.delete), name="delete_lab_report"),
	url(r'^(?P<pk>[0-9]+)/update/$',
		login_required(views.UpdateRecordView.as_view()), name="update_record"),
	# url(r'^(?P<pk>[0-9]+)/update/$',
	# 	login_required(views.UpdateLabReportView.as_view()), name="update_lab_report")
	# url(r'^(?P<pk>[0-9]+)/health/$',
	# 	login_required(views.CurrentHealthCondition.as_view()), name='patient_health_condition_form'),
]