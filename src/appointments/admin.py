from django.contrib import admin
from .models import HealthCondition, Emergency

# Register your models here.
admin.site.register(HealthCondition)
admin.site.register(Emergency)