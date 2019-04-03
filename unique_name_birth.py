import Error

def unique_name_and_birth(parsed_file, errors):
    """
    US23: No more than one individual with the same name and birth date should appear in a GEDCOM file
    """
    name_dict = {}
    birth_dict = {}
    for k in parsed_file['members'].keys():
        member = parsed_file['members'][k]
        name, birth = member['Name'], member['Birthday']
        if (name not in name_dict) and (birth not in birth_dict):
            name_dict[name] = k
            birth_dict[birth] = k

        else:
            pre_id = name_dict[name] if name in name_dict else birth_dict[birth]
            us23Err = Error.Error(Error.ErrorEnum.US23)
            us23Err.alterErrMsg(pre_id, k)
            errors.add(us23Err)

    return errors
