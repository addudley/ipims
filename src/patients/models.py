from django.db import models

# Create your models here.
from django.utils.translation import ugettext as _
from localflavor.us.models import USStateField
from localflavor.us.models import PhoneNumberField

class MedicalBackgroundChoice(models.Model):
	description = models.CharField(max_length=128)
	def __str__(self):
		return self.description

class Allergy(models.Model):
	description = models.CharField(max_length=128)
	def __str__(self):
		return self.description

class Patient(models.Model):

	# Patient Sex Constants
	MALE = 'm'
	FEMALE = 'f'
	SEX_CHOICES = ((MALE, 'Male'), (FEMALE, 'Female'))

	# Patient Ethnicity Constansts
	WHITE = 'wh'
	BLACK = 'bl'
	NATIVE_AMERICAN = 'na'
	HISPANIC = 'hi'
	ASIAN = 'as'
	OTHER = 'o'
	ETHNICITY_CHOICES = ((WHITE, 'White'), 
						(BLACK, 'Black'), 
						(NATIVE_AMERICAN, 'Native American'), 
						(HISPANIC, 'Hispanic'),
						(ASIAN, 'Asian'),
						(OTHER, 'Other'))

	profile_picture = models.ImageField(upload_to = 'images/', blank=True, null=True)

	first_name = models.CharField(max_length = 30)
	last_name = models.CharField(max_length = 30)
	dob = models.DateField()
	sex = models.CharField(max_length=1, choices=SEX_CHOICES)
	ethnicity = models.CharField(max_length=2, choices=ETHNICITY_CHOICES)
	ssn = models.CharField(max_length = 11)
	phone_number = PhoneNumberField(default = 'null')
	email = models.EmailField(default = 'null')

	# Address Info
	address = models.CharField(max_length = 128)
	city = models.CharField(max_length=64)
	state = USStateField()
	zip_code = models.PositiveIntegerField()

	# Health Insurance
	health_insurance_provider = models.CharField(max_length = 64)
	health_insurance_id = models.CharField(max_length = 30)

	# Medical History
	medical_background_information = models.ManyToManyField(MedicalBackgroundChoice, blank=True)
	allergies = models.ManyToManyField(Allergy, blank=True)

	def get_full_name(self):
		# returns the patient's full name (ex: Doe, John)
		return '%s, %s' % (self.last_name, self.first_name)

	def get_ssn(self):
		return 'xxx-xx' + self.ssn[6:]

	DISCOMFORT_LEVELS = (('1', '1'),('2', '2'),('3', '3'),('4', '4'),('5', '5'),('6', '6'),('7', '7'),('8', '8'),('9', '9'),('10', '10'))
	nausea_level = models.CharField(max_length=2, choices=DISCOMFORT_LEVELS, default=1, verbose_name='Nausea')
	headache_level = models.CharField(max_length=2, choices=DISCOMFORT_LEVELS, default=1, verbose_name='Headache')
	sore_throat_level = models.CharField(max_length=2, choices=DISCOMFORT_LEVELS, default=1, verbose_name='Sore throat')
	abdominal_pain_level = models.CharField(max_length=2, choices=DISCOMFORT_LEVELS, default=1, verbose_name='Abdominal pain')
	constipation_level = models.CharField(max_length=2, choices=DISCOMFORT_LEVELS, default=1, verbose_name='Constipation')
	lack_of_appetite_level = models.CharField(max_length=2, choices=DISCOMFORT_LEVELS, default=1, verbose_name='Lack of appetite')
	sleepiness_level = models.CharField(max_length=2, choices=DISCOMFORT_LEVELS, default=1, verbose_name='Sleepiness')
	insomnia_level = models.CharField(max_length=2, choices=DISCOMFORT_LEVELS, default=1, verbose_name='Insomnia')
	
	def __str__(self):
		return self.get_full_name()
