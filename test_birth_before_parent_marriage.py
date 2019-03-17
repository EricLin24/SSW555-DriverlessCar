import birth_before_parent_marriage
import unittest
import Error

class TestBirthBeforeParentMarriage(unittest.TestCase):
    #Children should be born after marriage of parents
    def test_valid_birth_before_parent_marriage(self):
        birth = '20 APR 1994'
        valid_marriage = '20 APR 1993'
        errors = set()
        errors = birth_before_parent_marriage.birth_before_parent_marriage(birth, valid_marriage, 'NA', errors)
        self.assertEqual(len(errors), 0, msg='Failed to check valid birth')

    def test_before_parent_marriage_year(self):
        birth = '20 APR 1994'
        invalid_marriage = '20 APR 1995'
        errors = set()
        errors = birth_before_parent_marriage.birth_before_parent_marriage(birth, invalid_marriage, 'NA', errors)

        for err in errors:
            self.assertEqual(err.errCode,
                             Error.ErrorEnum.US08, msg='failed to generate US08 error in test_before_marriage_year')


    def test_before_parent_marriage_month(self):
        birth = '20 APR 1994'
        invalid_marriage = '20 MAY 1994'

        errors = set()
        errors = birth_before_parent_marriage.birth_before_parent_marriage(birth, invalid_marriage, 'NA', errors)
        for err in errors:
            self.assertEqual(err.errCode,
                             Error.ErrorEnum.US08, msg='failed to generate US08 error in test_before_marriage_month')


    def test_before_parent_marriage_day(self):
        birth = '20 APR 1994'
        invalid_marriage = '21 APR 1994'

        errors = set()
        errors = birth_before_parent_marriage.birth_before_parent_marriage(birth, invalid_marriage, 'NA', errors)
        for err in errors:
            self.assertEqual(err.errCode,
                             Error.ErrorEnum.US08, msg='failed to generate US08 error in test_before_marriage_day')

    # not more than 9 months after divorce
    def test_after_parent_divorce(self):
        birth = '20 APR 1994'
        valid_marriage = '19 APR 1994'
        invalid_divorce = '19 JUL 1993'

        errors = set()
        errors = birth_before_parent_marriage.birth_before_parent_marriage(birth, valid_marriage, invalid_divorce, errors)

        for err in errors:
            self.assertEqual(err.errCode,
                             Error.ErrorEnum.US08, msg='Failed to generate US08 error in test_after_divorce')

if __name__ == '__main__':
    unittest.main()
