import unittest
import Error
from unique_family_spouses_marriage_date import unique_family_spouse_marriage_date


class TestUniqueFamilySpousesMarriageDate(unittest.TestCase):
    def test_valid_spouses_and_marriage_date(self):
        print("US24: No more than one family with the same spouses by name and the same marriage date should appear in a GEDCOM file")
        parsed_file = {
            'family': {
                '1': {
                    'Children': {
                        '@c@',
                        '@d@'
                    },
                    'Married': '1 JUL 1990',
                    'Spouse 1': '@a@',
                    'Spouse 2': '@b@',
                    'Spouse 1 Name': 'Brian',
                    'Spouse 2 Name': 'Jane Lancing /Smith/',
                    'Divorced': 'NA'
                },
                '2': {
                    'Children': {
                        '@I6000000089090979883@',
                        '@I6000000089090979871@'
                    },
                    'Married': '2 JUL 1990',
                    'Spouse 1': '@I6000000089090867827@',
                    'Spouse 2': '@I6000000089090979886@',
                    'Spouse 1 Name': 'Eric',
                    'Spouse 2 Name': 'Sunny /Wood/',
                    'Divorced': 'NA'
                },
                '3': {
                    'Children': {
                        '@I6000000089090979811@',
                        '@I6000000089090979822@'
                    },
                    'Married': '3 JUL 1990',
                    'Spouse 1': '@I6000000089090867827@',
                    'Spouse 2': '@I6000000089090979886@',
                    'Spouse 1 Name': 'Frank',
                    'Spouse 2 Name': 'Jenny /Wood/',
                    'Divorced': 'NA'
                }
            }
        }

        errors = set()
        errors = unique_family_spouse_marriage_date(parsed_file, errors)

        for e in errors:
            print(e.getErrMsg())

        self.assertEqual(len(errors), 0, msg='The len of errors should be 0.')

    def test_unique_family_spouses_name(self):
        print('US24: No more than one family with the same spouses by name in a GEDCOM file')
        parsed_file = {
            'family': {
                '1': {
                    'Children': {
                        '@c@',
                        '@d@'
                    },
                    'Married': '1 JUL 1990',
                    'Spouse 1': '@a@',
                    'Spouse 2': '@b@',
                    'Spouse 1 Name': 'Brian',
                    'Spouse 2 Name': 'Jane Lancing /Smith/',
                    'Divorced': 'NA'
                },
                '2': {
                    'Children': {
                        '@I6000000089090979883@',
                        '@I6000000089090979871@'
                    },
                    'Married': '2 JUL 1990',
                    'Spouse 1': '@I6000000089090867827@',
                    'Spouse 2': '@I6000000089090979886@',
                    'Spouse 1 Name': 'Eric',
                    'Spouse 2 Name': 'Sunny /Wood/',
                    'Divorced': 'NA'
                },
                '3': {
                    'Children': {
                        '@I6000000089090979811@',
                        '@I6000000089090979822@'
                    },
                    'Married': '3 JUL 1990',
                    'Spouse 1': '@I6000000089090867827@',
                    'Spouse 2': '@I6000000089090979886@',
                    'Spouse 1 Name': 'Jane Lancing /Smith/',
                    'Spouse 2 Name': 'Brian',
                    'Divorced': 'NA'
                }
            }
        }

        errors = set()
        errors = unique_family_spouse_marriage_date(parsed_file, errors)

        for e in errors:
            print(e.getErrMsg())

        self.assertEqual(len(errors), 1, msg='The len of errors should be 1.')

    def test_unique_family_marriage_date(self):
        print('US24: No more than one family with the same marriage date should appear in a GEDCOM file')

        parsed_file = {
            'family': {
                '1': {
                    'Children': {
                        '@c@',
                        '@d@'
                    },
                    'Married': '1 JUL 1990',
                    'Spouse 1': '@a@',
                    'Spouse 2': '@b@',
                    'Spouse 1 Name': 'Brian',
                    'Spouse 2 Name': 'Jane Lancing /Smith/',
                    'Divorced': 'NA'
                },
                '2': {
                    'Children': {
                        '@I6000000089090979883@',
                        '@I6000000089090979871@'
                    },
                    'Married': '2 JUL 1990',
                    'Spouse 1': '@I6000000089090867827@',
                    'Spouse 2': '@I6000000089090979886@',
                    'Spouse 1 Name': 'Eric',
                    'Spouse 2 Name': 'Sunny /Wood/',
                    'Divorced': 'NA'
                },
                '3': {
                    'Children': {
                        '@I6000000089090979811@',
                        '@I6000000089090979822@'
                    },
                    'Married': '1 JUL 1990',
                    'Spouse 1': '@I6000000089090867827@',
                    'Spouse 2': '@I6000000089090979886@',
                    'Spouse 1 Name': 'Frank',
                    'Spouse 2 Name': 'Jenny /Wood/',
                    'Divorced': 'NA'
                }
            }
        }

        errors = set()
        errors = unique_family_spouse_marriage_date(parsed_file, errors)

        for e in errors:
            print(e.getErrMsg())

        self.assertEqual(len(errors), 1, msg='The len of errors should be 1.')

if __name__ == '__main__':
    unittest.main()