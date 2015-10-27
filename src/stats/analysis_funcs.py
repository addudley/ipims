from patients.models import Patient
from datetime import date


class ChartData(object):
	def check_patient_data():
		data = {'sex': [['Male', 0], ['Female', 0]],
				'ethnicity': [['White', 0], 
								['Black', 0], 
								['Native American', 0], 
								['Hispanic', 0], 
								['Asian', 0], 
								['Other', 0]],
				'age_group': [['0-9', 0], 
								['10-19', 0],
								['20-29', 0],
								['30-39', 0],
								['40-49', 0],
								['50-59', 0],
								['60-69', 0],
								['70-79', 0],
								['80-89', 0],
								['90+', 0]]
								}

		patients = Patient.objects.all()

		for patient in patients:
			# Count number of males and females
			if patient.sex == patient.MALE:
				data['sex'][0][1] += 1
			else:
				data['sex'][1][1] += 1

			# Count ethnic groups
			ethnicity = patient.get_ethnicity_display()
			count = 0
			flag = 0
			for item in data['ethnicity']:
				if ethnicity not in item:
					count += 1
				else:
					flag = 1
					break
			if flag == 1:
				index = count
				data['ethnicity'][index][1] += 1

			# Count age groups
			age = calculate_age(patient.dob)
			if age <= 9:
				data['age_group'][0][1] += 1
			elif age <= 19:
				data['age_group'][1][1] += 1
			elif age <= 29:
				data['age_group'][2][1] += 1
			elif age <= 39:
				data['age_group'][3][1] += 1
			elif age <= 49:
				data['age_group'][4][1] += 1
			elif age <= 59:
				data['age_group'][5][1] += 1
			elif age <= 69:
				data['age_group'][6][1] += 1
			elif age <= 79:
				data['age_group'][7][1] += 1
			elif age <= 89:
				data['age_group'][8][1] += 1
			else:
				data['age_group'][9][1] += 1
		return data

def calculate_age(born):
    today = date.today()
    return today.year - born.year - ((today.month, today.day) < (born.month, born.day))

