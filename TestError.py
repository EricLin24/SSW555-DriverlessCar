# TestError.py 
# Tests Error.py

import Error
import unittest
from datetime import date

class TestError(unittest.TestCase):
	def test_createError(self):
		newErr = Error.Error()

		print('Creating a new error...')
		self.assertEqual(newErr.getErrMsg(), Error.ErrorEnum.UNKNOWN.value, msg='Failed to create error' )

	def test_setError(self):
		print('Creating a US01 error...')

		us01Err = Error.Error(Error.ErrorEnum.US01)
		self.assertEqual(us01Err.getErrMsg(), Error.ErrorEnum.US01.value, msg='Failed to create US01 error' )

	def test_alterErMsg(self):
		print('Testing modifying an error message...')

		us04Err = Error.Error(Error.ErrorEnum.US04)
		value0 = '2003 03 07'
		value1 = '2002 10 11'

		us04Err.alterErrMsg(value0, value1)

		expected = 'ERROR US04: Invalid date divorce date: 2003 03 07 must occur after marraige date: 2002 10 11'

		self.assertEqual(us04Err.getErrMsg(), expected,  msg='Failed to alter US06 message' )


if __name__ == '__main__':
	unittest.main()
