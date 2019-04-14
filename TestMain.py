# TestMain.py - runs all available unit tests

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
#from test_siblings_not_too_many import TestSiblingsNotTooMany
from TestLivingMaritalStatus import TestLivingMaritalStatus
from TestMaleLastName import TestMaleNames
from TestMarriageToChildren import TestSameFamilyChildrenMarriage
from TestDeseasedIndividuals import TestDeseasedIndividauls
from test_unique_name_birth import TestUniqueNameAndBirth
from test_unique_family_spouses_marriage_date import TestUniqueFamilySpousesMarriageDate
from TestUniqueIds import TestUniqueIds
from TestCousinsMarriageValidation import TestCousinMarrages

if __name__ == '__main__':
    unittest.main()