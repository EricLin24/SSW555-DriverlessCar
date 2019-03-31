import unittest
import no_marriage_to_children

class TestSameFamilyChildrenMarriage(unittest.TestCase):
    
    def setUp(self):
        self.parsed_file1 = {
        'family' : { '@F6000000056297358922@' : {'Children': {'@I6000000085762947144@', '@I6000000085762947145@'}, 'Married': '28 AUG 1949', 'Spouse 1':             '@I6000000085762947143@', 'Spouse 2': '@I6000000085762947142@', 'Spouse 1 Name': 'Enrique /Martinez/', 'Spouse 2 Name': 'Sonia /Martinez/', 'Divorced': 'NA'},
        '@F6000000089090867863@' : {'Children': {'@I6000000089090475678@', '@I6000000089090478876@', '@I6000000089090475940@'}, 'Married': '15 MAR 1982', 'Spouse 1': '@I6000000089090867827@', 'Spouse 2': '@I6000000089090867831@', 'Spouse 1 Name': 'Brian', 'Spouse 2 Name': 'Rebecca', 'Divorced': 'NA'}},
        'members': { '@I6000000085762947144@':{'ID': '@I6000000085762947144@', 'Child': {'@F6000000056297358922@'}, 'Spouse': 'NA', 'Name': 'Gilbert /Martinez/', 'Gender': 'M', 'Birthday': '30 APR 2002', 'Death': 'NA', 'Alive?': 'Y', 'Age': 16}, 
        '@I6000000085762947145@': {'ID': '@I6000000085762947145@', 'Child': {'@F6000000056297358922@'}, 'Spouse': 'NA', 'Name': 'Jenny /Martinez/', 'Gender': 'F', 'Birthday': '15 JUL 2011', 'Death': 'NA', 'Alive?': 'Y', 'Age': 7},
        '@I6000000089090475678@': {'ID': '@I6000000089090475678@', 'Child': {'@F6000000089090867863@'}, 'Spouse': 'NA', 'Name': 'Gregory /Smith/', 'Gender': 'M', 'Birthday': '?? OCT 1984', 'Death': 'NA', 'Alive?': 'Y', 'Age': 'Unknown'},
        '@I6000000089090478876@': {'ID': '@I6000000089090478876@', 'Child': {'@F6000000089090867863@'}, 'Spouse': 'NA', 'Name': 'Gage /Smith/', 'Gender': 'M', 'Birthday': '2 JAN 1982', 'Death': 'NA', 'Alive?': 'Y', 'Age': 37},
        '@I6000000089090475940@': {'ID': '@I6000000089090475940@', 'Child': {'@F6000000089090867863@'}, 'Spouse': 'NA', 'Name': 'George /Smith/', 'Gender': 'M', 'Birthday': '2 JAN 1982', 'Death': 'NA', 'Alive?': 'Y', 'Age': 37},}   }
        
        self.parsed_file2 = {
        'family' : { '@F6000000056297358922@' : {'Children': {'@I6000000085762947144@', '@I6000000085762947145@'}, 'Married': '28 AUG 1949', 'Spouse 1':             '@I6000000085762947143@', 'Spouse 2': '@I6000000085762947142@', 'Spouse 1 Name': 'Enrique /Martinez/', 'Spouse 2 Name': 'Sonia /Martinez/', 'Divorced': 'NA'},
        '@F6000000089090867863@' : {'Children': {'@I6000000089090475678@', '@I6000000089090478876@', '@I6000000089090475940@'}, 'Married': '15 MAR 1982', 'Spouse 1': '@I6000000089090867827@', 'Spouse 2': '@I6000000089090867831@', 'Spouse 1 Name': 'Brian', 'Spouse 2 Name': 'Rebecca', 'Divorced': 'NA'}},
        'members': { '@I6000000085762947144@':{'ID': '@I6000000085762947144@', 'Child': {'@F6000000056297358922@'}, 'Spouse': {'@I6000000085762947145@'}, 'Name': 'Gilbert /Martinez/', 'Gender': 'M', 'Birthday': '30 APR 2002', 'Death': 'NA', 'Alive?': 'Y', 'Age': 16}, 
        '@I6000000085762947145@': {'ID': '@I6000000085762947145@', 'Child': {'@F6000000056297358922@'}, 'Spouse': {'@I6000000085762947144@'}, 'Name': 'Jenny /Martinez/', 'Gender': 'F', 'Birthday': '15 JUL 2011', 'Death': 'NA', 'Alive?': 'Y', 'Age': 7},
        '@I6000000089090475678@': {'ID': '@I6000000089090475678@', 'Child': {'@F6000000089090867863@'}, 'Spouse': 'NA', 'Name': 'Gregory /Smiths/', 'Gender': 'M', 'Birthday': '?? OCT 1984', 'Death': 'NA', 'Alive?': 'Y', 'Age': 'Unknown'},
        '@I6000000089090478876@': {'ID': '@I6000000089090478876@', 'Child': {'@F6000000089090867863@'}, 'Spouse': 'NA', 'Name': 'Gage /Smith/', 'Gender': 'M', 'Birthday': '2 JAN 1982', 'Death': 'NA', 'Alive?': 'Y', 'Age': 37},
        '@I6000000089090475940@': {'ID': '@I6000000089090475940@', 'Child': {'@F6000000089090867863@'}, 'Spouse': 'NA', 'Name': 'George /Smith/', 'Gender': 'M', 'Birthday': '2 JAN 1982', 'Death': 'NA', 'Alive?': 'Y', 'Age': 37},
            }   
        }

        
    def test_children_marriage1(self):
        errors = set()
        no_marriage_to_children.no_marriage_to_children(self.parsed_file1, errors)
        self.assertEqual(len(errors), 0,
                         msg=str([err.getErrMsg() for err in errors]))

    def test_children_marriage2(self):
        errors = set()
        no_marriage_to_children.no_marriage_to_children(self.parsed_file2, errors)
        self.assertEqual(len(errors), 2,
                         msg='Failed to find marriages to children')


if __name__ == '__main__':
    unittest.main(exit=False, verbosity=2)

