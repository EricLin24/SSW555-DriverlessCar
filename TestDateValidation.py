# Test file for DateValidation.py module

import DateValidation
from datetime import date



def test_validateDate():
	valid = date(1990, 4, 21)
	invalid_year = date(2020, 10, 10)
	invalid_month = date(2019, 10, 24)
	invalid_day = date(2019, 2, 28)

	
	try:
		# Valid
		if DateValidation.validateDate(valid):
			print(str(valid) + ' is a valid date')
			try:
				# Invalid year
				if DateValidation.validateDate(invalid_year):
					print(str(invalid_year) + ' should not be valid (something is wrong)')
			except Exception as e:
				print(str(e))
			finally:
				try:
					# Invalid month
					if DateValidation.validateDate(invalid_month):
						print(str(invalid_month) + ' should not be valid (something is wrong)')
				except Exception as e:
					print(str(e))
				finally:
					try:
						# Invalid day
						if DateValidation.validateDate(invalid_day):
							print(str(invalid_day) + ' should not be valid (something is wrong)')
					except Exception as e:
						print(str(e))
	except Exception as e:
		print(str(e))


def test_validateMarraigeDate():
	validBirthdate = date(1990, 12, 28)
	validMarraigeDate = date(2019, 1, 1)
	invalidMarraigeDate_year = date(1919, 3, 21)
	invalidMarraigeDate_month = date(1990, 11, 21)
	invalidMarraigeDate_day = date(1990, 12, 21)

	
	try:
		# Valid
		if DateValidation.validateMarraigeDate(validBirthdate, validMarraigeDate):
			print 'Marraige date: ' + str(validMarraigeDate) + ' is valid'
		
		# Invalid year
		try:
			if DateValidation.validateMarraigeDate(validBirthdate, invalidMarraigeDate_year):
				print 'Marraige date: ' + str(invalidMarraigeDate_year) + ' should not be valid (something is wrong)'
		
		except Exception as e:
			print str(e)
		
		finally:
			# Invalid month
			try:
				if DateValidation.validateMarraigeDate(validBirthdate, invalidMarraigeDate_month):
					print 'Marraige date: ' + str(invalidMarraigeDate_month) + ' should not be valid (something is wrong)'
		
			except Exception as e:
				print str(e)

			finally:
				#Invalid day
				try:
					if DateValidation.validateMarraigeDate(validBirthdate, invalidMarraigeDate_day):
						print 'Marraige date: ' + str(invalidMarraigeDate_day) + ' should not be valid (something is wrong)'

				except Exception as e:
					print str(e)
	except Exception as e:
		print str(e)

def test_validate_birth_before_death():
	valid_birth = date(1994, 3 ,21)
	invalid_year = date(1993, 3, 21)
	invalid_month = date(1994, 2, 21)
	invalid_day =  date(1994, 3, 20)
	valid_death = date(2011, 5, 11)



test_validateDate()
test_validateMarraigeDate()
