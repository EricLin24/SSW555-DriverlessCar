# Test file for DateValidation.py module

import DateValidation
import unittest
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
			print('Marraige date: ' + str(validMarraigeDate) + ' is valid')

		# Invalid year
		try:
			if DateValidation.validateMarraigeDate(validBirthdate, invalidMarraigeDate_year):
				print('Marraige date: ' + str(invalidMarraigeDate_year) + ' should not be valid (something is wrong)')

		except Exception as e:
			print(str(e))

		finally:
			# Invalid month
			try:
				if DateValidation.validateMarraigeDate(validBirthdate, invalidMarraigeDate_month):
					print('Marraige date: ' + str(invalidMarraigeDate_month) + ' should not be valid (something is wrong)')

			except Exception as e:
				print(str(e))

			finally:
				#Invalid day
				try:
					if DateValidation.validateMarraigeDate(validBirthdate, invalidMarraigeDate_day):
						print('Marraige date: ' + str(invalidMarraigeDate_day) + ' should not be valid (something is wrong)')

				except Exception as e:
					print(str(e))
	except Exception as e:
		print(str(e))

class TestDateValidation(unittest.TestCase):
    #Testcases of US03
    def test_validate_birth_before_death_year(self):
        birth = date(1955, 2, 3)
        invalid_death = date(1954, 2, 3)
        self.assertEqual(DateValidation.validate_birth_before_death(birth, invalid_death), False,
                         msg='should be False, year error.')

    def test_validate_birth_before_death_month(self):
        birth = date(1995, 2, 3)
        invalid_death = date(1955, 1, 3)
        self.assertEqual(DateValidation.validate_birth_before_death(birth, invalid_death), False,
                         msg='should be False, month error')

    def test_validate_birth_before_death_day(self):
        birth = date(1995, 2, 3)
        invalid_death = date(1955, 2, 2)
        self.assertEqual(DateValidation.validate_birth_before_death(birth, invalid_death), False,
                         msg='should be False, day error')

    def test_validate_birth_before_death_valid(self):
        birth = date(1995, 2, 3)
        valid_death = date(2011, 11, 19)
        self.assertEqual(DateValidation.validate_birth_before_death(birth, valid_death), True, msg='correct')

    #Testcases of US04
    def test_validate_marraige_before_divorce_year(self):
        marraige = date(2001, 2, 14)
        invalid_divorce = date(2000, 2, 14)
        self.assertEqual(DateValidation.validate_marraige_before_divorce(marraige, invalid_divorce), False, msg='should be False, year error')

    def test_validate_marraige_before_divorce_month(self):
        marraige = date(2001, 2, 14)
        invalid_divorce = date(2001, 1, 14)
        self.assertEqual(DateValidation.validate_marraige_before_divorce(marraige, invalid_divorce), False,
                         msg='should be False, month error')

    def test_validate_marraige_before_divorce_day(self):
        marraige = date(2001, 2, 14)
        invalid_divorce = date(2001, 2, 13)
        self.assertEqual(DateValidation.validate_marraige_before_divorce(marraige, invalid_divorce), False,
                         msg='should be False, day error')

    def test_validate_marraige_before_divorce_valid(self):
        marraige = date(2001, 2, 14)
        valid_divorce = date(2013, 7, 9)
        self.assertEqual(DateValidation.validate_marraige_before_divorce(marraige, valid_divorce), True, msg='correct')

if __name__ == '__main__':
    #test_validateDate()
    #test_validateMarraigeDate()
    unittest.main()


