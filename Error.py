# Error.py
# Error class

from enum import Enum

class ErrorEnum(Enum):
	UNKNOWN = 'An unknown error has occured'
	US01 = 'ERROR US01: Invalid date: {0} must occur before today: {1}'
	US02 = 'ERROR US02: Invalid marriage date: {0} must occur after bitthdate: {1}'
	US03 = 'ERROR US03: Invalid date death date: {0} must occur after birthdate: {1}'
	US04 = 'ERROR US04: Invalid date divorce date: {0} must occur after marriage date: {1}'
	US05 = 'ERROR US05: Invalid marriage date for {0}. Must be before death of spouse'
	US06 = 'ERROR US06: Invalid divorce date for {0}. Must be before death of spouse'
	US07 = 'ERROR US07: Invalid age: {0} years old of {1}. Must less than 150 years'
	US08 = 'ERROR US08: Invalid birth date for {0}. Children should be born after marriage of parents (and not more than 9 months after their divorce)'
	US09 = 'ERROR US09: Invalid birth date for {0}. Parent death should occur after birth'
	US10 = 'ERROR US10: {0} was not yet 14 for marriage in family {1}.'
	US11 = 'ERROR US11: Bigamy is present in this family'
	US12 = 'ERROR US12: Invalid date of birth for child {0}. Parent {1} is too old.'
	US13 = 'ERROR US13: Siblings born on {0} and {1} have birthdays that are too close together.'
	US14 = 'ERROR US14: Multiple births must be <= 5 for Family {0}.'
	US15 = 'ERROR US15: Family {0} should have less than 15 siblings but they have {1}.'
	US16 = 'ERROR US16: All male members of a family should have the same last name.'
	US17 = 'ERROR US17: Parents should not marry any of their children'
	US18 = 'ERROR US18: Parents of family {0} should not be siblings in family {1}.'
	US19 = 'ERROR US19: Invalid Marriage Type. {0}'
	US20 = 'ERROR US20: Invalid Marriage Type. {0}'
	US22 = 'ERROR US22: Individual with ID {0} already exists'
	US23 = 'ERROR US23: '
	US24 = 'ERROR US24: '
	US25 = 'ERROR US25: There can be no more than one child with the name {0} in family {1}'
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
