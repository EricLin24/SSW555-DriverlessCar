# DateValidation

from datetime import date

months = {1:'JAN', 2:'FEB', 3:'MAR', 4:'APR', 5:'MAY', 6:'JUN',
          7:'JUL', 8:'AUG', 9:'SEP', 10:'OCT', 11:'NOV', 12:'DEC'}

def validateDate(date):
	'''
		US01: Dates (birth, marriage, divorce, death) 
			should not be after the current date
        :param date: date
	'''

	today = date.today()
	month = months[today.month]
	errorStr = ''
	isValid = False

	if today.year < date.year:
		errStr = 'Invalid date: year must be <= ' + str(today.year)
		print(errStr)
	elif today.year == date.year and today.month < date.month:
		errStr = 'Invalid date: ' + str(months[date.month]) + ' has not yet occured this year'
		print(errStr)
	elif today.year == date.year and today.month == date.month and today.day < date.day:
		errStr = 'Invalid date: ' + str(month) + ' ' + str(date.day) + ' has not occured yet'
		print(errStr)
	else:
		isValid = True

	return isValid

def validateMarraigeDate(birthDate, marraigeDate):
	'''
		US02: Birth should occur before marriage of an individual
        :param birthDate: date
        :param marraigeDate: date
	'''

	errStr = 'Invalid date marraige date: ' + str(marraigeDate) + ' must occur after birthdate: ' + str(birthDate)
	isValid = False

	if birthDate.year > marraigeDate.year:
		print(errStr)
	elif birthDate.year == marraigeDate.year and birthDate.month > marraigeDate.month:
		print(errStr)
	elif birthDate.year == marraigeDate.year and birthDate.month == marraigeDate.month and birthDate.day > marraigeDate.day:
		print(errStr)
	else:
		isValid = True

	return isValid

def validate_birth_before_death(birth_date, death_date):
    """
    US03: birth should occur before death of an individual
    :param birth_date: date
    :param death_date: date
    """

    err_str = 'Invalid date death date: ' + str(death_date) + ' must occur after birth date: ' + str(birth_date)
    is_valid = False
    if birth_date.year > death_date.year:
        print(err_str)
        return is_valid
    elif birth_date.year == death_date.year and birth_date.month > death_date.year:
        print(err_str)
        return is_valid
    elif birth_date.year == death_date.year and birth_date.month == death_date.month and birth_date.day > death_date.day:
        print(err_str)
        return is_valid
    else:
        is_valid = True
    return is_valid

def validate_marraige_before_divorce(marraige_date, divorce_date):
    """
    US04: marraige date should occur before divorce date
    :param marraige_date: date
    :param divorce_date: date
    """
    err_str = 'Invalid date divorce date: ' + str(divorce_date) + ' must occur after marraige date: ' + str(marraige_date)
    is_valid = False
    if marraige_date.year > divorce_date.year:
        print(err_str)
        return is_valid
    elif marraige_date.year == divorce_date.year and marraige_date.month > divorce_date.month:
        print(err_str)
        return is_valid
    elif marraige_date.year == divorce_date.year and marraige_date.month == divorce_date.month and marraige_date.day > divorce_date.day:
        print(err_str)
        return is_valid
    else:
        is_valid = True
    return is_valid