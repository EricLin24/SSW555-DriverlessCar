import unittest
from lessthan_150 import less_than_150
import Error

class TestLessThan150(unittest.TestCase):
    def test_no_parameter(self):
        errors = set()
        errors = less_than_150('', errors)
        self.assertEqual(len(errors), 0, msg='No parameter input but not a error')

    def test_alive_less_than_150(self):
        member1 = {'Name': 'Mary Frances /Napier/', 'Birthday': '27 DEC 1930', 'Death':'NA'}
        member2 = {'Name': 'RoseMary /Anderson/', 'Birthday': '5 MAY 1958', 'Death': 'NA'}
        errors = set()
        error1 = less_than_150(member1, errors)
        error2 = less_than_150(member2, errors)
        self.assertEqual(len(error1), 0, msg='No error found')
        self.assertEqual(len(error2), 0, msg='No error found')

    def test_dead_less_than_150(self):
        member1 = {'Name': 'Mary Frances /Napier/', 'Birthday': '1 MAY 1869', 'Death': '15 FEB 2019'}
        member2 = {'Name': 'RoseMary /Anderson/', 'Birthday': '20 APR 1994', 'Death': '2 OCT 2016'}
        errors = set()
        error1 = less_than_150(member1, errors)
        error2 = less_than_150(member2, errors)
        self.assertEqual(len(error1), 0, msg='No error found')
        self.assertEqual(len(error2), 0, msg='No error found')

    def test_alive_more_than_150(self):
        member1 = {'Name': 'RoseMary /Anderson/', 'Birthday': '1 MAY 1865', 'Death': 'NA'}
        #member2 = {'Birthday': '1 MAY 1860', 'Death': 'NA'}
        errors = set()
        errors = less_than_150(member1, errors)
        #error2 = less_than_150(member2, errors)
        for err in errors:
            self.assertEqual(err.errCode, Error.ErrorEnum.US07, msg='Failed to generate US07 error')
        #self.assertEqual(less_than_150(member2)[0], False, msg='Result should be false')

    def test_dead_more_than_150(self):
        member1 = {'Name': 'RoseMary /Anderson/', 'Birthday': '1 MAY 1860', 'Death': '15 MAR 2019'}
        #member2 = {'Birthday': '1 MAY 1860', 'Death': '2 OCT 2016'}
        errors = set()
        errors = less_than_150(member1, errors)
        for err in errors:
            self.assertEqual(err.errCode, Error.ErrorEnum.US07, msg='Failed to generate US07 error')
        #self.assertEqual(less_than_150(member2)[0], False, msg='Result should be false')

if __name__ == '__main__':
    unittest.main()