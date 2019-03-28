import MarriageValidation
import unittest
from datetime import date


class TestMarriageValidation(unittest.TestCase):
    def test_valid_age_at_marriage_year(self):
        print("US10: Testing valid age at marriage (invalid year < 14 years old)")
        birthdate = date(2006, 3, 31)
        marriage = date(2019, 2, 17)
        self.assertEqual(MarriageValidation.valid_age_at_marriage(birthdate, marriage), False,
                         msg="Return False: age is less than 14 by year(s)")

    def test_valid_age_at_marriage_month(self):
        print("US10: Testing valid age at marriage (invalid month < 14 years old)")
        birthdate = date(2005, 3, 16)
        marriage = date(2019, 2, 17)
        self.assertEqual(MarriageValidation.valid_age_at_marriage(birthdate, marriage), False,
                         msg="Return False: age is less than 14 by month(s)")

    def test_valid_age_at_marriage_day(self):
        print("US10: Testing valid age at marriage (invalid day < 14 years old)")
        birthdate = date(2005, 2, 17)
        marriage = date(2019, 2, 16)
        self.assertEqual(MarriageValidation.valid_age_at_marriage(birthdate, marriage), False,
                         msg="Return False: age is less than 14 by day(s)")

    def test_valid_age_at_marriage_equal(self):
        print("US10: Testing valid age at marriage (invalid date < 14 years old)")
        birthdate = date(2005, 2, 17)
        marriage = date(2019, 2, 17)
        self.assertEqual(MarriageValidation.valid_age_at_marriage(birthdate, marriage), True,
                         msg="Return True: spouse just turned 14")

    def test_valid_age_at_marriage_ok(self):
        print("US10: Testing valid age at marriage (valid > 14 years old)")
        birthdate = date(2000, 1, 1)
        marriage = date(2019, 2, 17)
        self.assertEqual(MarriageValidation.valid_age_at_marriage(birthdate, marriage), True,
                         msg="Return True: spouse is at least 14")

    def test_not_bigamous_ok(self):
        print("US11: Testing bigamy (valid)")
        marriages = [date(2005, 5, 25), date(2009, 2, 20), date(2011, 4, 12)]
        deaths = [date(2006, 12, 12)]
        divorces = [date(2010, 1, 1)]
        self.assertEqual(MarriageValidation.not_bigamous(marriages, sorted(divorces + deaths)), True,
                         msg="Return True: all previous marriages terminated")

    def test_not_bigamous_married_before_death(self):
        print("US11: Testing bigamy (invalid married before death of previous spouse)")
        marriages = [date(2005, 5, 25), date(2009, 2, 20), date(2011, 4, 12)]
        deaths = [date(2009, 12, 12)]
        divorces = [date(2010, 1, 1)]
        self.assertEqual(MarriageValidation.not_bigamous(marriages, sorted(divorces + deaths)), False,
                         msg="Return False: Married before death")

    def test_not_bigamous_married_before_divorce(self):
        print("US11: Testing bigamy (invalid married before divorce)")
        marriages = [date(2005, 5, 25), date(2009, 2, 20), date(2011, 4, 12)]
        deaths = [date(2006, 12, 12)]
        divorces = [date(2012, 1, 1)]
        self.assertEqual(MarriageValidation.not_bigamous(marriages, sorted(divorces + deaths)), False,
                         msg="Return False: Married before divorce")


if __name__ == '__main__':
    unittest.main()
