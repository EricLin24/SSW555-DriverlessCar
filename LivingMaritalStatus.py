def list_living_married(parsed_file_dict):
    '''
        US 30 & 31 - List living married, living single
        :returns dict with individual data grouped into sub-dicts 'married' and 'single'
        :param parsed_file_dict parsed GEDCOM file
    '''

    has_spouse = {}
    living_single = {}

    for v in parsed_file_dict['members'].values():
        if v['Spouse'] != 'NA' and v['Death'] == 'NA':
            has_spouse[v['ID']] = v
        elif v['Spouse'] == 'NA' and v['Death'] == 'NA':
            living_single[v['ID']] = v

    still_married = []
    for v in has_spouse.values():
        currIndi = v['ID']
        families = []
        for f in v['Spouse']:
            families.append(f)

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

    return {'singles': living_single, 'married': updated_has_spouse}
