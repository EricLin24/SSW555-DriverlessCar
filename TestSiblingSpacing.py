import SiblingSpacing
import unittest

class TestSiblingSpacing(unittest.TestCase):
    def test_valid_sibling_spacing_too_close(self):
        print("US13: Testing sibling spacing, must be >= 9 months apart (invalid < 8 months)")
        date1 = '20 FEB 1992'
        date2 = '15 MAR 1992'
        self.assertEqual(SiblingSpacing.valid_sibling_spacing(date1, date2), False,
                         msg='Return False: dates too close - less than 8 months, greater than 1 day')

    def test_valid_sibling_spacing_days(self):
        print("US13: Testing sibling spacing, must be >= 9 months apart (valid < 2 days for twins)")
        date1 = '20 FEB 1992'
        date2 = '21 FEB 1992'
        self.assertEqual(SiblingSpacing.valid_sibling_spacing(date1, date2), True, msg='Return True: less than 2 days')

    def test_valid_sibling_spacing_validDate(self):
        print("US13: Testing sibling spacing, must be >= 9 months apart (valid)")
        date1 = '20 FEB 1992'
        date2 = '8 OCT 1994'
        self.assertEqual(SiblingSpacing.valid_sibling_spacing(date1, date2), True, msg='Return True: more than 8 months')


if __name__ == '__main__':
    unittest.main()
