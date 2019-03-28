# Test file for DateValidation.py module

import DateValidation
import unittest
from datetime import date

class TestDateValidation(unittest.TestCase):

    # Test Cases US01
    def test_validateDate_valid(self):
        print("US01: Testing a valid date...")
        valid_date = date(1990, 4, 21)
        self.assertEqual(DateValidation.validateDate(valid_date), True, msg='Date is valid')

    def test_validateDate_invalid_year(self):
        print("US01: Testing an invalid date with invalid year...")
        today = date.today()
        invalid_year = date((today.year + 5), today.month, today.day)
        self.assertEqual(DateValidation.validateDate(invalid_year), False, msg='Date should be invalid: year error')

    def test_validateDate_invalid_month(self):
        print("US01: Testing an invalid date with invalid month...")
        today = date.today()
        invalid_month = date(today.year, (today.month + 3), today.day)
        self.assertEqual(DateValidation.validateDate(invalid_month), False, msg='Date should be invalid: month error')

    def test_validateDate_invalid_day(self):
        print("US01: Testing an invalid date with invalid day...")
        today = date.today()
        invalid_day = date(today.year, today.month, (today.day + 1))
        self.assertEqual(DateValidation.validateDate(invalid_day), False, msg='Date should be invalid: day error')

    # Test Cases US02
    def test_validateMarraigeDate_valid(self):
        print("US02: Testing a valid marriage date...")
        validBirthdate = date(1990, 12, 28)
        validMarraigeDate = date(2019, 1, 1)
        self.assertEqual(DateValidation.validateMarraigeDate(validBirthdate, validMarraigeDate), True, msg='Valid: marraige date after birthdate')

    def test_validateMarraigeDate_invalid_year(self):
        print("US02: Testing an invalid marriage date with invalid year...")
        validBirthdate = date(1990, 12, 28)
        invalidMarraigeDate_year = date(1919, 3, 21)
        self.assertEqual(DateValidation.validateMarraigeDate(validBirthdate, invalidMarraigeDate_year), False, msg='Marraige date should be invalid: year error')

    def test_validateMarraigeDate_invalid_month(self):
        print("US02: Testing an invalid marriage date with invalid month...")
        validBirthdate = date(1990, 12, 28)
        invalidMarraigeDate_month = date(1990, 11, 21)
        self.assertEqual(DateValidation.validateMarraigeDate(validBirthdate, invalidMarraigeDate_month), False, msg='Marraige date should be invalid: month error')

    def test_validateMarraigeDate_invalid_day(self):
        print("US02: Testing an invalid marriage date with invalid day...")
        validBirthdate = date(1990, 12, 28)
        invalidMarraigeDate_day = date(1990, 12, 21)
        self.assertEqual(DateValidation.validateMarraigeDate(validBirthdate, invalidMarraigeDate_day), False, msg='Marraige date should be invalid: day error')

    #Testcases of US03
    def test_validate_birth_before_death_year(self):
        print("US03: Testing birth before death (invalid year)...")
        birth = date(1955, 2, 3)
        invalid_death = date(1954, 2, 3)
        valid_death = date(1956, 2, 3)
        self.assertEqual(DateValidation.validate_birth_before_death(birth, invalid_death), False,
                         msg='should be False, year error.')
        self.assertEqual(DateValidation.validate_birth_before_death(birth, valid_death), True, msg='correct')

    def test_validate_birth_before_death_month(self):
        print("US03: Testing birth before death (invalid month)...")
        birth = date(1995, 2, 3)
        invalid_death = date(1955, 1, 3)
        valid_death = date(1995, 3, 3)
        self.assertEqual(DateValidation.validate_birth_before_death(birth, invalid_death), False,
                         msg='should be False, month error')
        self.assertEqual(DateValidation.validate_birth_before_death(birth, valid_death), True, msg='correct')

    def test_validate_birth_before_death_day(self):
        print("US03: Testing birth before death (invalid day)...")
        birth = date(1995, 2, 3)
        invalid_death = date(1955, 2, 2)
        valid_death = date(1995, 2, 4)
        self.assertEqual(DateValidation.validate_birth_before_death(birth, invalid_death), False,
                         msg='should be False, day error')
        self.assertEqual(DateValidation.validate_birth_before_death(birth, valid_death), True, msg='correct')

    def test_validate_birth_before_death_valid(self):
        print("US03: Testing birth before death (valid)...")
        birth = date(1995, 2, 3)
        valid_death = date(2011, 11, 19)
        self.assertEqual(DateValidation.validate_birth_before_death(birth, valid_death), True, msg='correct')

    #Testcases of US04
    def test_validate_marraige_before_divorce_year(self):
        print("US04: Testing marriage before divorce (invalid year)...")
        marraige = date(2001, 2, 14)
        invalid_divorce = date(2000, 2, 14)
        valid_divorce = date(2002, 2, 14)
        self.assertEqual(DateValidation.validate_marraige_before_divorce(marraige, invalid_divorce), False, msg='should be False, year error')
        self.assertEqual(DateValidation.validate_marraige_before_divorce(marraige, valid_divorce), True, msg='correct')

    def test_validate_marraige_before_divorce_month(self):
        print("US04: Testing marriage before divorce (invalid month)...")
        marraige = date(2001, 2, 14)
        invalid_divorce = date(2001, 1, 14)
        valid_divorce = date(2001, 3, 14)
        self.assertEqual(DateValidation.validate_marraige_before_divorce(marraige, invalid_divorce), False,
                         msg='should be False, month error')
        self.assertEqual(DateValidation.validate_marraige_before_divorce(marraige, valid_divorce), True, msg='correct')

    def test_validate_marraige_before_divorce_day(self):
        print("US04: Testing marriage before divorce (invalid day)...")
        marraige = date(2001, 2, 14)
        invalid_divorce = date(2001, 2, 13)
        valid_divorce = date(2001, 2, 15)
        self.assertEqual(DateValidation.validate_marraige_before_divorce(marraige, invalid_divorce), False,
                         msg='should be False, day error')
        self.assertEqual(DateValidation.validate_marraige_before_divorce(marraige, valid_divorce), True, msg='correct')

    def test_validate_marraige_before_divorce_valid(self):
        print("US04: Testing marriage before divorce (valid)...")
        marraige = date(2001, 2, 14)
        valid_divorce = date(2013, 7, 9)
        self.assertEqual(DateValidation.validate_marraige_before_divorce(marraige, valid_divorce), True, msg='correct')

    # Test cases US42
    def test_createValidDate_valid(self):
        print("US42: Testing creating a valid date from string (valid)...")
        validDateStr = '10 OCT 2020'
        validDate = date(2020, 10, 10)
        self.assertEqual(DateValidation.createValidDate(validDateStr), validDate, msg='Error: Date is valid')

    def test_createValidDate_invalid_Feb(self):
        print("US42: Testing creating a valid date from string (invalid days in month)...")
        invalidFebStr = '30 FEB 2020'
        self.assertRaises(ValueError, lambda:DateValidation.createValidDate(invalidFebStr))

    def test_createValidDate_invalid_Sept(self):
        print("US42: Testing creating a valid date from string (invalid days in month)...")
        invalidDateSept = '31 SEP 2019'
        self.assertRaises(ValueError, lambda:DateValidation.createValidDate(invalidDateSept))

    def test_createValidDate_Invalid_Aug(self):
        print("US42: Testing creating a valid date from string (invalid days in month)...")
        invalidDateAug = '33 AUG 2019'
        self.assertRaises(ValueError, lambda:DateValidation.createValidDate(invalidDateAug))

    # US41 Test Cases
    def test_partial_date_check_missing_day(self):
        print("US41: Testing creating a valid date from an incomplete date string (missing day)...")
        partial_date = 'MAR 2019'
        self.assertEqual(DateValidation.partial_date_check(partial_date), '?? MAR 2019', True)

    def test_partial_date_check_missing_month_day(self):
        print("US41: Testing creating a valid date from an incomplete date string (missing day and month)...")
        partial_date = '2019'
        self.assertEqual(DateValidation.partial_date_check(partial_date), '?? ??? 2019', True)

    def test_partial_date_check_full_date(self):
        print("US41: Testing creating a valid date from an incomplete date string (full date)...")
        full_date = '14 MAR 2019'
        self.assertEqual(DateValidation.partial_date_check(full_date), full_date, True)

if __name__ == '__main__':
    unittest.main()
