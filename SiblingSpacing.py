from datetime import date

'''
US 13:

Birth dates of siblings should be more than 8 months apart or less than 2 days apart 
(twins may be born one day apart, e.g. 11:59 PM and 12:02 AM the following calendar day)
'''
months = {'JAN': 1, 'FEB': 2, 'MAR': 3, 'APR': 4, 'MAY': 5, 'JUN': 6,
          'JUL': 7, 'AUG': 8, 'SEP': 9, 'OCT': 10, 'NOV': 11, 'DEC': 12}


def create_date(year, month, day):
    try:
        if month in months.keys():
            dateYear = int(year)
            dateMonth = int(months[month])
            dateDay = int(day)
        else:
            dateYear = int(year)
            dateMonth = int(month)
            dateDay = int(day)

        return date(dateYear, dateMonth, dateDay)
    except ValueError as v:
        print('All inputs must be whole, positive numbers!', str(v))


def valid_sibling_spacing(birthdate_1, birthdate_2):
    print('new')
    b1 = create_date(birthdate_1.split(' ', 2)[2], birthdate_1.split(' ', 2)[1], birthdate_1.split(' ', 2)[0])
    b2 = create_date(birthdate_2.split(' ', 2)[2], birthdate_2.split(' ', 2)[1], birthdate_2.split(' ', 2)[0])

    print(b1, b2)

    if b1 == b2:
        return True
    elif abs(b1.year - b2.year) > 0:
        return True
    elif b1.month == b2.month and abs(b1.day - b2.day) < 2:
        return True
    elif abs(b1.month - b2.month) > 8:
        return True
    else:
        return False


def sibling_check(parsed_file_dict):
    siblings = [c['Children'] for c in parsed_file_dict['family'].values()
                if len(c['Children']) > 1 and c['Children'] != 'NA']

    for s in siblings:
        sibBirths = []
        for i in s:
            sibBirths.append(create_date(parsed_file_dict['members'][i]['Birthday'].split(' ', 2)[2],
                              parsed_file_dict['members'][i]['Birthday'].split(' ', 2)[1],
                              parsed_file_dict['members'][i]['Birthday'].split(' ', 2)[0]))

        sibBirths = sorted(sibBirths)
        for d in sibBirths:
            if sibBirths.index(d) == len(sibBirths) - 1:
                break

        print('next set')



