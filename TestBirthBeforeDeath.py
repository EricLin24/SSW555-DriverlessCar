import unittest
import BirthBeforeDeath

class Test_Birth_Before_Parents_Death(unittest.TestCase):

    def test_birth_before_death_invalid_year(self):
        print("US09: Testing birth before death of parents (invalid year)...")
        death = '1 MAR 2000'
        birth = '1 MAR 2001'
        self.assertEqual(BirthBeforeDeath.birth_before_death(death, birth), False,
                         msg='Return False: child born >= 1 year after parent death')

    def test_birth_before_death_invalid_month(self):
        print("US09: Testing birth before death of parents (invalid month)...")
        death = '1 MAR 2000'
        birth = '1 APR 2000'
        self.assertEqual(BirthBeforeDeath.birth_before_death(death, birth), False,
                         msg='Return False: child born >= 1 month after parent death')

    def test_birth_before_death_invalid_day(self):
        print("US09: Testing birth before death of parents (invalid day)...")
        death = '1 MAR 2000'
        birth = '2 MAR 2000'
        self.assertEqual(BirthBeforeDeath.birth_before_death(death, birth), False,
                         msg='Return False: child born >= 1 day after parent death')

    def test_birth_before_death_equal(self):
        print("US09: Testing birth before death of parents (invalid)...")
        death = '1 MAR 2000'
        birth = '1 MAR 2000'
        self.assertEqual(BirthBeforeDeath.birth_before_death(death, birth), True,
                         msg='Return True: child on same day as parent death')

    def test_birth_before_death_valid(self):
        print("US09: Testing birth before death of parents (valid)...")
        death = '1 MAR 2000'
        birth = '28 FEB 2000'
        self.assertEqual(BirthBeforeDeath.birth_before_death(death, birth), True,
                         msg='Return True: child born before death')

    # def old_test_birth_before_death(self):
    #     self.assertTrue(BirthBeforeDeath.birth_before_death(
    #         [{'INDI': '@I1@', 'BIRT': '1984-08-15', 'SPOUSE': ['@F1@'], 'num': 5},
    #          {'INDI': '@I2@', 'DEAT': '1995-08-15', 'SPOUSE': ['@F1@'], 'num': 5},
    #          {'INDI': '@I3@', 'DEAT': '1999-08-15', 'SPOUSE': ['@F1@'], 'num': 5}],
    #         [{'MARR': '1978-12-15', 'CHIL': ['@I1@'], 'WIFE': ['@I2@'], 'HUSB': ['@I3@']}]))
    #     self.assertFalse(BirthBeforeDeath.birth_before_death(
    #         [{'INDI': '@I1@', 'BIRT': '1994-08-15', 'SPOUSE': ['@F1@'], 'num': 5},
    #          {'INDI': '@I2@', 'DEAT': '1998-07-15', 'SPOUSE': ['@F1@'], 'num': 5},
    #          {'INDI': '@I3@', 'DEAT': '1993-08-15', 'SPOUSE': ['@F1@'], 'num': 5}],
    #         [{'MARR': '1978-12-15', 'CHIL': ['@I1@'], 'WIFE': ['@I2@'], 'HUSB': ['@I3@']}]))

if __name__ == '__main__':
    unittest.main(exit=False, verbosity=2)
