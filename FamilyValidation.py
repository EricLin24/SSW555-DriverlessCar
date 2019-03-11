# FamilyValidation.py 

import Error

def check_multiple_births(parsed_file_dict, errors):
	'''
		US14: Multiple births <= 5: no more than five sibling 
			should be born at the same time
		:param parsed_file_dict GEDCOM file parsed into a dictionary of members and families
	'''

	# Check for an empty dictionary
	if not parsed_file_dict:
		return errors

	for key in parsed_file_dict['family'].keys():
		children = []
		familyID = key
		birthCount = 0

		if parsed_file_dict['family'][key]['Children'] == 'NA':
			continue
		else:
			children = parsed_file_dict['family'][key]['Children']
			birthCount = len(children)

			# Only check families with > 5 children
			if birthCount <= 5:
				continue
			else:
				birthdays = {}
				for child in children:
					birthday = parsed_file_dict['members'][child]['Birthday']
					if birthday in birthdays.keys():
						birthdays[birthday] = birthdays[birthday] + 1
					else:
						birthdays[birthday] = 1

					if birthdays[birthday] > 5:
						us14Err = Error.Error(Error.ErrorEnum.US14)
						us14Err.alterErrMsg(familyID)
						errors.add(us14Err)

	return errors