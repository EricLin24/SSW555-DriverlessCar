import unittest
import UniqueIds


class TestUniqueIds(unittest.TestCase):
    def test_no_duplicate_family_ids(self):
        familyDict = {'1': 'data',
                      '2': 'data'}

        newId = '3'

        self.assertEqual(False, UniqueIds.UniqueFamilyIds(newId, familyDict),
                         msg='New ID does not exist in current family dict')

    def test_no_duplicate_individual_ids(self):
        memberDict = {'1': 'data',
                      '2': 'data'}
        newId = '3'

        self.assertEqual(False, UniqueIds.UniqueFamilyIds(newId, memberDict),
                         msg='New ID does not exist in current member dict')

    def test_duplicate_individual_ids(self):
        memberDict = {'1': 'data',
                      '2': 'data'}

        newId = '2'
        self.assertEqual(True, UniqueIds.UniqueFamilyIds(newId, memberDict),
                         msg='New ID is a duplicate ID in current member dict')

    def test_duplicate_family_ids(self):
        familyDict = {'1': 'data',
                      '2': 'data'}

        newId = '2'

        self.assertEqual(True, UniqueIds.UniqueFamilyIds(newId, familyDict),
                         msg='New ID does not exist in current family dict')


if __name__ == '__main__':
    unittest.main()