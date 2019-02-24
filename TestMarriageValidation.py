import MarriageValidation
import unittest
from datetime import date


class TestMarriageValidation(unittest.TestCase):
    def test_valid_age_at_marriage_year(self):
        birthdate = date(2006, 3, 31)
        marriage = date(2019, 2, 17)
        self.assertEqual(MarriageValidation.valid_age_at_marriage(birthdate, marriage), False,
                         msg="Return False: age is less than 14 by year(s)")

    def test_valid_age_at_marriage_month(self):
        birthdate = date(2005, 3, 16)
        marriage = date(2019, 2, 17)
        self.assertEqual(MarriageValidation.valid_age_at_marriage(birthdate, marriage), False,
                         msg="Return False: age is less than 14 by month(s)")

    def test_valid_age_at_marriage_day(self):
        birthdate = date(2005, 2, 17)
        marriage = date(2019, 2, 16)
        self.assertEqual(MarriageValidation.valid_age_at_marriage(birthdate, marriage), False,
                         msg="Return False: age is less than 14 by day(s)")

    def test_valid_age_at_marriage_equal(self):
        birthdate = date(2005, 2, 17)
        marriage = date(2019, 2, 17)
        self.assertEqual(MarriageValidation.valid_age_at_marriage(birthdate, marriage), True,
                         msg="Return True: spouse just turned 14")

    def test_valid_age_at_marriage_ok(self):
        birthdate = date(2000, 1, 1)
        marriage = date(2019, 2, 17)
        self.assertEqual(MarriageValidation.valid_age_at_marriage(birthdate, marriage), True,
                         msg="Return True: spouse is at least 14")

    def test_bigamy_check(self):





if __name__ == '__main__':
    unittest.main()