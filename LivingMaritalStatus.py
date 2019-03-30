from prettytable import PrettyTable


def list_living_married(parsed_file_dict):
    '''
        US 30 & 31 - List living married, living single
        check living, check family, check not divorced, check spouse alive (just because there are spouses, doesn't mean they're married)
        :param parsed_file_dict parsed GEDCOM file
    '''

    has_spouse = {}
    living_single = {}

    for v in parsed_file_dict['members'].values():
        if v['Spouse'] != 'NA' and v['Death'] == 'NA':
            has_spouse[v['ID']] = v
        elif v['Spouse'] == 'NA' and v['Death'] == 'NA':
            living_single[v['ID']] = v

    # print(len(has_spouse))
    # print('\n')
    # print(len(living_single))

    # for each person that has a spouse
    # check if divorced (data from family)
    # else check if spouse died (ID from family, check in members)
    still_married = []
    for v in has_spouse.values():
        currIndi = v['ID']
        # print(currIndi)
        families = []
        for f in v['Spouse']:
            families.append(f)

        # print(families)

        for fam in families:
            if parsed_file_dict['family'][fam]['Divorced'] != 'NA':
                families.pop(families.index(fam))

        if len(families) > 0:
            for fam in families:
                if parsed_file_dict['family'][fam]['Spouse 1'] != currIndi:
                    if parsed_file_dict['members'][parsed_file_dict['family'][fam]['Spouse 1']]['Death'] != 'NA':
                        families.pop(families.index(fam))
                else:
                    if parsed_file_dict['members'][parsed_file_dict['family'][fam]['Spouse 2']]['Death'] != 'NA':
                        families.pop(families.index(fam))

        if len(families) == 0:
            living_single[currIndi] = parsed_file_dict['members'][currIndi]
        else:
            still_married.append(currIndi)

    updated_has_spouse = {}

    for v in has_spouse.values():
        if v['ID'] in still_married:
            updated_has_spouse[v['ID']] = v

    # print('AFTER')
    # print(len(updated_has_spouse))
    # print('\n')
    # print(len(living_single))

    return {'singles': living_single, 'married': updated_has_spouse}





# US 31 - List living single