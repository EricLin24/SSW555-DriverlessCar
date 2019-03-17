"""US08"""
from datetime import date
import Error
months = {'JAN': 1, 'FEB': 2, 'MAR': 3, 'APR': 4, 'MAY': 5, 'JUN': 6,
          'JUL': 7, 'AUG': 8, 'SEP': 9, 'OCT': 10, 'NOV': 11, 'DEC': 12}

def birth_before_parent_marriage(birth_date, parent_marriage_date, parent_divorce_date, errors):
    """
    Children should be born after marriage of parents (and not more than 9 months after their divorce)
    :param member:dict
    :return: bool
    """
    if not birth_date:
        return errors
    err_str = f"Invalid Date birthday:{str(birth_date)} should occur after parents' marriage:{str(parent_marriage_date)} and and not more than 9 months after their divorce:{str(parent_divorce_date)}"
    birth_date = parse_date(birth_date)
    parent_marriage_date = parse_date(parent_marriage_date)

    if parent_marriage_date.year > birth_date.year:
        us08Err = Error.Error(Error.ErrorEnum.US08)
        us08Err.alterErrMsg(str(birth_date))
        errors.add(us08Err)

    elif parent_marriage_date.year == birth_date.year and parent_marriage_date.month > birth_date.month:
        us08Err = Error.Error(Error.ErrorEnum.US08)
        us08Err.alterErrMsg(str(birth_date))
        errors.add(us08Err)

    elif parent_marriage_date.year == birth_date.year and parent_marriage_date.month == birth_date.month and parent_marriage_date.day > birth_date.day:
        us08Err = Error.Error(Error.ErrorEnum.US08)
        us08Err.alterErrMsg(str(birth_date))
        errors.add(us08Err)

    elif parent_divorce_date != 'NA':  #divorce
        parent_divorce_date = parse_date(parent_divorce_date)
        month = (birth_date.year - parent_divorce_date.year) * 12 + (birth_date.month - parent_divorce_date.month) + (birth_date.day > parent_divorce_date.day)
        if month > 9: #divorced beyond 9 month
            us08Err = Error.Error(Error.ErrorEnum.US08)
            us08Err.alterErrMsg(str(birth_date))
            errors.add(us08Err)

    return errors


def parse_date(string):
    date_list = string.split()
    if date_list[0] == '??':
        date_list[0] = 1
    valid_date = date(int(date_list[2]), months[date_list[1]], int(date_list[0]))
    return valid_date
