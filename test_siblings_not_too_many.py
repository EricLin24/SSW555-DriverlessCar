import unittest
from siblings_not_too_many import siblings_not_too_many

class TestSiblingsNotTooMany(unittest.TestCase):
    def test_valid_siblings_num(self):
        siblings = {
            '1': [{'ID':'123', 'Name':'A', 'Birthday':'8/9/1994', 'Age': 24}, {'ID':'123', 'Name':'A', 'Birthday':'8/9/1994', 'Age': 24}, {'ID':'123', 'Name':'A', 'Birthday':'8/9/1994', 'Age': 24}],
            '2': [{'ID':'234', 'Name':'B', 'Birthday':'8/9/1993', 'Age': 25}],
            '3': [{'ID':'242', 'Name':'C', 'Birthday':'8/9/1992', 'Age': 26}]
        }
        errors = set()
        errors = siblings_not_too_many(siblings, errors)
        self.assertEqual(len(errors), 0, msg='len of errors should be 0')

    def test_siblings_more_than_15(self):
        siblings = {
            '1': [
                {'ID':'123', 'Name':'A', 'Birthday':'8/9/1994', 'Age': 24}, {'ID':'123', 'Name':'A', 'Birthday': '8/9/1994', 'Age': 24}, {'ID':'123', 'Name':'A', 'Birthday': '8/9/1994', 'Age': 24},
                {'ID': '123', 'Name': 'A', 'Birthday': '8/9/1994', 'Age': 24},
                {'ID': '123', 'Name': 'A', 'Birthday': '8/9/1994', 'Age': 24},
                {'ID': '123', 'Name': 'A', 'Birthday': '8/9/1994', 'Age': 24},
                {'ID': '123', 'Name': 'A', 'Birthday': '8/9/1994', 'Age': 24},
                {'ID': '123', 'Name': 'A', 'Birthday': '8/9/1994', 'Age': 24},
                {'ID': '123', 'Name': 'A', 'Birthday': '8/9/1994', 'Age': 24},
                {'ID': '123', 'Name': 'A', 'Birthday': '8/9/1994', 'Age': 24},
                {'ID': '123', 'Name': 'A', 'Birthday': '8/9/1994', 'Age': 24},
                {'ID': '123', 'Name': 'A', 'Birthday': '8/9/1994', 'Age': 24},
                {'ID': '123', 'Name': 'A', 'Birthday': '8/9/1994', 'Age': 24},
                {'ID': '123', 'Name': 'A', 'Birthday': '8/9/1994', 'Age': 24},
                {'ID': '123', 'Name': 'A', 'Birthday': '8/9/1994', 'Age': 24}
                  ],
            '2': [{'ID':'234', 'Name':'B', 'Birthday':'8/9/1993', 'Age': 25}],
            '3': [{'ID':'242', 'Name':'C', 'Birthday':'8/9/1992', 'Age': 26}]
        }
        errors = set()
        errors = siblings_not_too_many(siblings, errors)
        self.assertEqual(len(errors), 1, msg='len of errors should be 1')
        for e in errors:
            print(e.getErrMsg())

if __name__ == '__main__':
    unittest.main()