######################################
#### US 17
#### Parents should not marry any of 
#### their children
######################################
import Error

def no_marriage_to_children(parsed_file, errors):
    if not parsed_file or type(parsed_file) != dict:
        return errors
    for family_id, family_details in parsed_file['family'].items():
        if family_details['Children'] != 'NA':
            children_ids = family_details['Children']
        else:
            continue
        if len(children_ids) <= 1:
            continue
        #children_names = [parsed_file['members']['Name'] for child_id in children_ids]
        for child_id in children_ids:
            spouse_id = parsed_file['members'][child_id]['Spouse']
            spouse_id = list(spouse_id)[0] if isinstance(spouse_id, set) else spouse_id
            #print(spouse_id)
            if spouse_id != 'NA' and spouse_id in children_ids:
                err_us17 = Error.Error(Error.ErrorEnum.US17)
                married_children = ','.join([parsed_file['members'][child_id]['Name'], parsed_file['members'][spouse_id]['Name']])
                err_us17.alterErrMsg(family_id, married_children)
                errors.add(err_us17)

    return errors
