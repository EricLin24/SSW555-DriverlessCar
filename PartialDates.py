'''
US 41 - Include partial dates
Accept and use dates without days or without days and months
Defining "use" as display in table. Cannot perform date validation with incomplete dates as it might yield
inaccurate results

    :param dateStr: string
'''

monthsStr = {'JAN': 1, 'FEB': 2, 'MAR': 3, 'APR': 4, 'MAY': 5, 'JUN': 6,
             'JUL': 7, 'AUG': 8, 'SEP': 9, 'OCT': 10, 'NOV': 11, 'DEC': 12}


def partial_date_check(dateStr):
    dateCheck = dateStr.split(' ')
    if len(dateCheck) > 3:
        return dateStr
    if len(dateCheck) == 3:
        return dateStr
    else:
        if len(dateCheck) == 2:
            return '?? ' + dateCheck[0] + ' ' + dateCheck[1]
        else:
            return '?? ??? ' + dateCheck[0]

