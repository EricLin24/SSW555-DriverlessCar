######################################
#### US 16
#### All male members of a family should 
#### have the same last name
######################################
import Error

def check_all_male_last_names(parsed_file, errors):

    if not parsed_file or type(parsed_file) != dict:
        return errors
        
    for family_id, family_details in parsed_file['family'].items():
        #print(family_details)
        children_ids = family_details['Children']
        #print(children_ids)
        male_children = [child_id for child_id in children_ids if parsed_file['members'][child_id]['Gender'] == 'M']
        names = [parsed_file['members'][male_id]['Name'] for male_id in male_children ]
        #print(names)
        if len(names) <= 1:
            continue
        else:
            #diff_name = False
            last_0 = names[0].split(' ')[1].strip('/') if len(names[0].split(' ')) == 2 else 'No Last Name'
    
            for name in names[1:]:
                last_other = name.split(' ')[1].strip('/') if len(name.split(' ')) == 2 else 'No Last Name'
                if last_0 != last_other:
                    err_us16 = Error.Error(Error.ErrorEnum.US16)
                    different_last_name_children = ','.join(names)
                    err_us16.alterErrMsg(family_id, different_last_name_children)
                    errors.add(err_us16)
                    break
                    #diff_name = True
            #if diff_name:
            #    return False
            #else:
            #    return True