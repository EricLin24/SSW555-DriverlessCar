# TestDeseasedIndividuals.py

# Unit test for the list_deseased_individuals
import DeseasedIndividuals
import unittest

class TestDeseasedIndividauls(unittest.TestCase):
    def test_list_deseased(self):
        print('US29: Testing listing deseased individuals')
        parsed_file = {'family': {'@F6000000086661172986@': {'Children': {'@I6000000086661584835@'}, 
                        'Married': '15 MAR 1982', 'Spouse 1': '@I6000000086661172981@', 'Spouse 2': '@I6000000086661506862@', 
                        'Spouse 1 Name': 'Brian /Smith/', 'Spouse 2 Name': 'Rebecca /Smith/', 'Divorced': 'NA'}}, 
                        'members': {'@I6000000086661584835@': {'ID': '@I6000000086661584835@', 'Child': {'@F6000000086661172986@'}, 
                        'Spouse': 'NA', 'Name': 'George /Smith/', 'Gender': 'M', 'Birthday': '2 JAN 1987', 'Death': '3 MAR 2019', 'Alive?': 'N', 
                        'Age': 32}, '@I6000000086661172981@': {'ID': '@I6000000086661172981@', 'Child': 'NA', 
                        'Spouse': {'@F6000000086661172986@'}, 'Name': 'Brian /Smith/', 'Gender': 'M', 'Birthday': '21 SEP 1956', 
                        'Death': '12 DEC 2017', 'Alive?': 'N', 'Age': 60}, '@I6000000086661506862@': {'ID': '@I6000000086661506862@', 
                        'Child': {'@F6000000086661201064@'}, 'Spouse': {'@F6000000086661172986@'}, 'Name': 'Rebecca /Smith/', 
                        'Gender': 'F', 'Birthday': '13 MAY 1972', 'Death': 'NA', 'Alive?': 'Y', 'Age': 46}}}

        expectedDeseasedDict = {'@I6000000086661584835@':{'Name': 'George /Smith/', 'Birthday': '2 JAN 1987', 'Death': '3 MAR 2019', 'Age': 32},
                                '@I6000000086661172981@':{'Name': 'Brian /Smith/', 'Birthday': '21 SEP 1956', 'Death': '12 DEC 2017', 'Age': 60}}

        result = DeseasedIndividuals.list_deseased_individuals(parsed_file)

        deseased_list = result['deseased']

        self.assertEqual(len(expectedDeseasedDict), len(deseased_list), msg='Error: sorted deseased list size does not match expected')

if __name__ == '__main__':
    unittest.main()
