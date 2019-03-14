from MarriageValidation import create_date

'''
US 13:

Birth dates of siblings should be more than 8 months apart or less than 2 days apart 
(twins may be born one day apart, e.g. 11:59 PM and 12:02 AM the following calendar day)
'''

def valid_sibling_spacing(birthdate_1, birthdate_2):
    b1 = create_date(birthdate_1.split(' ', 2)[2], birthdate_1.split(' ', 2)[1], birthdate_1.split(' ', 2)[0])
    b2 = create_date(birthdate_2.split(' ', 2)[2], birthdate_2.split(' ', 2)[1], birthdate_2.split(' ', 2)[0])

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
