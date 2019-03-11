# TestFamilyValidation.py 

# Unit Test for FamilyValidation
import FamilyValidation
import unittest
import Error

class TestFamilyValidation(unittest.TestCase):
    def test_check_multiple_births_valid(self):
        print('Testing family with < 5 multiple births...')

        validParsedFile = {'family': {'@F6000000086661172986@': {'Children': {'@I6000000086661584835@'}, 
                        'Married': '15 MAR 1982', 'Spouse 1': '@I6000000086661172981@', 'Spouse 2': '@I6000000086661506862@', 
                        'Spouse 1 Name': 'Brian /Smith/', 'Spouse 2 Name': 'Rebecca /Smith/', 'Divorced': 'NA'}}, 
                        'members': {'@I6000000086661584835@': {'ID': '@I6000000086661584835@', 'Child': {'@F6000000086661172986@'}, 
                        'Spouse': 'NA', 'Name': 'George /Smith/', 'Gender': 'M', 'Birthday': '2 JAN 1987', 'Death': 'NA', 'Alive?': 'Y', 
                        'Age': 32}, '@I6000000086661172981@': {'ID': '@I6000000086661172981@', 'Child': 'NA', 
                        'Spouse': {'@F6000000086661172986@'}, 'Name': 'Brian /Smith/', 'Gender': 'M', 'Birthday': '21 SEP 1956', 
                        'Death': 'NA', 'Alive?': 'Y', 'Age': 62}, '@I6000000086661506862@': {'ID': '@I6000000086661506862@', 
                        'Child': {'@F6000000086661201064@'}, 'Spouse': {'@F6000000086661172986@'}, 'Name': 'Rebecca /Smith/', 
                        'Gender': 'F', 'Birthday': '13 MAY 1972', 'Death': 'NA', 'Alive?': 'Y', 'Age': 46}}}

        errors = set()

        errors = FamilyValidation.check_multiple_births(validParsedFile, errors)

        self.assertEqual(len(errors), 0, msg='Failed to check valid family for multiple births')

    def test_check_multiple_births_invalid(self):
        print('Testing family with > 5 multiple births...')

        invaliParsedFile = {'family': {'@F6000000089090979889@': {'Children': {'@I6000000089090979883@', '@I6000000089090979871@', 
                        '@I6000000089090979874@', '@I6000000089090979891@', '@I6000000089090979877@', '@I6000000089090979880@'}, 
                        'Married': '4 JUL 1990', 'Spouse 1': '@I6000000089090867827@', 'Spouse 2': '@I6000000089090979886@', 
                        'Spouse 1 Name': 'Brian', 'Spouse 2 Name': 'Jane Lancing /Smith/', 'Divorced': 'NA'}}, 
                        'members': {'@I6000000089090867827@': {'ID': '@I6000000089090867827@', 'Child': 'NA', 
                            'Spouse': {'@F6000000089090867863@', '@F6000000089090979889@'}, 
                            'Name': 'Brian', 'Gender': 'M', 'Birthday': '21 SEP 1756', 
                            'Death': 'NA', 'Alive?': 'Y', 'Age': 262}, 
                        '@I6000000089090979886@': {'ID': '@I6000000089090979886@', 'Child': 'NA', 
                            'Spouse': {'@F6000000089090979889@'}, 
                            'Name': 'Jane Lancing /Smith/', 'Gender': 'F', 'Birthday': '12 APR 1959', 
                            'Death': 'NA', 'Alive?': 'Y', 'Age': 59}, 
                        '@I6000000089090979891@': {'ID': '@I6000000089090979891@', 'Child': {'@F6000000089090979889@'}, 
                            'Spouse': 'NA', 'Name': 'Jason /Smith/', 'Gender': 'M', 'Birthday': '15 AUG 1990', 
                            'Death': 'NA', 'Alive?': 'Y', 'Age': 28}, 
                        '@I6000000089090979871@': {'ID': '@I6000000089090979871@', 'Child': {'@F6000000089090979889@'}, 
                            'Spouse': 'NA', 'Name': 'Jackson /Smith/', 'Gender': 'M', 'Birthday': '15 AUG 1990', 
                            'Death': 'NA', 'Alive?': 'Y', 'Age': 28}, 
                        '@I6000000089090979880@': {'ID': '@I6000000089090979880@', 'Child': {'@F6000000089090979889@'}, 
                            'Spouse': 'NA', 'Name': 'Janet /Smith/', 'Gender': 'F', 'Birthday': '15 AUG 1990', 
                            'Death': 'NA', 'Alive?': 'Y', 'Age': 28}, 
                        '@I6000000089090979877@': {'ID': '@I6000000089090979877@', 'Child': {'@F6000000089090979889@'}, 
                            'Spouse': 'NA', 'Name': 'Jasmine /Smith/', 'Gender': 'F', 'Birthday': '15 AUG 1990', 
                            'Death': 'NA', 'Alive?': 'Y', 'Age': 28}, 
                         '@I6000000089090979874@': {'ID': '@I6000000089090979874@', 'Child': {'@F6000000089090979889@'}, 
                            'Spouse': 'NA', 'Name': 'Jamie /Smith/', 'Gender': 'F', 'Birthday': '15 AUG 1990', 
                            'Death': 'NA', 'Alive?': 'Y', 'Age': 28}, 
                         '@I6000000089090979883@': {'ID': '@I6000000089090979883@', 'Child': {'@F6000000089090979889@'}, 
                            'Spouse': 'NA', 'Name': 'Joel /Smith/', 'Gender': 'M', 'Birthday': '15 AUG 1990', 
                            'Death': 'NA', 'Alive?': 'Y', 'Age': 28} }}

        errors = set()
        errors = FamilyValidation.check_multiple_births(invaliParsedFile, errors)

        for err in errors:
            self.assertEqual(err.errCode, Error.ErrorEnum.US14, msg='Failed to generate US14 error')

if __name__ == '__main__':
    unittest.main()