from datetime import date


def at_least_14(birthday, targetdate=date.today()):
    if targetdate.year <= birthday.year:
        return 0
    if targetdate.year - birthday.year > 14:
        return 15
    elif targetdate.year - birthday.year < 14:
        return 0
    elif targetdate.year - birthday.year == 14:
        if targetdate.month > birthday.month:
            return 15
        elif targetdate.month < birthday.month:
            return 0
        else:
            if targetdate.day >= birthday.day:
                return 15
            elif targetdate.day < birthday.day:
                return 0


'''
US 10 - no marriage after 14:

Marriage should be at least 14 years after birth of both spouses (parents must be at least 14)

'''


def valid_age_at_marriage(birthday, marriagedate):
    if at_least_14(birthday, marriagedate) >= 14:
        isOldEnough = True
        return isOldEnough
    else:
        isOldEnough = False
        return isOldEnough


'''
US 11 - no bigamy: 

No one should have more than one spouse at a time
    - If someone is remarried, the marriage date must be after the previous spouse(s)'s div/death date
    
'''



