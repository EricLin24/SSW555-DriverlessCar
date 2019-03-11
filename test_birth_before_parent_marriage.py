import birth_before_parent_marriage
import unittest

class TestBirthBeforeParentMarriage(unittest.TestCase):
    #Children should be born after marriage of parents
    def test_before_marriage_year(self):
        birth = '20 APR 1994'
        invalid_marriage = '20 APR 1995'
        valid_marriage = '20 APR 1993'
        self.assertEqual(birth_before_parent_marriage.birth_before_parent_marriage(birth, invalid_marriage, 'NA')[0],
                         False, msg='Should be False')
        self.assertEqual(birth_before_parent_marriage.birth_before_parent_marriage(birth, valid_marriage, 'NA')[0],
                         True, msg='Should be True')

    def test_before_marriage_month(self):
        birth = '20 APR 1994'
        invalid_marriage = '20 MAY 1994'
        valid_marriage = '20 MAR 1994'
        self.assertEqual(birth_before_parent_marriage.birth_before_parent_marriage(birth, invalid_marriage, 'NA')[0],
                         False, msg='Should be False')
        self.assertEqual(birth_before_parent_marriage.birth_before_parent_marriage(birth, valid_marriage, 'NA')[0],
                         True, msg='Should be True')

    def test_before_marriage_day(self):
        birth = '20 APR 1994'
        invalid_marriage = '21 APR 1994'
        valid_marriage = '19 APR 1994'
        self.assertEqual(birth_before_parent_marriage.birth_before_parent_marriage(birth, invalid_marriage, 'NA')[0],
                         False, msg='Should be False')
        self.assertEqual(birth_before_parent_marriage.birth_before_parent_marriage(birth, valid_marriage, 'NA')[0],
                         True, msg='Should be True')

    # not more than 9 months after divorce
    def test_after_divorce(self):
        birth = '20 APR 1994'
        valid_marriage = '19 APR 1994'
        invalid_divorce = '19 JUL 1993'
        valid_divorce = '21 JUL 1994'
        self.assertEqual(
            birth_before_parent_marriage.birth_before_parent_marriage(birth, valid_marriage, invalid_divorce)[0],
            False, msg='Should be False')
        self.assertEqual(
            birth_before_parent_marriage.birth_before_parent_marriage(birth, valid_marriage, valid_divorce)[0],
            True, msg='Should be True')

if __name__ == '__main__':
    unittest.main()
