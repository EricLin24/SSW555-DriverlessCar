import PartialDates
import unittest

class TestPartialDateValidation(unittest.TestCase):
    def test_partial_date_check_missing_day(self):
        partial_date = 'MAR 2019'
        self.assertEqual(PartialDates.partial_date_check(partial_date), '?? MAR 2019', True)

    def test_partial_date_check_missing_month_day(self):
        partial_date = '2019'
        self.assertEqual(PartialDates.partial_date_check(partial_date), '?? ??? 2019', True)

    def test_partial_date_check_full_date(self):
        full_date = '14 MAR 2019'
        self.assertEqual(PartialDates.partial_date_check(full_date), full_date, True)


if __name__ == '__main__':
    unittest.main()