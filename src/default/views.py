from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
import datetime
from pytz import timezone

from patients.models import Patient
from appointments.models import Appointment, Emergency
from records.models import Record
# Create your views here.

@login_required(login_url='/accounts/login/')
def home(request):
	u = request.user
	if u.groups.filter(name='lab_technician').exists():
		return HttpResponseRedirect('labs/dashboard/')
	elif u.groups.filter(name='doctor').exists():
		return HttpResponseRedirect('dashboard/')
	elif u.groups.filter(name='pharmacist').exists() or u.groups.filter(name='nurse').exists():
		return HttpResponseRedirect('/search/')
	elif u.groups.filter(name='staff').exists():
		return HttpResponseRedirect('/search/')
	else:
		return render(request, 'base.html', {})

@login_required(login_url='/accounts/login/')
def doctorDashboard(request):
	u = request.user
	if u.groups.filter(name='doctor').exists():
		# Get list of appointments for current doctor
		appointments = Appointment.objects.filter(doctor=request.user.pk).order_by('date').reverse()
		emergencies = Emergency.objects.filter(doctor=request.user.pk)
		
		appointments_today = [] # list of today's appointments
		patients = [] # list of patients who have had appointments with current doctor
		records = Record.objects.filter(doctor=request.user.pk, date_created__gte=datetime.datetime.today().date() - datetime.timedelta(days=7)).order_by('date_created').reverse()
		for appointment in appointments:
			if appointment.date.date() == datetime.datetime.now().date():
				# populate list for todays appointments
				appointments_today.insert(0, appointment)
			if appointment.patient not in patients:
				# populate list of doctor's patients
				patients.append(appointment.patient)

		for emergency in emergencies:
			if emergency.patient not in patients:
				# poplate list of er doctor's patients
				patients.append(emergency.patient)

		# load notifications
		notifications = u.notifications

		context = {'appointments':appointments, 
					'appointments_today':appointments_today, 
					'patients':patients, 
					'records':records,
					'notifications': notifications}
		return render(request, 'default/doctor_dashboard.html', context)
	else:
		return render(request, 'access_denied.html', {})