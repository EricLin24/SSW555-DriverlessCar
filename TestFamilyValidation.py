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

    def test_order_siblings_by_age(self):
        print('Testing sorting siblings by age...')

        validParsedFile = {'family': {'@F6000000089090979889@': {'Children': {'@I6000000089090979883@', '@I6000000089090979871@', 
                        '@I6000000089090979874@', '@I6000000089090979891@', '@I6000000089090979877@', '@I6000000089090979880@'}, 
                        'Married': '4 JUL 1990', 'Spouse 1': '@I6000000089090867827@', 'Spouse 2': '@I6000000089090979886@', 
                        'Spouse 1 Name': 'Brian', 'Spouse 2 Name': 'Jane Lancing /Smith/', 'Divorced': 'NA'}}, 
                        'members': {'@I6000000089090867827@': {'ID': '@I6000000089090867827@', 'Child': 'NA', 
                            'Spouse': {'@F6000000089090867863@', '@F6000000089090979889@'}, 
                            'Name': 'Brian', 'Gender': 'M', 'Birthday': '21 SEP 1956', 
                            'Death': 'NA', 'Alive?': 'Y', 'Age': 62}, 
                        '@I6000000089090979886@': {'ID': '@I6000000089090979886@', 'Child': 'NA', 
                            'Spouse': {'@F6000000089090979889@'}, 
                            'Name': 'Jane Lancing /Smith/', 'Gender': 'F', 'Birthday': '12 APR 1959', 
                            'Death': 'NA', 'Alive?': 'Y', 'Age': 59}, 
                        '@I6000000089090979891@': {'ID': '@I6000000089090979891@', 'Child': {'@F6000000089090979889@'}, 
                            'Spouse': 'NA', 'Name': 'Jason /Smith/', 'Gender': 'M', 'Birthday': '15 MAR 1990', 
                            'Death': 'NA', 'Alive?': 'Y', 'Age': 28}, 
                        '@I6000000089090979871@': {'ID': '@I6000000089090979871@', 'Child': {'@F6000000089090979889@'}, 
                            'Spouse': 'NA', 'Name': 'Jackson /Smith/', 'Gender': 'M', 'Birthday': '12 JUL 1989', 
                            'Death': 'NA', 'Alive?': 'Y', 'Age': 29}, 
                        '@I6000000089090979880@': {'ID': '@I6000000089090979880@', 'Child': {'@F6000000089090979889@'}, 
                            'Spouse': 'NA', 'Name': 'Janet /Smith/', 'Gender': 'F', 'Birthday': '2 APR 1993', 
                            'Death': 'NA', 'Alive?': 'Y', 'Age': 26}, 
                        '@I6000000089090979877@': {'ID': '@I6000000089090979877@', 'Child': {'@F6000000089090979889@'}, 
                            'Spouse': 'NA', 'Name': 'Jasmine /Smith/', 'Gender': 'F', 'Birthday': '30 NOV 1997', 
                            'Death': 'NA', 'Alive?': 'Y', 'Age': 22}, 
                         '@I6000000089090979874@': {'ID': '@I6000000089090979874@', 'Child': {'@F6000000089090979889@'}, 
                            'Spouse': 'NA', 'Name': 'Jamie /Smith/', 'Gender': 'F', 'Birthday': '12 JAN 2000', 
                            'Death': 'NA', 'Alive?': 'Y', 'Age': 19}, 
                         '@I6000000089090979883@': {'ID': '@I6000000089090979883@', 'Child': {'@F6000000089090979889@'}, 
                            'Spouse': 'NA', 'Name': 'Joel /Smith/', 'Gender': 'M', 'Birthday': '?? AUG 2018', 
                            'Death': 'NA', 'Alive?': 'Y', 'Age': 'Unknown'} }}

        expectedSiblingsList = [{'ID': '@I6000000089090979871@', 'Name': 'Jackson /Smith/', 'Birthday': '12 JUL 1989', 'Age': 29}, 
                                {'ID': '@I6000000089090979891@', 'Name': 'Jason /Smith/', 'Birthday': '15 MAR 1990', 'Age': 28},                            
                                {'ID': '@I6000000089090979880@', 'Name': 'Janet /Smith/', 'Birthday': '2 APR 1993', 'Age': 26}, 
                                {'ID': '@I6000000089090979877@', 'Name': 'Jasmine /Smith/', 'Birthday': '30 NOV 1997', 'Age': 22}, 
                                {'ID': '@I6000000089090979874@', 'Name': 'Jamie /Smith/', 'Birthday': '12 JAN 2000', 'Age': 19}, 
                                {'ID': '@I6000000089090979883@', 'Name': 'Joel /Smith/',  'Birthday': '?? AUG 2018', 'Age': 'Unknown'}]

        sortedSiblingsList = FamilyValidation.order_siblings_by_age(validParsedFile)

        self.assertEqual(len(expectedSiblingsList), len(sortedSiblingsList['siblings']['@F6000000089090979889@']), msg='Error: sorted siblings list size does not match expected')

        for index in range(0, len(expectedSiblingsList)):
            self.assertEqual(expectedSiblingsList[index]['Age'], sortedSiblingsList['siblings']['@F6000000089090979889@'][index]['Age'], msg='Error: siblings lists do not match')


    def test_list_multiple_births(self):
        print('Testing listing multiple births...')

        valiParsedFile = {'family': {'@F6000000089090979889@': {'Children': {'@I6000000089090979883@', '@I6000000089090979871@', 
                        '@I6000000089090979874@', '@I6000000089090979891@', '@I6000000089090979877@'}, 
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
                        '@I6000000089090979877@': {'ID': '@I6000000089090979877@', 'Child': {'@F6000000089090979889@'}, 
                            'Spouse': 'NA', 'Name': 'Jasmine /Smith/', 'Gender': 'F', 'Birthday': '15 AUG 1990', 
                            'Death': 'NA', 'Alive?': 'Y', 'Age': 28}, 
                         '@I6000000089090979874@': {'ID': '@I6000000089090979874@', 'Child': {'@F6000000089090979889@'}, 
                            'Spouse': 'NA', 'Name': 'Jamie /Smith/', 'Gender': 'F', 'Birthday': '15 AUG 1990', 
                            'Death': 'NA', 'Alive?': 'Y', 'Age': 28}, 
                         '@I6000000089090979883@': {'ID': '@I6000000089090979883@', 'Child': {'@F6000000089090979889@'}, 
                            'Spouse': 'NA', 'Name': 'Joel /Smith/', 'Gender': 'M', 'Birthday': '15 AUG 1990', 
                            'Death': 'NA', 'Alive?': 'Y', 'Age': 28} }}

        expectedMultipleList = [{'Birthday': '15 AUG 1990', 'ID': '@I6000000089090979871@', 'Name': 'Jackson /Smith/'}, 
                                {'Birthday': '15 AUG 1990', 'ID': '@I6000000089090979891@', 'Name': 'Jason /Smith/'},                            
                                {'Birthday': '15 AUG 1990', 'ID': '@I6000000089090979877@', 'Name': 'Jasmine /Smith/'}, 
                                {'Birthday': '15 AUG 1990', 'ID': '@I6000000089090979874@', 'Name': 'Jamie /Smith/'}, 
                                {'Birthday': '15 AUG 1990', 'ID': '@I6000000089090979883@', 'Name': 'Joel /Smith/'}]

        valiParsedFile = FamilyValidation.list_multiple_births(valiParsedFile)

        multiplesList = valiParsedFile['multiples']['@F6000000089090979889@']

        self.assertEqual(len(expectedMultipleList), len(multiplesList), msg='Error: multiples lists sizes do not match')            
            
if __name__ == '__main__':
    unittest.main()
