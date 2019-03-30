import Error

def siblings_not_too_many(siblings, errors):
    """
    US15
    There should be fewer than 15 siblings in a family
    """
    for k in siblings.keys():
        num = len(siblings[k])
        if num >= 15: # a family with >= 15 siblings
            us15Err = Error.Error(Error.ErrorEnum.US15)
            us15Err.alterErrMsg(k, num)
            errors.add(us15Err)

    return errors
