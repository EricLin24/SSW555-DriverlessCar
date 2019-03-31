# TestMain.py - runs all availabel unit tests

import unittest
from TestDateValidation import TestDateValidation
from TestDeathValidation import Test_Divorce_Before_Death
from TestBirthBeforeDeath import Test_Birth_Before_Parents_Death
from test_lessthan_150 import TestLessThan150
from TestError import TestError
from TestFamilyValidation import TestFamilyValidation
from TestMarriageValidation import TestMarriageValidation
from TestParentsTooOld import Test_Parents_Too_Old
from TestSiblingSpacing import TestSiblingSpacing
from test_birth_before_parent_marriage import TestBirthBeforeParentMarriage
from test_siblings_not_marry import TestSiblingsNotMarry
from TestLivingMaritalStatus import TestLivingMaritalStatus
from TestMaleLastName import TestMaleNames
from TestMarriageToChildren import TestSameFamilyChildrenMarriage

if __name__ == '__main__':
    unittest.main()