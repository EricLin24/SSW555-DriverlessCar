# DeseasedIndividuals.py

def list_deseased_individuals(parsed_file_dict):
    '''
        US29: List all deseased individuals
        :param parsed_file_dict - GEDCOM file parsed into a dictionary of members and families
        :returns - parsed_file_dict with 'deseased' dictionary
    '''

    # Check for an empty dictionary
    if not parsed_file_dict:
        return

    deseased = {}

    # Find all individuals that are deseased and add their ID, Name, birthday,
    # and death date to the deseased dictionary
    for key in parsed_file_dict['members'].keys():
        
        if parsed_file_dict['members'][key]['Alive?'] == 'Y':
            continue
        else:
            ID = parsed_file_dict['members'][key]['ID']
            deseased[ID] = {'Name':parsed_file_dict['members'][key]['Name'],
                        'Birthday':parsed_file_dict['members'][key]['Birthday'],
                        'Death':parsed_file_dict['members'][key]['Death'],
                        'Age':parsed_file_dict['members'][key]['Age']}

    parsed_file_dict['deseased'] = deseased

    return parsed_file_dict
