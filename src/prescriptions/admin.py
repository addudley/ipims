from django.contrib import admin
from .models import Medication, Prescription


# Register your models here.
admin.site.register(Medication)
admin.site.register(Prescription)