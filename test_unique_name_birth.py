import Error
import unittest
from unique_name_birth import unique_name_and_birth

class TestUniqueNameAndBirth(unittest.TestCase):
    def test_valid_unique_name_and_birth(self):
        print('US23: No more than one individual with the same name and birth date should appear in a GEDCOM file (valid).')
        valid_parsed_file = {
            'family': {
                '1': {
                    'Children': {
                        '@c@',
                        '@d@'
                    },
                    'Married': '4 JUL 1990',
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
                    'Married': '4 JUL 1990',
                    'Spouse 1': '@I6000000089090867827@',
                    'Spouse 2': '@I6000000089090979886@',
                    'Spouse 1 Name': 'Eric',
                    'Spouse 2 Name': 'Sunny /Wood/',
                    'Divorced': 'NA'
                }},
            'members': {
                '@a@': {
                    'ID': '@a@',
                    'Child': {
                        '@c@',
                        '@d@'
                    },
                    'Spouse': {
                        '@b@'
                    },
                    'Name': 'Brian',
                    'Gender': 'M',
                    'Birthday': '20 SEP 1756',
                    'Death': 'NA',
                    'Alive?': 'Y',
                    'Age': 262
                },
                '@b@': {
                    'ID': '@b@',
                    'Child': {
                        '@c@',
                        '@d@'
                    },
                    'Spouse': {
                        '@a@'
                    },
                    'Name': 'Jane Lancing /Smith/',
                    'Gender': 'M',
                    'Birthday': '21 SEP 1756',
                    'Death': 'NA',
                    'Alive?': 'Y',
                    'Age': 262
                },
                '@c@': {
                    'ID': '@c@',
                    'Child': 'NA',
                    'Spouse': 'NA',
                    'Name': 'Drian',
                    'Gender': 'M',
                    'Birthday': '22 SEP 1756',
                    'Death': 'NA',
                    'Alive?': 'Y',
                    'Age': 262
                },
                '@d@': {
                    'ID': '@d@',
                    'Child': 'NA',
                    'Spouse': 'NA',
                    'Name': 'Erian',
                    'Gender': 'M',
                    'Birthday': '23 SEP 1756',
                    'Death': 'NA',
                    'Alive?': 'Y',
                    'Age': 262
                },
                '@I6000000089090867827@': {
                    'ID': '@I6000000089090867827@',
                    'Child': {
                        '@I6000000089090979883@',
                        '@I6000000089090979871@'
                    },
                    'Spouse': {
                        '@I6000000089090979886@'
                    },
                    'Name': 'Eric',
                    'Gender': 'M',
                    'Birthday': '24 SEP 1756',
                    'Death': 'NA',
                    'Alive?': 'Y',
                    'Age': 262
                },
                '@I6000000089090979886@': {
                    'ID': '@I6000000089090979886@',
                    'Child': {
                        '@I6000000089090979883@',
                        '@I6000000089090979871@'
                    },
                    'Spouse': {
                        '@I6000000089090867827@'
                    },
                    'Name': 'Frian',
                    'Gender': 'M',
                    'Birthday': '25 SEP 1756',
                    'Death': 'NA',
                    'Alive?': 'Y',
                    'Age': 262
                },
                '@I6000000089090979883@': {
                    'ID': '@I6000000089090979883@',
                    'Child': 'NA',
                    'Spouse': 'NA',
                    'Name': 'Grian',
                    'Gender': 'M',
                    'Birthday': '26 SEP 1756',
                    'Death': 'NA',
                    'Alive?': 'Y',
                    'Age': 262
                },
                '@I6000000089090979871@': {
                    'ID': '@I6000000089090979871@',
                    'Child': 'NA',
                    'Spouse': 'NA',
                    'Name': 'Sunny /Wood/',
                    'Gender': 'M',
                    'Birthday': '27 SEP 1756',
                    'Death': 'NA',
                    'Alive?': 'Y',
                    'Age': 262
                }
            }
        }
        errors = set()
        errors = unique_name_and_birth(valid_parsed_file, errors)
        for e in errors:
            print(e.getErrMsg())
        self.assertEqual(len(errors), 0, msg='The len of errors should be 0')

    def test_unique_name_and_birth_invalid_name(self):
        print('US23: No more than one individual with the same name and birth date should appear in a GEDCOM file (invalid name).')

        parse_file = {
            'family': {
                '1': {
                    'Children': {
                        '@c@',
                        '@d@'
                    },
                    'Married': '4 JUL 1990',
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
                    'Married': '4 JUL 1990',
                    'Spouse 1': '@I6000000089090867827@',
                    'Spouse 2': '@I6000000089090979886@',
                    'Spouse 1 Name': 'Eric',
                    'Spouse 2 Name': 'Sunny /Wood/',
                    'Divorced': 'NA'
                }},
            'members': {
                '@a@': {
                    'ID': '@a@',
                    'Child': {
                        '@c@',
                        '@d@'
                    },
                    'Spouse': {
                        '@b@'
                    },
                    'Name': 'Brian',
                    'Gender': 'M',
                    'Birthday': '20 SEP 1756',
                    'Death': 'NA',
                    'Alive?': 'Y',
                    'Age': 262
                },
                '@b@': {
                    'ID': '@b@',
                    'Child': {
                        '@c@',
                        '@d@'
                    },
                    'Spouse': {
                        '@a@'
                    },
                    'Name': 'Jane Lancing /Smith/',
                    'Gender': 'M',
                    'Birthday': '21 SEP 1756',
                    'Death': 'NA',
                    'Alive?': 'Y',
                    'Age': 262
                },
                '@c@': {
                    'ID': '@c@',
                    'Child': 'NA',
                    'Spouse': 'NA',
                    'Name': 'Drian',
                    'Gender': 'M',
                    'Birthday': '22 SEP 1756',
                    'Death': 'NA',
                    'Alive?': 'Y',
                    'Age': 262
                },
                '@d@': {
                    'ID': '@d@',
                    'Child': 'NA',
                    'Spouse': 'NA',
                    'Name': 'Erian',
                    'Gender': 'M',
                    'Birthday': '23 SEP 1756',
                    'Death': 'NA',
                    'Alive?': 'Y',
                    'Age': 262
                },
                '@I6000000089090867827@': {
                    'ID': '@I6000000089090867827@',
                    'Child': {
                        '@I6000000089090979883@',
                        '@I6000000089090979871@'
                    },
                    'Spouse': {
                        '@I6000000089090979886@'
                    },
                    'Name': 'Eric',
                    'Gender': 'M',
                    'Birthday': '24 SEP 1756',
                    'Death': 'NA',
                    'Alive?': 'Y',
                    'Age': 262
                },
                '@I6000000089090979886@': {
                    'ID': '@I6000000089090979886@',
                    'Child': {
                        '@I6000000089090979883@',
                        '@I6000000089090979871@'
                    },
                    'Spouse': {
                        '@I6000000089090867827@'
                    },
                    'Name': 'Frian',
                    'Gender': 'M',
                    'Birthday': '25 SEP 1756',
                    'Death': 'NA',
                    'Alive?': 'Y',
                    'Age': 262
                },
                '@I6000000089090979883@': {
                    'ID': '@I6000000089090979883@',
                    'Child': 'NA',
                    'Spouse': 'NA',
                    'Name': 'Drian',
                    'Gender': 'M',
                    'Birthday': '26 SEP 1756',
                    'Death': 'NA',
                    'Alive?': 'Y',
                    'Age': 262
                },
                '@I6000000089090979871@': {
                    'ID': '@I6000000089090979871@',
                    'Child': 'NA',
                    'Spouse': 'NA',
                    'Name': 'Sunny /Wood/',
                    'Gender': 'M',
                    'Birthday': '27 SEP 1756',
                    'Death': 'NA',
                    'Alive?': 'Y',
                    'Age': 262
                }
            }
        }

        errors = set()
        errors = unique_name_and_birth(parse_file, errors)
        for e in errors:
            print(e.getErrMsg())
        self.assertEqual(len(errors), 1, msg='The len of errors should be 1.')

    def test_unique_name_and_birth_invalid_birth(self):
        print('US23: No more than one individual with the same name and birth date should appear in a GEDCOM file (invalid '
              'birth date).')
        parsed_file = {
            'family': {
                '1': {
                    'Children': {
                        '@c@',
                        '@d@'
                    },
                    'Married': '4 JUL 1990',
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
                    'Married': '4 JUL 1990',
                    'Spouse 1': '@I6000000089090867827@',
                    'Spouse 2': '@I6000000089090979886@',
                    'Spouse 1 Name': 'Eric',
                    'Spouse 2 Name': 'Sunny /Wood/',
                    'Divorced': 'NA'
                }},
            'members': {
                '@a@': {
                    'ID': '@a@',
                    'Child': {
                        '@c@',
                        '@d@'
                    },
                    'Spouse': {
                        '@b@'
                    },
                    'Name': 'Brian',
                    'Gender': 'M',
                    'Birthday': '20 SEP 1756',
                    'Death': 'NA',
                    'Alive?': 'Y',
                    'Age': 262
                },
                '@b@': {
                    'ID': '@b@',
                    'Child': {
                        '@c@',
                        '@d@'
                    },
                    'Spouse': {
                        '@a@'
                    },
                    'Name': 'Jane Lancing /Smith/',
                    'Gender': 'M',
                    'Birthday': '21 SEP 1756',
                    'Death': 'NA',
                    'Alive?': 'Y',
                    'Age': 262
                },
                '@c@': {
                    'ID': '@c@',
                    'Child': 'NA',
                    'Spouse': 'NA',
                    'Name': 'Drian',
                    'Gender': 'M',
                    'Birthday': '22 SEP 1756',
                    'Death': 'NA',
                    'Alive?': 'Y',
                    'Age': 262
                },
                '@d@': {
                    'ID': '@d@',
                    'Child': 'NA',
                    'Spouse': 'NA',
                    'Name': 'Erian',
                    'Gender': 'M',
                    'Birthday': '23 SEP 1756',
                    'Death': 'NA',
                    'Alive?': 'Y',
                    'Age': 262
                },
                '@I6000000089090867827@': {
                    'ID': '@I6000000089090867827@',
                    'Child': {
                        '@I6000000089090979883@',
                        '@I6000000089090979871@'
                    },
                    'Spouse': {
                        '@I6000000089090979886@'
                    },
                    'Name': 'Eric',
                    'Gender': 'M',
                    'Birthday': '24 SEP 1756',
                    'Death': 'NA',
                    'Alive?': 'Y',
                    'Age': 262
                },
                '@I6000000089090979886@': {
                    'ID': '@I6000000089090979886@',
                    'Child': {
                        '@I6000000089090979883@',
                        '@I6000000089090979871@'
                    },
                    'Spouse': {
                        '@I6000000089090867827@'
                    },
                    'Name': 'Frian',
                    'Gender': 'M',
                    'Birthday': '25 SEP 1756',
                    'Death': 'NA',
                    'Alive?': 'Y',
                    'Age': 262
                },
                '@I6000000089090979883@': {
                    'ID': '@I6000000089090979883@',
                    'Child': 'NA',
                    'Spouse': 'NA',
                    'Name': 'Grian',
                    'Gender': 'M',
                    'Birthday': '26 SEP 1756',
                    'Death': 'NA',
                    'Alive?': 'Y',
                    'Age': 262
                },
                '@I6000000089090979871@': {
                    'ID': '@I6000000089090979871@',
                    'Child': 'NA',
                    'Spouse': 'NA',
                    'Name': 'Sunny /Wood/',
                    'Gender': 'M',
                    'Birthday': '21 SEP 1756',
                    'Death': 'NA',
                    'Alive?': 'Y',
                    'Age': 262
                }
            }
        }

        errors = set()
        errors = unique_name_and_birth(parsed_file, errors)
        self.assertEqual(len(errors), 1, msg='The len of errors should be 1.')
        for e in errors:
            print(e.getErrMsg())

if __name__ == '__main__':
    unittest.main()