def UniqueFamilyIds(familyId: str, family: dict) -> bool:
    for k in family.keys():
        if k == familyId:
            return True

    return False


def UniqueIndividualIds(indivId: str, members: dict) -> bool:
    for k in members.keys():
        if k == indivId:
            return True

    return False
