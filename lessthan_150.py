from datetime import date


months = {'JAN': 1, 'FEB': 2, 'MAR': 3, 'APR': 4, 'MAY': 5, 'JUN': 6,
          'JUL': 7, 'AUG': 8, 'SEP': 9, 'OCT': 10, 'NOV': 11, 'DEC': 12}

def less_than_150(member):
    """
    The age of an individual should less than 150 years
    :param member: dict
    :return: bool
    """
    if type(member) != dict:
        print('Input Error: The parameter is invalid.')
        return -1
    if not member['Birthday'] or not member['Death']:
        print('Input Error: The parameter is invalid.')
        return -1

    birth_date = parse_date(member['Birthday'])

    #last_date could be the death date or today
    last_date = parse_date(member['Death']) if member['Death'] != 'NA' else date.today()

    #inspect if the indi elder than 150 years old
    age = last_date.year - birth_date.year - ((last_date.month, last_date.day) < (birth_date.month, birth_date.day))
    #print(age)
    if age >= 150:
        print(f"Invalid age: Individual's age is {age}, should less than 150.")
        return False
    else:
        return True

def parse_date(string):
    date_list = string.split()
    valid_date = date(int(date_list[2]), months[date_list[1]], int(date_list[0]))
    return valid_date


