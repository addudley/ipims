from django.test import TestCase
from patients.models import Patient

class PatientTestCase_2(TestCase):
	def test_setUp(self):
	        Patient.objects.create(first_name="Andrew", 
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



    # def test_animals_can_speak(self):
    #     """Animals that can speak are correctly identified"""
    #     lion = Animal.objects.get(name="lion")
    #     cat = Animal.objects.get(name="cat")
    #     self.assertEqual(lion.speak(), 'The lion says "roar"')
    #     self.assertEqual(cat.speak(), 'The cat says "meow"')