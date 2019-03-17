import unittest
import BirthBeforeDeath

class Test_Birth_Before_Parents_Death(unittest.TestCase):

    def test_birth_before_deat(self):
        self.assertTrue(BirthBeforeDeath.birth_before_death(
            [{'INDI': '@I1@', 'BIRT': '1984-08-15', 'SPOUSE': ['@F1@'], 'num': 5},
             {'INDI': '@I2@', 'DEAT': '1995-08-15', 'SPOUSE': ['@F1@'], 'num': 5},
             {'INDI': '@I3@', 'DEAT': '1999-08-15', 'SPOUSE': ['@F1@'], 'num': 5}],
            [{'MARR': '1978-12-15', 'CHIL': ['@I1@'], 'WIFE': ['@I2@'], 'HUSB': ['@I3@']}]))
        self.assertFalse(BirthBeforeDeath.birth_before_death(
            [{'INDI': '@I1@', 'BIRT': '1994-08-15', 'SPOUSE': ['@F1@'], 'num': 5},
             {'INDI': '@I2@', 'DEAT': '1998-07-15', 'SPOUSE': ['@F1@'], 'num': 5},
             {'INDI': '@I3@', 'DEAT': '1993-08-15', 'SPOUSE': ['@F1@'], 'num': 5}],
            [{'MARR': '1978-12-15', 'CHIL': ['@I1@'], 'WIFE': ['@I2@'], 'HUSB': ['@I3@']}]))

if __name__ == '__main__':
    unittest.main(exit=False, verbosity=2)