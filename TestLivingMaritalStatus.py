import LivingMaritalStatus
import unittest


class TestLivingMaritalStatus(unittest.TestCase):
    def test_living_marital_status_no_div_no_death(self):
        print('US30/US31: Testing listing living individuals marital status')
        parsedFile = {'family': {'1': {'Spouse 1': '10', 'Spouse 2': '11', 'Divorced': 'NA'},
                                 '2': {'Spouse 1': '12', 'Spouse 2': '13', 'Divorced': 'NA'}},
                      'members': {'10': {'ID': '10', 'Spouse': {'1'}, 'Death': 'NA'},
                                  '11': {'ID': '11', 'Spouse': {'1'}, 'Death': 'NA'},
                                  '12': {'ID': '12', 'Spouse': {'2'}, 'Death': 'NA'},
                                  '13': {'ID': '13', 'Spouse': {'2'}, 'Death': 'NA'},
                                  '14': {'ID': '14', 'Spouse': 'NA', 'Death': 'NA'}}}

        expected_output = {'singles': {'14': {'ID': '14', 'Spouse': 'NA', 'Death': 'NA'}},
                           'married': {'10': {'ID': '10', 'Spouse': {'1'}, 'Death': 'NA'},
                                       '11': {'ID': '11', 'Spouse': {'1'}, 'Death': 'NA'},
                                       '12': {'ID': '12', 'Spouse': {'2'}, 'Death': 'NA'},
                                       '13': {'ID': '13', 'Spouse': {'2'}, 'Death': 'NA'}}}

        self.assertEqual(expected_output, LivingMaritalStatus.list_living_married(parsedFile),
                         msg='Function did not sort singles and married properly')

    def test_living_marital_status_no_div_death(self):
        print('US30/US31: Testing listing living individuals marital status')
        parsedFile = {'family': {'1': {'Spouse 1': '10', 'Spouse 2': '11', 'Divorced': 'NA'},
                                 '2': {'Spouse 1': '12', 'Spouse 2': '13', 'Divorced': 'NA'}},
                      'members': {'10': {'ID': '10', 'Spouse': {'1'}, 'Death': '1 APR 2019'},
                                  '11': {'ID': '11', 'Spouse': {'1'}, 'Death': 'NA'},
                                  '12': {'ID': '12', 'Spouse': {'2'}, 'Death': 'NA'},
                                  '13': {'ID': '13', 'Spouse': {'2'}, 'Death': 'NA'},
                                  '14': {'ID': '14', 'Spouse': 'NA', 'Death': 'NA'}}}

        expected_output = {'singles': {'11': {'ID': '11', 'Spouse': {'1'}, 'Death': 'NA'},
                                       '14': {'ID': '14', 'Spouse': 'NA', 'Death': 'NA'}},
                           'married': {'12': {'ID': '12', 'Spouse': {'2'}, 'Death': 'NA'},
                                       '13': {'ID': '13', 'Spouse': {'2'}, 'Death': 'NA'}}}

        self.assertEqual(LivingMaritalStatus.list_living_married(parsedFile), expected_output,
                         msg='Function did not sort singles and married properly')

    def test_living_marital_status_div_no_death(self):
        print('US30/US31: Testing listing living individuals marital status')
        parsedFile = {'family': {'1': {'Spouse 1': '10', 'Spouse 2': '11', 'Divorced': 'NA'},
                                 '2': {'Spouse 1': '12', 'Spouse 2': '13', 'Divorced': '1 APR 2019'}},
                      'members': {'10': {'ID': '10', 'Spouse': {'1'}, 'Death': 'NA'},
                                  '11': {'ID': '11', 'Spouse': {'1'}, 'Death': 'NA'},
                                  '12': {'ID': '12', 'Spouse': {'2'}, 'Death': 'NA'},
                                  '13': {'ID': '13', 'Spouse': {'2'}, 'Death': 'NA'},
                                  '14': {'ID': '14', 'Spouse': 'NA', 'Death': 'NA'}}}

        expected_output = {'singles': {'12': {'ID': '12', 'Spouse': {'2'}, 'Death': 'NA'},
                                       '13': {'ID': '13', 'Spouse': {'2'}, 'Death': 'NA'},
                                       '14': {'ID': '14', 'Spouse': 'NA', 'Death': 'NA'}},
                           'married': {'10': {'ID': '10', 'Spouse': {'1'}, 'Death': 'NA'},
                                       '11': {'ID': '11', 'Spouse': {'1'}, 'Death': 'NA'}}}

        self.assertEqual(LivingMaritalStatus.list_living_married(parsedFile), expected_output,
                         msg='Function did not sort singles and married properly')

    def test_living_marital_status_div_death(self):
        print('US30/US31: Testing listing living individuals marital status')
        parsedFile = {'family': {'1': {'Spouse 1': '10', 'Spouse 2': '11', 'Divorced': 'NA'},
                                 '2': {'Spouse 1': '12', 'Spouse 2': '13', 'Divorced': '1 APR 2019'}},
                      'members': {'10': {'ID': '10', 'Spouse': {'1'}, 'Death': '1 APR 2019'},
                                  '11': {'ID': '11', 'Spouse': {'1'}, 'Death': 'NA'},
                                  '12': {'ID': '12', 'Spouse': {'2'}, 'Death': 'NA'},
                                  '13': {'ID': '13', 'Spouse': {'2'}, 'Death': 'NA'},
                                  '14': {'ID': '14', 'Spouse': 'NA', 'Death': 'NA'}}}

        expected_output = {'singles': {'11': {'ID': '11', 'Spouse': {'1'}, 'Death': 'NA'},
                                       '14': {'ID': '14', 'Spouse': 'NA', 'Death': 'NA'},
                                       '12': {'ID': '12', 'Spouse': {'2'}, 'Death': 'NA'},
                                       '13': {'ID': '13', 'Spouse': {'2'}, 'Death': 'NA'}},
                           'married': {}}

        self.assertEqual(LivingMaritalStatus.list_living_married(parsedFile), expected_output,
                         msg='Function did not sort singles and married properly')


if __name__ == '__main__':
    unittest.main()
