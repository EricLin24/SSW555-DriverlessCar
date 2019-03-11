# Error.py
# Error class

from enum import Enum

class ErrorEnum(Enum):
	UNKNOWN = 'An unknown error has occured'
	US01 = 'ERROR US01: Invalid date: {0} must occur before today: {1}'
	US02 = 'ERROR US02: Invalid marraige date: {0} must occur after bitthdate: {1}'
	US03 = 'ERROR US03: Invalid date death date: {0} must occur after birthdate: {1}'
	US04 = 'ERROR US04: Invalid date divorce date: {0} must occur after marraige date: {1}'
	US05 = 'ERROR US05: Invalid marraige date for {0}. Must be before death of spouse'
	US06 = 'ERROR US06: Invalid divorce date for {0}. Must be before death of spouse'
	US07 = 'ERROR US07: '
	US08 = 'ERROR US08: '
	US09 = 'ERROR US09: '
	US10 = 'ERROR US10: {0} was not yet 14 for marraige in family {1}.'
	US11 = 'ERROR US11: Bigamy is present in this family'
	US12 = 'ERROR US12: '
	US13 = 'ERROR US13: '
	US14 = 'ERROR US14: Multiple births mmust be <= 5 for Family {0}.'
	US15 = 'ERROR US15: '
	US16 = 'ERROR US16: '
	US17 = 'ERROR US17: '
	US18 = 'ERROR US18: '
	US19 = 'ERROR US19: '
	US20 = 'ERROR US20: '
	US22 = 'ERROR US22: '
	US23 = 'ERROR US23: '
	US24 = 'ERROR US24: '
	US25 = 'ERROR US25: '
	US27 = 'ERROR US27: '
	US28 = 'ERROR US28: '
	US29 = 'ERROR US29: '
	US30 = 'ERROR US30: '
	US31 = 'ERROR US31: '
	US32 = 'ERROR US32: '
	US41 = 'ERROR US41: '
	US42 = 'ERROR US42: Invalid date: {0}' 

class Error:

	def __init__(self, eCode=ErrorEnum.UNKNOWN):
		self.errCode = ErrorEnum(eCode)
		self.errMsg = ErrorEnum(eCode).value

	def getErrMsg(self):
		return self.errMsg

	def alterErrMsg(self, value0, value1 = ''):
		'''
			Replace the placeholders in the default error string with specific values
		'''

		defaultMsg  = self.errMsg

		if value1 == '':
			self.errMsg = defaultMsg.format(str(value0))
		else:
			self.errMsg = defaultMsg.format(str(value0), str(value1))
