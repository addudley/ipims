from django.test import TestCase
from patients.models import Patient
from django.test.utils import override_settings
import haystack
from django.core.management import call_command
from haystack.query import SearchQuerySet

#Define Test Index for ElasticSearch test cases
TEST_INDEX = {
	'default': {
		'ENGINE': 'haystack.backends.elasticsearch_backend.ElasticsearchSearchEngine',
		'URL': 'http://127.0.0.1:9200/',
		'TIMEOUT': 60 * 10,
		'INDEX_NAME': 'test_index',
	},
}

class CreatePatientDBEntryTestCase(TestCase):
	def test_setUp(self):
			patient = Patient.objects.create(first_name="Andrew", 
								last_name="Dudley", 
								dob="1989-02-22", 
								ssn="101-11-1010", 
								phone_number="623-910-0586",
								email = "addudley@asu.edu",
								address = "2027 E University Dr",
								city = "tempe",
								state = "Arizona",
								zip_code = 85281,

								health_insurance_provider="Aetna",
								health_insurance_id="XBH105 15014-40")
			patient.save()

class CreatePatientViewTestCase(TestCase):
	def test_create_patient_view(self):
		resp = self.client.get('/patient/add/')
		self.assertEqual(resp.status_code, 200)

class PatientProfileViewTestCase(TestCase):
	fixtures = ['patients_testdata.json']
	def test_patient_profile_view(self):
		resp = self.client.get('/patient/1/')
		self.assertEqual(resp.status_code, 200)
		patient = resp.context['patient']
		self.assertEqual(patient.id, 1)

class PatientFullNameTestCase(TestCase):
	fixtures = ['patients_testdata.json']
	def test_patient_profile_view(self):
		resp = self.client.get('/patient/1/')
		self.assertEqual(resp.status_code, 200)
		patient = resp.context['patient']
		self.assertEqual(patient.get_full_name(), patient.last_name + ', ' + patient.first_name)

class PatientUpdateCurrentHealthConditionsViewTestCase(TestCase):
	fixtures = ['patients_testdata.json']
	def test_current_health_condition(self):
		resp = self.client.get('/patient/1/health/')
		self.assertEqual(resp.status_code, 200)

@override_settings(HAYSTACK_CONNECTIONS=TEST_INDEX)
class PatientSearchViewTestCase(TestCase):
	#fixtures = ['patients_testdata.json']
	def setUp(self):
		haystack.connections.reload('default')
		super(PatientSearchViewTestCase, self).setUp()

	def test_search_view(self):
		resp = self.client.get('/search/')
		self.assertEqual(resp.status_code, 200)

	def test_search_query_view(self):
		resp = self.client.get('/search/?q=sarah')
		self.assertEqual(resp.status_code, 200)

		# Test Search Query
		self.sqs = SearchQuerySet()
		self.assertEqual(self.sqs.auto_query('sarah').count(), 1)

	def tearDown(self):
		call_command('clear_index', interactive=False, verbosity=0)