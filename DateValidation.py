# DateValidation

from datetime import date

months = {1:'JAN', 2:'FEB', 3:'MAR', 4:'APR', 5:'MAY', 6:'JUN',
          7:'JUL', 8:'AUG', 9:'SEP', 10:'OCT', 11:'NOV', 12:'DEC'}

def validateDate(date):
	'''
		US01: Dates (birth, marriage, divorce, death) 
			should not be after the current date
	'''

	today = date.today()
	month = months[today.month]
	errorStr = ''
	isValid = False

	if today.year < date.year:
		errStr = 'Invalid date: year must be <= ' + str(today.year)
		raise Exception(errStr)
	elif today.year == date.year and today.month < date.month:
		errStr = 'Invalid date: ' + str(months[date.month]) + ' has not yet occured this year'
		raise Exception(errStr)
	elif today.year == date.year and today.month == date.month and today.day < date.day:
		errStr = 'Invalid date: ' + str(month) + ' ' + str(date.day) + ' has not occured yet'
		raise Exception(errStr)
	else:
		isValid = True

	return isValid

def validateMarraigeDate(birthDate, marraigeDate):
	'''
		US02: Birth should occur before marriage of an individual
	'''

	errStr = 'Invalid date marraige date: ' + str(marraigeDate) + ' must occur after birthdate: ' + str(birthDate)
	isValid = False

	if birthDate.year > marraigeDate.year:
		raise Exception(errStr)
	elif birthDate.year == marraigeDate.year and birthDate.month > marraigeDate.month:
		raise Exception(errStr)
	elif birthDate.year == marraigeDate.year and birthDate.month == marraigeDate.month and birthDate.day > marraigeDate.day:
		raise Exception(errStr)
	else:
		isValid = True

	return isValid