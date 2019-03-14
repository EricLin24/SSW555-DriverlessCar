from datetime import date

months = {'JAN': 1, 'FEB': 2, 'MAR': 3, 'APR': 4, 'MAY': 5, 'JUN': 6,
          'JUL': 7, 'AUG': 8, 'SEP': 9, 'OCT': 10, 'NOV': 11, 'DEC': 12}


def at_least_age(target_age, birthday, targetdate=date.today()):
    if targetdate.year <= birthday.year:
        return False
    if targetdate.year - birthday.year > target_age:
        return True
    elif targetdate.year - birthday.year < target_age:
        return False
    elif targetdate.year - birthday.year == target_age:
        if targetdate.month > birthday.month:
            return True
        elif targetdate.month < birthday.month:
            return False
        else:
            if targetdate.day >= birthday.day:
                return True
            elif targetdate.day < birthday.day:
                return False


'''
US 10 - no marriage after 14:

Marriage should be at least 14 years after birth of both spouses (parents must be at least 14)

'''


def valid_age_at_marriage(birthday, marriagedate):
    return at_least_age(14, birthday, marriagedate)


'''
US 11 - no bigamy: 

No one should have more than one spouse at a time
    - If someone is remarried, the marriage date must be after the previous spouse(s)'s div/death date

'''


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



def not_bigamous(marriages, divorces_deaths=[]):
    marriage_term = divorces_deaths
    if len(marriages) >= 2:
        for m in marriages:
            try:
                if marriage_term[0] > marriages[marriages.index(m) + 1]:
                    return False
            except IndexError as e:
                pass

            if len(marriage_term) == 1:
                break
            else:
                marriage_term = marriage_term[1:len(marriage_term)]

    return True


def bigamy_check(parsed_file_dict):

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
                    if '??' in origDate:
                        return True
                    marriageDates[marriageDates.index(i)] = create_date(origDate[2], origDate[1], origDate[0]);

                marriageDates = sorted(marriageDates)

                for i in divorceDates:
                    origDate = i.split(' ', 2)
                    if '??' in origDate:
                        return True
                    divorceDates[divorceDates.index(i)] = create_date(origDate[2], origDate[1], origDate[0]);

                divorceDates = sorted(divorceDates)

                for i in deathDates:
                    origDate = i.split(' ', 2)
                    if '??' in origDate:
                        return True
                    deathDates[deathDates.index(i)] = create_date(origDate[2], origDate[1], origDate[0]);

                deathDates = sorted(deathDates)

                if not_bigamous(marriageDates, sorted(divorceDates + deathDates)) is True:
                    continue
                else:
                    return False

    return True








