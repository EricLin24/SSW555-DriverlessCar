import unittest
import DivorceBeforeDeathValidation
import MarriageBeforeDeathValidation

class Test_Divorce_Before_Death(unittest.TestCase):

    def test_divorce_before_death(self):
        self.assertTrue(DivorceBeforeDeathValidation.divorce_before_death([{'INDI': '@I1@', 'DEAT': '2018-08-15', 'SPOUSE': ['@F1@'], 'num': 5}], [{'DIV': '2010-12-15'}]))
        self.assertTrue(DivorceBeforeDeathValidation.divorce_before_death([{'INDI': '@I1@', 'DEAT': '2017-08-15', 'SPOUSE': 'NONE', 'num': 5}], [{'DIV': 'NONE'}]))
        self.assertFalse(DivorceBeforeDeathValidation.divorce_before_death([{'INDI': '@I1@', 'DEAT': '1991-01-15', 'SPOUSE': ['@F1@'], 'num': 5}], [{'DIV': '1999-12-15'}]))
        self.assertFalse(DivorceBeforeDeathValidation.divorce_before_death([{'INDI': '@I1@', 'DEAT': '2010-09-15', 'SPOUSE': ['@F1@'], 'num': 5}], [{'DIV': '2019-1-15'}]))
        self.assertFalse(DivorceBeforeDeathValidation.divorce_before_death([{'INDI': '@I1@', 'DEAT': '1992-04-15', 'SPOUSE': ['@F1@'], 'num': 5}], [{'DIV': '1997-2-22'}]))
    
    def test_marriage_before_death(self):
        self.assertTrue(MarriageBeforeDeathValidation.marriage_before_death([{'INDI': '@I1@', 'num': 5, 'DEAT': '1994-08-15', 'SPOUSE': ['@F1@']}], [{'MARR': '1968-12-15'}]))
        self.assertTrue(MarriageBeforeDeathValidation.marriage_before_death([{'INDI': '@I1@', 'num': 5, 'DEAT': '1994-08-15', 'SPOUSE': 'NONE'}], [{'MARR': 'NONE'}]))
        self.assertFalse(MarriageBeforeDeathValidation.marriage_before_death([{'INDI': '@I1@', 'num': 5, 'DEAT': '1993-08-15', 'SPOUSE': ['@F1@', '@F2@']}],[{'MARR': '1999-12-15'}, {'MARR': '2000-12-15'}]))
        self.assertFalse(MarriageBeforeDeathValidation.marriage_before_death([{'INDI': '@I1@', 'num': 5, 'DEAT': '1992-08-15', 'SPOUSE': ['@F1@']}], [{'MARR': '1996-11-15'}]))
        self.assertFalse(MarriageBeforeDeathValidation.marriage_before_death([{'INDI': '@I1@', 'num': 5, 'DEAT': '1991-08-15', 'SPOUSE': ['@F1@']}], [{'MARR': '1999-1-15'}]))


if __name__ == '__main__':
    unittest.main(exit=False, verbosity=2)