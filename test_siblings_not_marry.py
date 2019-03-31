import unittest
from siblings_not_marry import siblings_not_marry

class TestSiblingsNotMarry(unittest.TestCase):
    def test_valid(self):
        print("Siblings should not marry one another (valid):")
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
                        'Birthday': '21 SEP 1756',
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
                        'Name': 'Brian',
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
                        'Name': 'Brian',
                        'Gender': 'M',
                        'Birthday': '21 SEP 1756',
                        'Death': 'NA',
                        'Alive?': 'Y',
                        'Age': 262
                    },
                    '@d@': {
                        'ID': '@d@',
                        'Child': 'NA',
                        'Spouse': 'NA',
                        'Name': 'Brian',
                        'Gender': 'M',
                        'Birthday': '21 SEP 1756',
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
                        'Name': 'Brian',
                        'Gender': 'M',
                        'Birthday': '21 SEP 1756',
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
                        'Name': 'Brian',
                        'Gender': 'M',
                        'Birthday': '21 SEP 1756',
                        'Death': 'NA',
                        'Alive?': 'Y',
                        'Age': 262
                    },
                    '@I6000000089090979883@': {
                        'ID': '@I6000000089090979883@',
                        'Child': 'NA',
                        'Spouse': 'NA',
                        'Name': 'Brian',
                        'Gender': 'M',
                        'Birthday': '21 SEP 1756',
                        'Death': 'NA',
                        'Alive?': 'Y',
                        'Age': 262
                    },
                    '@I6000000089090979871@': {
                        'ID': '@I6000000089090979871@',
                        'Child': 'NA',
                        'Spouse': 'NA',
                        'Name': 'Brian',
                        'Gender': 'M',
                        'Birthday': '21 SEP 1756',
                        'Death': 'NA',
                        'Alive?': 'Y',
                        'Age': 262
                    }
                }
            }
        errors = set()
        errors = siblings_not_marry(valid_parsed_file, errors)
        self.assertEqual(len(errors), 0, msg='The len of errors should be 0.')
        for e in errors:
            print(e.getErrMsg())

    def test_invalid(self):
        print("Siblings should not marry one another (invalid):")
        invalid_parsed_file = {
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
                    'Spouse 1': '@c@',
                    'Spouse 2': '@d@',
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
                    'Birthday': '21 SEP 1756',
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
                    'Name': 'Brian',
                    'Gender': 'M',
                    'Birthday': '21 SEP 1756',
                    'Death': 'NA',
                    'Alive?': 'Y',
                    'Age': 262
                },
                '@c@': {
                    'ID': '@c@',
                    'Child': {
                        '@I6000000089090979883@',
                        '@I6000000089090979871@'},
                    'Spouse': '@d@',
                    'Name': 'Brian',
                    'Gender': 'M',
                    'Birthday': '21 SEP 1756',
                    'Death': 'NA',
                    'Alive?': 'Y',
                    'Age': 262
                },
                '@d@': {
                    'ID': '@d@',
                    'Child': {
                        '@I6000000089090979883@',
                        '@I6000000089090979871@'
                    },
                    'Spouse': '@c@',
                    'Name': 'Brian',
                    'Gender': 'F',
                    'Birthday': '21 SEP 1756',
                    'Death': 'NA',
                    'Alive?': 'Y',
                    'Age': 262
                },
                '@I6000000089090979883@': {
                    'ID': '@I6000000089090979883@',
                    'Child': 'NA',
                    'Spouse': 'NA',
                    'Name': 'Brian',
                    'Gender': 'M',
                    'Birthday': '21 SEP 1756',
                    'Death': 'NA',
                    'Alive?': 'Y',
                    'Age': 262
                },
                '@I6000000089090979871@': {
                    'ID': '@I6000000089090979871@',
                    'Child': 'NA',
                    'Spouse': 'NA',
                    'Name': 'Brian',
                    'Gender': 'M',
                    'Birthday': '21 SEP 1756',
                    'Death': 'NA',
                    'Alive?': 'Y',
                    'Age': 262
                }
            }
        }
        errors = set()
        errors = siblings_not_marry(invalid_parsed_file, errors)
        self.assertEqual(len(errors), 1, msg='The len of errors should be 1.')
        for e in errors:
            print(e.getErrMsg())

if __name__ == '__main__':
    unittest.main()
