import SiblingSpacing
import unittest

class TestSiblingSpacing(unittest.TestCase):
    def test_valid_sibling_spacing(self):
        date1 = '20 FEB 1992'
        date2 = '15 MAR 1992'
        self.assertEqual(SiblingSpacing.valid_sibling_spacing(date1, date2), False,
                         msg='Return False: dates too close - year')

    def test_valid_sibling_spacing_days(self):
        date1 = '20 FEB 1992'
        date2 = '21 FEB 1992'
        self.assertEqual(SiblingSpacing.valid_sibling_spacing(date1, date2), True, msg='Return True: less than 2 days')


if __name__ == '__main__':
    unittest.main()