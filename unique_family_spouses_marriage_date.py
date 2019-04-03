import Error
import operator

def unique_family_spouse_marriage_date(parsed_file, errors):
    """
    US24:No more than one family with the same spouses by name and the same marriage date should appear in a GEDCOM file
    """
    family_info = {} # fid:{spouse:[], marriage_date: str}
    for k in parsed_file['family'].keys():
        family = parsed_file['family'][k]
        spouse1, spouse2 = family['Spouse 1 Name'], family['Spouse 2 Name']
        marriage_date = family['Married']

        for key, value in family_info.items():
            if operator.eq(sorted([spouse1, spouse2]), sorted(value['spouses'])):
                us24Err = Error.Error(Error.ErrorEnum.US24)
                us24Err.alterErrMsg(key, k)
                errors.add(us24Err)
                continue

            if marriage_date == value['marriage_date']:
                us24Err = Error.Error(Error.ErrorEnum.US24)
                us24Err.alterErrMsg(key, k)
                errors.add(us24Err)

        else:
            family_info[k] = {
                'spouses': [spouse1, spouse2],
                'marriage_date': marriage_date
            }

    return errors
