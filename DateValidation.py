# DateValidation

from datetime import date
import Error

monthsStr = {'JAN': 1, 'FEB': 2, 'MAR': 3, 'APR': 4, 'MAY': 5, 'JUN': 6,
             'JUL': 7, 'AUG': 8, 'SEP': 9, 'OCT': 10, 'NOV': 11, 'DEC': 12}

def validateDate(date):
    '''
        US01: Dates (birth, marriage, divorce, death) 
            should not be after the current date
        :param date: date
    '''
    today = date.today()

    if today.year < date.year:
        return False
    elif today.year == date.year and today.month < date.month:
        return False
    elif today.year == date.year and today.month == date.month and today.day < date.day:
        return False
    else:
        return True

def validateMarraigeDate(birthDate, marraigeDate):
    '''
        US02: Birth should occur before marriage of an individual
        :param birthDate: date
        :param marraigeDate: date
    '''

    if birthDate.year > marraigeDate.year:
        return False
    elif birthDate.year == marraigeDate.year and birthDate.month > marraigeDate.month:
        return False
    elif birthDate.year == marraigeDate.year and birthDate.month == marraigeDate.month and birthDate.day > marraigeDate.day:
        return False
    else:
        return True

def validate_birth_before_death(birth_date, death_date):
    """
    US03: birth should occur before death of an individual
    :param birth_date: date
    :param death_date: date
    """

    if birth_date.year > death_date.year:
        return False
    elif birth_date.year == death_date.year and birth_date.month > death_date.year:
        return False
    elif birth_date.year == death_date.year and birth_date.month == death_date.month and birth_date.day > death_date.day:
        return False
    else:
        return True

def validate_marraige_before_divorce(marraige_date, divorce_date):
    """
    US04: marraige date should occur before divorce date
    :param marraige_date: date
    :param divorce_date: date
    """

    if marraige_date.year > divorce_date.year:
        return False
    elif marraige_date.year == divorce_date.year and marraige_date.month > divorce_date.month:
        return False
    elif marraige_date.year == divorce_date.year and marraige_date.month == divorce_date.month and marraige_date.day > divorce_date.day:
        return False
    else:
        return True

def createValidDate(dateStr):
    '''
        US042: Reject illegitimate dates
        :param dateStr: string date in dd mm yyyy format
    '''

    # Split dateStr into day, month, year componnets
    testDate = dateStr.split(' ', 2)

    try:
        aDate = date(int(testDate[2]), monthsStr[testDate[1]], int(testDate[0]))
        return aDate
    except ValueError as err:
        raise ValueError(str(err))
