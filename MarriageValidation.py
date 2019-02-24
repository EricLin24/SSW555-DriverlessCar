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


def bigamy_check(parsed_file_dict):

    def not_bigamous(marriages, divorces=[], deaths=[]):
        for d in divorces:
            if (divorces.index(d) + 1) > (len(marriages) - 1):
                break
            elif d > marriages[divorces.index(d) + 1]:
                return False

        for d in deaths:
            if (deaths.index(d) + 1) > (len(marriages) - 1):
                break
            elif d > marriages[deaths.index(d) + 1]:
                return False

        return True

    for k in parsed_file_dict['members'].keys():
        spouses, marriageDates, divorceDates, deathDates = [], [], [], []
        currentID = parsed_file_dict['members'][k]['ID']
        if parsed_file_dict['members'][k]['Spouse'] == 'NA':
            continue
        else:
            for s in parsed_file_dict['members'][k]['Spouse']:
                spouses.append(s)

            if len(spouses) <= 1:
                continue
            else:

                for s in spouses:
                    if parsed_file_dict['family'][s]['Married'] != 'NA':
                        marriageDates.append(parsed_file_dict['family'][s]['Married'])
                    if parsed_file_dict['family'][s]['Divorced'] != 'NA':
                        divorceDates.append(parsed_file_dict['family'][s]['Divorced'])

                    if parsed_file_dict['family'][s]['Spouse 1'] == currentID:
                        spouseID = parsed_file_dict['family'][s]['Spouse 2']
                    else:
                        spouseID = parsed_file_dict['family'][s]['Spouse 1']

                    if parsed_file_dict['members'][spouseID]['Death'] != 'NA':
                        deathDates.append(parsed_file_dict['members'][spouseID]['Death'])

                for i in marriageDates:
                    origDate = i.split(' ', 2)
                    marriageDates[marriageDates.index(i)] = date(int(origDate[2]), int(months[origDate[1]]), int(origDate[0]))

                marriageDates = sorted(marriageDates)

                for i in divorceDates:
                    origDate = i.split(' ', 2)
                    divorceDates[divorceDates.index(i)] = date(int(origDate[2]), int(months[origDate[1]]),
                                                                 int(origDate[0]))

                divorceDates = sorted(divorceDates)

                for i in deathDates:
                    origDate = i.split(' ', 2)
                    deathDates[deathDates.index(i)] = date(int(origDate[2]), int(months[origDate[1]]),
                                                               int(origDate[0]))

                deathDates = sorted(deathDates)

                if not_bigamous(marriageDates, divorceDates, deathDates) is True:
                    continue
                else:
                    return False

    return True








