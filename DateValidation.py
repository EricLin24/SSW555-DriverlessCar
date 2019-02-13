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

def validate_birth_before_death(birth_date, death_date):
    """
    US03: birth should occur before death of an individual
    :param birth_date: date
    :param death_date: date
    :return: Bool
    """

    err_str = 'Invalid date birth date: ' + str(birth_date) + ' must occur after death date: ' + str(death_date)
    is_valid = False

    if birth_date.year > death_date.year:
        raise Exception(err_str)
    elif birth_date.year == death_date.year and birth_date.month > death_date.year:
        raise Exception(err_str)
    elif birth_date.year == death_date.year and birth_date.month == death_date.month and birth_date.day > death_date.day:
        raise Exception(err_str)
    else:
        is_valid = True

    return is_valid

def validate_marraige_before_divorce(marraige_date, divorce_date):
    """
    US04: marraige date should occur before divorce date
    :param marraige_date: date
    :param divorce_date: date
    :return: bool
    """
    err_str = 'Invalid date birth date: ' + str(marraige_date) + ' must occur after death date: ' + str(divorce_date)
    is_valid = False
    
    if marraige_date.year > divorce_date.year:
        raise Exception(err_str)
    elif marraige_date.year == divorce_date.year and marraige_date.month > divorce_date.year:
        raise Exception(err_str)
    elif marraige_date.year == divorce_date.year and marraige_date.month == divorce_date.month and marraige_date.day > divorce_date.day:
        raise Exception(err_str)
    else:
        is_valid = True

    return is_valid