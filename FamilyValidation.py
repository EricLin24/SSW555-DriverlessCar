# FamilyValidation.py 

import Error

def check_multiple_births(parsed_file_dict, errors):
	'''
		US14: Multiple births <= 5: no more than five sibling 
			should be born at the same time
		:param parsed_file_dict GEDCOM file parsed into a dictionary of members and families
		:param errors set of errors
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

def check_same_name(parsed_file_dict, errors):
	'''
		US25: Unique first names in families - no more than one child can have the same first name
		:param parsed_file_dict GEDCOM file parsed into a dictionary of members and families
		:param errors set of errors
	'''

	# Check for an empty dictionary
	if not parsed_file_dict:
		return errors


	# Find the children in each family and compare their names
	for key in parsed_file_dict['family'].keys():
		children = []
		familyID = key
		childCount = 0

		if parsed_file_dict['family'][key]['Children'] == 'NA':
			continue
		else:
			children = parsed_file_dict['family'][key]['Children']
			childCount = len(children)

			# Only check families with > 1 child
			if childCount <= 1:
				continue
			else:
				names = {}
				for child in children:
					name = parsed_file_dict['members'][child]['Name']
					fullName = name.split('/')
					firstName = fullName[0]

					if firstName in names.keys():
						names[firstName] = names[firstName] + 1
					else:
						names[firstName] = 1

					if names[firstName] > 1:
						us25Err = Error.Error(Error.ErrorEnum.US25)
						us25Err.alterErrMsg(firstName, familyID)
						errors.add(us25Err)

	return errors

def sort_siblings(siblings_list):
	'''
		Sorts a list of siblings by age decending
		:param siblings_list - list of siblings
		:returns siblings_list sorted by age (oldest first)
	'''

	# Sort the list in acending order
	for index in range(1, len(siblings_list)):
		current = siblings_list[index]
		position = index

		while position > 0 and siblings_list[position-1]['Age'] < current['Age']:
			siblings_list[position] = siblings_list[position-1]
			position -= 1

		siblings_list[position] = current

	return siblings_list

def order_siblings_by_age(parsed_file_dict):
	'''
		US28: Order siblings by age - List siblings in families by decreasing age, i.e. oldest siblings first
		:param parsed_file_dict - GEDCOM file parsed into a dictionary of members and families
		:return parsed file dict with 'siblings' dictionary
	'''
	# Check for an empty dictionary
	if not parsed_file_dict:
		return

	siblings = {}

	for key in parsed_file_dict['family'].keys():
		children = []
		familyID = key

		# Skip families with no children or one child
		if parsed_file_dict['family'][key]['Children'] == 'NA' or len(parsed_file_dict['family'][key]['Children']) == 1:
			continue
		else:
			children = parsed_file_dict['family'][key]['Children']

		# Add relavent information to the siblings dictionary
		for child in children:
			ID = child
			name = parsed_file_dict['members'][child]['Name']
			birthdate = parsed_file_dict['members'][child]['Birthday']
			if parsed_file_dict['members'][child]['Age'] == 'Unknown':
				age = -1				
			else:
				age = parsed_file_dict['members'][child]['Age']

			if familyID not in siblings.keys():
				siblings[familyID] = [{'ID':ID, 'Name':name, 'Birthday':birthdate, 'Age':age}]
			else:
				siblings[familyID].append({'ID':ID, 'Name':name, 'Birthday':birthdate, 'Age':age})

	# Order the siblings by age
	for familyID in siblings.keys():
		siblings[familyID] = sort_siblings(siblings[familyID])

		# Return any -1 values with 'Unknown'
		for individual in siblings[familyID]:
			if individual['Age'] == -1:
				individual['Age'] = 'Unknown'

	parsed_file_dict['siblings'] = siblings

	return parsed_file_dict

def list_multiple_births(parsed_file_dict):
	'''
		US32: List multiple births - List all multiple births in a GEDCOM file
		:param parsed_file_dict - GEDCOM file parsed into a dictionary of members and families
		:return parsed file dict with 'multiples' dictionary
	'''

	# Check for an empty dictionary
	if not parsed_file_dict:
		return

	multiples = {}

	for key in parsed_file_dict['family'].keys():
		children = []
		familyID = key
		birthCount = 0

		if parsed_file_dict['family'][key]['Children'] == 'NA':
			continue
		else:
			children = parsed_file_dict['family'][key]['Children']
			birthCount = len(children)

			# Only check families with at least 2 children
			if birthCount <= 2:
				continue
			else:
				birthdays = {}
				for child in children:
					birthday = parsed_file_dict['members'][child]['Birthday']

					# Skip any unknown birthdays
					if birthday == 'Unknown':
						continue
					elif birthday in birthdays.keys():
						birthdays[birthday].append(parsed_file_dict['members'][child]['ID']) 
					else:
						birthdays[birthday] = [parsed_file_dict['members'][child]['ID']]

				for births in birthdays.keys():
					if len(birthdays[births]) >= 2:
						for person in birthdays[births]:
							ID = person
							name = parsed_file_dict['members'][ID]['Name']

							if familyID in multiples.keys():
								multiples[familyID].append({'Birthday':births, 'ID':ID, 'Name':name})
							else:
								multiples[familyID] = [{'Birthday':births, 'ID':ID, 'Name':name}]

	parsed_file_dict['multiples'] = multiples

	return parsed_file_dict	 
