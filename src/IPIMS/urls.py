"""IPIMS URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""

from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.auth.decorators import login_required
# Haystack Search
from haystack.forms import SearchForm
from haystack.views import SearchView

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'default.views.home', name='home'),
    url(r'^dashboard/$', 'default.views.doctorDashboard', name='doctordashboard'),
    url(r'^accounts/', include('registration.backends.simple.urls')),
    url(r'^patient/', include('patients.urls')),
    url(r'^search/', login_required(SearchView(form_class=SearchForm))),
    url(r'^appointments/', include('appointments.urls')),
    url(r'^inbox/notifications/', include('notifications.urls', namespace="notifications")),
    url(r'^prescriptions/', include('prescriptions.urls', namespace="prescriptions")),
    url(r'^stats/', 'stats.views.statisticalAnalysis'),
    url(r'^hc/', 'stats.views.plot'),
    url(r'^labs/', include('labreports.urls', namespace = "labreports")),
    url(r'^records/', include('records.urls', namespace="records")),
]