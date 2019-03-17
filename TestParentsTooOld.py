import unittest
import ParentsNotTooOld

class Test_Parents_Too_Old(unittest.TestCase):
     def test_parents_not_too_old(self):
        self.assertTrue(ParentsNotTooOld.parents_too_old(
            [{'INDI': '@I1@', 'BIRT': '1994-08-15', 'AGE': '20', 'SPOUSE': ['@F1@'], 'num': 5}, {'INDI': '@I2@', 'DEAT': '1995-08-15', 'AGE': '50', 'SPOUSE': ['@F1@'], 'num': 5},
             {'INDI': '@I3@', 'DEAT': '1996-08-15', 'AGE': '40', 'SPOUSE': ['@F1@'], 'num': 5}],
            [{'MARR': '2001-12-15', 'CHIL': ['@I1@'], 'WIFE': ['@I2@'], 'HUSB': ['@I3@']}]))
        self.assertFalse(ParentsNotTooOld.parents_too_old(
            [{'INDI': '@I1@', 'BIRT': '1992-08-15', 'AGE': '20', 'SPOUSE': ['@F1@'], 'num': 5},{'INDI': '@I2@', 'DEAT': '1991-07-15', 'AGE': '1000', 'SPOUSE': ['@F1@'], 'num': 5},
             {'INDI': '@I3@', 'DEAT': '1996-06-15', 'AGE': '60', 'SPOUSE': ['@F1@'], 'num': 5}],
            [{'MARR': '1968-12-15', 'CHIL': ['@I1@'], 'WIFE': ['@I2@'], 'HUSB': ['@I3@']}]))
     
if __name__ == '__main__':
    unittest.main(exit=False, verbosity=2)