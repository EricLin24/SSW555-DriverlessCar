import unittest
import ParentsNotTooOld


class Test_Parents_Too_Old(unittest.TestCase):

    def test_parent_age_check_father_invalid(self):
        p_birth = '1 APR 1900'
        c_birth = '2 APR 1980'
        self.assertEqual(ParentsNotTooOld.parent_age_check(80, p_birth, c_birth), False,
                         msg="Father over 80 at child birth")

    def test_parent_age_check_mother_invalid(self):
        p_birth = '1 APR 1900'
        c_birth = '2 APR 1960'
        self.assertEqual(ParentsNotTooOld.parent_age_check(60, p_birth, c_birth), False,
                         msg="Mother over 60 at child birth")

    def test_parent_age_check_father_valid(self):
        p_birth = '1 APR 1900'
        c_birth = '24 MAR 1950'
        self.assertEqual(ParentsNotTooOld.parent_age_check(80, p_birth, c_birth), True,
                         msg="Pass. Father under 80 at child birth")

    def test_parent_age_check_mother_valid(self):
        p_birth = '1 APR 1900'
        c_birth = '24 MAR 1950'
        self.assertEqual(ParentsNotTooOld.parent_age_check(60, p_birth, c_birth), True,
                         msg="Pass. Mother under 60 at child birth")

    # def test_parents_not_too_old(self):
    #     self.assertTrue(ParentsNotTooOld.parents_too_old(
    #     [{'INDI': '@I1@', 'BIRT': '1994-08-15', 'AGE': '20', 'SPOUSE': ['@F1@'], 'num': 5}, {'INDI': '@I2@', 'DEAT': '1995-08-15', 'AGE': '50', 'SPOUSE': ['@F1@'], 'num': 5},
    #      {'INDI': '@I3@', 'DEAT': '1996-08-15', 'AGE': '40', 'SPOUSE': ['@F1@'], 'num': 5}],
    #     [{'MARR': '2001-12-15', 'CHIL': ['@I1@'], 'WIFE': ['@I2@'], 'HUSB': ['@I3@']}]))
    #     self.assertFalse(ParentsNotTooOld.parents_too_old(
    #     [{'INDI': '@I1@', 'BIRT': '1992-08-15', 'AGE': '20', 'SPOUSE': ['@F1@'], 'num': 5},{'INDI': '@I2@', 'DEAT': '1991-07-15', 'AGE': '1000', 'SPOUSE': ['@F1@'], 'num': 5},
    #      {'INDI': '@I3@', 'DEAT': '1996-06-15', 'AGE': '60', 'SPOUSE': ['@F1@'], 'num': 5}],
    #     [{'MARR': '1968-12-15', 'CHIL': ['@I1@'], 'WIFE': ['@I2@'], 'HUSB': ['@I3@']}]))
     
if __name__ == '__main__':
    unittest.main(exit=False, verbosity=2)