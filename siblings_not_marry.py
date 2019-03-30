import Error

def siblings_not_marry(parsed_file, errors):
    """
    Siblings should not marry one another
    """
    for i in parsed_file['family'].keys():
        spouse1 = parsed_file['family'][i]['Spouse 1']
        spouse2 = parsed_file['family'][i]['Spouse 2']
        for f in parsed_file['family'].keys():
            children = parsed_file['family'][f]['Children']
            if spouse1 in children and spouse2 in children: #if spouse1 and spouse2 belong to same children of a family, they should be siblings.
                us18Err = Error.Error(Error.ErrorEnum.US18)
                us18Err.alterErrMsg(i, f)
                errors.add(us18Err)
                break

    return errors
