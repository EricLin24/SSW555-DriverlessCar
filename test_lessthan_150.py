import unittest
from lessthan_150 import less_than_150

class TestLessThan150(unittest.TestCase):
    def test_invalid_parameter(self):
        self.assertEqual(less_than_150('testcases'), -1, msg='The parameter inputed is invalid, should be a dict')

    def test_alive_less_than_150(self):
        member1 = {'Birthday': '27 DEC 1930', 'Death':'NA'}
        member2 = {'Birthday': '5 MAY 1958', 'Death': 'NA'}
        self.assertEqual(less_than_150(member1), True, msg='Result should be true')
        self.assertEqual(less_than_150(member2), True, msg='Result should be true')

    def test_dead_less_than_150(self):
        member1 = {'Birthday': '1 MAY 1869', 'Death': '15 FEB 2019'}
        member2 = {'Birthday': '20 APR 1994', 'Death': '2 OCT 2016'}
        self.assertEqual(less_than_150(member1), True, msg='Result should be true')
        self.assertEqual(less_than_150(member2), True, msg='Result should be true')

    def test_alive_more_than_150(self):
        member1 = {'Birthday': '1 MAY 1865', 'Death': 'NA'}
        member2 = {'Birthday': '1 MAY 1860', 'Death': 'NA'}
        self.assertEqual(less_than_150(member1), False, msg='Result should be false')
        self.assertEqual(less_than_150(member2), False, msg='Result should be false')

    def test_dead_more_than_150(self):
        member1 = {'Birthday': '1 MAY 1860', 'Death': '15 MAR 2019'}
        member2 = {'Birthday': '1 MAY 1860', 'Death': '2 OCT 2016'}
        self.assertEqual(less_than_150(member1), False, msg='Result should be false')
        self.assertEqual(less_than_150(member2), False, msg='Result should be false')

if __name__ == '__main__':
    unittest.main()