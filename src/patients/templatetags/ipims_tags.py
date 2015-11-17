from django import template 
from django.contrib.auth.models import Group 
from appointments.models import HealthCondition

register = template.Library() 

@register.filter(name='has_group') 
def has_group(user, group_name): 
	group = Group.objects.get(name=group_name)
	return True if group in user.groups.all() else False

@register.filter(name='by_id') 
def has_group(user, hc_pk):
	health_condition = Group.objects.get(pk=hc_pk)
	return health_condition

@register.filter(name='get_class')
def get_class(value):
	""" Return class name of object passed in from template """
	return value.__class__.__name__