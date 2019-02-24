# Test file for DateValidation.py module

import DateValidation
import unittest
from datetime import date

class TestDateValidation(unittest.TestCase):
    
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
        invalid_day = date(2019, 2, 28)
        self.assertEqual(DateValidation.validateDate(invalid_day), False, msg='Date should be invalid: day error')

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


if __name__ == '__main__':
    unittest.main()