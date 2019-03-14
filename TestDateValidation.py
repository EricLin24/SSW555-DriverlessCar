# Test file for DateValidation.py module

import DateValidation
import unittest
from datetime import date

class TestDateValidation(unittest.TestCase):

    # Test Cases US01
    def test_validateDate_valid(self):
        valid_date = date(1990, 4, 21)
        self.assertEqual(DateValidation.validateDate(valid_date), True, msg='Date is valid')

    def test_validateDate_invalid_year(self):
        invalid_year = date(2020, 10, 10)
        self.assertEqual(DateValidation.validateDate(invalid_year), False, msg='Date should be invalid: year error')

    def test_validateDate_invalid_month(self):
        invalid_month = date(2019, 10, 24)
        self.assertEqual(DateValidation.validateDate(invalid_month), False, msg='Date should be invalid: month error')

    def test_validateDate_invalid_day(self):
        invalid_day = date(2019, 3, 28)
        self.assertEqual(DateValidation.validateDate(invalid_day), False, msg='Date should be invalid: day error')

    # Test Cases US02
    def test_validateMarraigeDate_valid(self):
        validBirthdate = date(1990, 12, 28)
        validMarraigeDate = date(2019, 1, 1)
        self.assertEqual(DateValidation.validateMarraigeDate(validBirthdate, validMarraigeDate), True, msg='Valid: marraige date after birthdate')

    def test_validateMarraigeDate_invalid_year(self):
        validBirthdate = date(1990, 12, 28)
        invalidMarraigeDate_year = date(1919, 3, 21)
        self.assertEqual(DateValidation.validateMarraigeDate(validBirthdate, invalidMarraigeDate_year), False, msg='Marraige date should be invalid: year error')

    def test_validateMarraigeDate_invalid_month(self):
        validBirthdate = date(1990, 12, 28)
        invalidMarraigeDate_month = date(1990, 11, 21)
        self.assertEqual(DateValidation.validateMarraigeDate(validBirthdate, invalidMarraigeDate_month), False, msg='Marraige date should be invalid: month error')

    def test_validateMarraigeDate_invalid_day(self):
        validBirthdate = date(1990, 12, 28)
        invalidMarraigeDate_day = date(1990, 12, 21)
        self.assertEqual(DateValidation.validateMarraigeDate(validBirthdate, invalidMarraigeDate_day), False, msg='Marraige date should be invalid: day error')

    #Testcases of US03
    def test_validate_birth_before_death_year(self):
        birth = date(1955, 2, 3)
        invalid_death = date(1954, 2, 3)
        valid_death = date(1956, 2, 3)
        self.assertEqual(DateValidation.validate_birth_before_death(birth, invalid_death), False,
                         msg='should be False, year error.')
        self.assertEqual(DateValidation.validate_birth_before_death(birth, valid_death), True, msg='correct')

    def test_validate_birth_before_death_month(self):
        birth = date(1995, 2, 3)
        invalid_death = date(1955, 1, 3)
        valid_death = date(1995, 3, 3)
        self.assertEqual(DateValidation.validate_birth_before_death(birth, invalid_death), False,
                         msg='should be False, month error')
        self.assertEqual(DateValidation.validate_birth_before_death(birth, valid_death), True, msg='correct')

    def test_validate_birth_before_death_day(self):
        birth = date(1995, 2, 3)
        invalid_death = date(1955, 2, 2)
        valid_death = date(1995, 2, 4)
        self.assertEqual(DateValidation.validate_birth_before_death(birth, invalid_death), False,
                         msg='should be False, day error')
        self.assertEqual(DateValidation.validate_birth_before_death(birth, valid_death), True, msg='correct')

    def test_validate_birth_before_death_valid(self):
        birth = date(1995, 2, 3)
        valid_death = date(2011, 11, 19)
        self.assertEqual(DateValidation.validate_birth_before_death(birth, valid_death), True, msg='correct')

    #Testcases of US04
    def test_validate_marraige_before_divorce_year(self):
        marraige = date(2001, 2, 14)
        invalid_divorce = date(2000, 2, 14)
        valid_divorce = date(2002, 2, 14)
        self.assertEqual(DateValidation.validate_marraige_before_divorce(marraige, invalid_divorce), False, msg='should be False, year error')
        self.assertEqual(DateValidation.validate_marraige_before_divorce(marraige, valid_divorce), True, msg='correct')

    def test_validate_marraige_before_divorce_month(self):
        marraige = date(2001, 2, 14)
        invalid_divorce = date(2001, 1, 14)
        valid_divorce = date(2001, 3, 14)
        self.assertEqual(DateValidation.validate_marraige_before_divorce(marraige, invalid_divorce), False,
                         msg='should be False, month error')
        self.assertEqual(DateValidation.validate_marraige_before_divorce(marraige, valid_divorce), True, msg='correct')

    def test_validate_marraige_before_divorce_day(self):
        marraige = date(2001, 2, 14)
        invalid_divorce = date(2001, 2, 13)
        valid_divorce = date(2001, 2, 15)
        self.assertEqual(DateValidation.validate_marraige_before_divorce(marraige, invalid_divorce), False,
                         msg='should be False, day error')
        self.assertEqual(DateValidation.validate_marraige_before_divorce(marraige, valid_divorce), True, msg='correct')

    def test_validate_marraige_before_divorce_valid(self):
        marraige = date(2001, 2, 14)
        valid_divorce = date(2013, 7, 9)
        self.assertEqual(DateValidation.validate_marraige_before_divorce(marraige, valid_divorce), True, msg='correct')

    # Test cases US42
    def test_createValidDate_valid(self):
        validDateStr = '10 OCT 2020'
        validDate = date(2020, 10, 10)
        self.assertEqual(DateValidation.createValidDate(validDateStr), validDate, msg='Error: Date is valid')

    def test_createValidDate_invalid_Feb(self):
        invalidFebStr = '30 FEB 2020'
        self.assertRaises(ValueError, lambda:DateValidation.createValidDate(invalidFebStr))

    def test_createValidDate_invalid_Sept(self):
        invalidDateSept = '31 SEP 2019'
        self.assertRaises(ValueError, lambda:DateValidation.createValidDate(invalidDateSept))

    def test_createValidDate_Invalid_Aug(self):
        invalidDateAug = '33 AUG 2019'
        self.assertRaises(ValueError, lambda:DateValidation.createValidDate(invalidDateAug))

    # US41 Test Cases
    def test_partial_date_check_missing_day(self):
        partial_date = 'MAR 2019'
        self.assertEqual(DateValidation.partial_date_check(partial_date), '?? MAR 2019', True)

    def test_partial_date_check_missing_month_day(self):
        partial_date = '2019'
        self.assertEqual(DateValidation.partial_date_check(partial_date), '?? ??? 2019', True)

    def test_partial_date_check_full_date(self):
        full_date = '14 MAR 2019'
        self.assertEqual(DateValidation.partial_date_check(full_date), full_date, True)

if __name__ == '__main__':
    unittest.main()