#######################################################
#### US 19 & 20
#### First cousins should not marry one another
#### Aunts and uncles should not marry their nieces or nephews
########################################################

import Error

def check_whether_first_cousins_married(parsed_file,errors):
    for family_id, family_details in parsed_file['family'].items():
        children = family_details['Children']
        child_id_to_spouse_family_ids = {}
        if children != 'NA':
            for child_id in children:
                if parsed_file['members'][child_id]['Spouse'] != 'NA':
                    #print(parsed_file['members'][child_id]['Spouse'])
                    child_id_to_spouse_family_ids[child_id] = parsed_file['members'][child_id]['Spouse']
            #print(child_id_to_family_ids)
            if child_id_to_spouse_family_ids:
                #print(child_id_to_family_ids)
                for child_id, family_ids in child_id_to_spouse_family_ids.items():
                    other_child_to_family_ids = dict([(child_id2, family_ids2) for child_id2, family_ids2 in child_id_to_spouse_family_ids.items() if child_id2 != child_id])
                    #print(other_child_to_family_ids)
                    if other_child_to_family_ids:
                        for family_id in family_ids:
                            #print(parsed_file['family'][family_id])
                            second_gen_children = parsed_file['family'][family_id]['Children']
                            #print(second_gen_children)
                            if second_gen_children != 'NA':
                                for second_gen_child in second_gen_children:
                                    second_gen_child_spouse_family_ids = parsed_file['members'][second_gen_child]['Spouse']
                                    #print(second_gen_child_spouse_family_ids)
                                    if second_gen_child_spouse_family_ids != 'NA':
                                        #print(second_gen_child_spouse_family_ids)
                                        for second_gen_child_spouse_family_id in second_gen_child_spouse_family_ids:
                                            for other_child_id, other_family_ids in other_child_to_family_ids.items():
                                                for other_family_id in other_family_ids:
                                                    other_second_gen_children = parsed_file['family'][other_family_id]['Children']
                                                    if other_second_gen_children != 'NA':
                                                        for other_second_gen_child_id in other_second_gen_children:
                                                            other_second_gen_child_spouse_family_ids = parsed_file['members'][other_second_gen_child_id]['Spouse']
                                                            if second_gen_child_spouse_family_id in other_second_gen_child_spouse_family_ids:
                                                                fam_id = parsed_file['members'][child_id]['Child']
                                                                ch1 = parsed_file['family'][second_gen_child_spouse_family_id]['Spouse 1']
                                                                ch2 = parsed_file['family'][second_gen_child_spouse_family_id]['Spouse 2']
                                                                msg1 = 'Children: %s,%s of family %s married off their children %s,%s'%(child_id,other_child_id, fam_id, ch1, ch2)
                                                                us19Err = Error.Error(Error.ErrorEnum.US19)
                                                                us19Err.alterErrMsg(msg1)
                                                                errors.add(us19Err)
                                                                
                                                                type1 = 'Uncle-'+child_id if parsed_file['members'][child_id]['Gender'] == 'M' else 'Aunt-'+child_id
                                                                type2 = 'Uncle-'+other_child_id if parsed_file['members'][other_child_id]['Gender'] == 'M' else 'Aunt-'+other_child_id
                                                                
                                                                child_type1 = 'Nephew-'+ch1+'('+parsed_file['members'][ch1]['Name']+')' if parsed_file['members'][ch1]['Gender'] == 'M' else 'Niece-'+ch1+'('+parsed_file['members'][ch1]['Name']+')'
                                                                child_type2 = 'Nephew-'+ch2+'('+parsed_file['members'][ch2]['Name']+')' if parsed_file['members'][ch2]['Gender'] == 'M' else 'Niece-'+ch2+'('+parsed_file['members'][ch2]['Name']+')'
                                                                
                                                                msg2 = '%s and %s of family %s married off their children %s, %s'%(type1,type2, fam_id, child_type1, child_type2)
                                                                us20Err = Error.Error(Error.ErrorEnum.US20)
                                                                us20Err.alterErrMsg(msg2)
                                                                errors.add(us20Err)
                                                                
