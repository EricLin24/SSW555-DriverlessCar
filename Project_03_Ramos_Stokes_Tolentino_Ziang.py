# Michael Ramos, Sadie Stokes, Jonathan Tolentino, Lin Ziang
# CS 555
# Project 06
# 03/17/2019

import sys
import os
from datetime import date
from prettytable import PrettyTable
import DateValidation
import MarriageValidation
import MarriageBeforeDeathValidation
import DivorceBeforeDeathValidation
import FamilyValidation
import Error

cwd = os.path.dirname(os.path.realpath(__file__))

errors = set()

class GEDCOM_Line:
    def __init__(self):
        self.Level = 0
        self.Tag = 'default'
        self.Valid = 'N'
        self.Args = ''

    def Parse(self, line):
        '''
            Parse an input line into a GEDCOM_Line object
        '''

        token = line.split()

        self.Level = token[0]
        self.Tag = token[1].upper()

        # Check the value of token[2], certaing tags appear after the args
        if len(token) > 2:
            if token[2].upper() == 'INDI' or token[2].upper() == 'FAM' or token[2].upper() == 'SUBM':
                self.Tag = token[2].upper()
                self.Args = token[1]
            else:
                for i in range(2, len(token)):
                    self.Args += (token[i] + ' ')

    def Validate(self):
        '''
            Compare the Tag to the set of valid tags
        '''
        validTags = {'INDI', 'NAME', 'SEX', 'BIRT', 'DEAT', 'FAMC',
                     'FAMS', 'FAM', 'MARR', 'HUSB', 'WIFE', 'CHIL',
                     'DIV', 'DATE', 'HEAD', 'TRLR', 'NOTE', 'SPOUSE'}

        if self.Tag in validTags:
            # 2 DATE is supported 1 DATE is not
            # 1 NAME is supported 2 NAME is not
            if self.Tag == 'DATE' and self.Level == 1:
                self.Valid = 'N'
            elif self.Tag == 'NAME' and self.Level == 2:
                self.Valid = 'N'
            else:
                self.Valid = 'Y'
        else:
            self.Valid = 'N'

months = {'JAN': 1, 'FEB': 2, 'MAR': 3, 'APR': 4, 'MAY': 5, 'JUN': 6,
          'JUL': 7, 'AUG': 8, 'SEP': 9, 'OCT': 10, 'NOV': 11, 'DEC': 12}


# Functions for difference in years

def date_difference(pastdate, futuredate=date.today()):
    return futuredate.year - pastdate.year - ((futuredate.month, futuredate.day) < (pastdate.month, pastdate.day))


def parse_file(filename):
    try:
        with open(filename) as gedFile:

            # Initialize dicts for working with an individual, tracking members of the family, and grouping families
            family = {}
            individual = {}
            members = {}

            # Tracking where we are in the hierarchy
            currentFam, currentTag = '', ''

            line = gedFile.readline()

            # Parse the file
            while line:
                gedLine = GEDCOM_Line()
                gedLine.Parse(line)
                gedLine.Validate()
                line = line.rstrip()
                line = line.split(' ', 2)

                if line[0] == '0' and len(line) == 3:  # If line is an INDI or FAM line
                    if individual:  # If an individual has been completed
                        members[individual['ID']] = individual  # Add them to the members dict
                        individual = {} # Empty the dict to start over
                    if gedLine.Valid == 'Y':
                        if line[2] == 'INDI':
                            if line[1] not in members.keys():  # Ensure we're not duplicating people
                                individual['ID'] = line[1]
                                individual['Child'] = set()
                                individual['Spouse'] = set()
                                currentTag = line[2]
                                line = gedFile.readline()  # Move to the next line
                                continue
                        if line[2] == 'FAM':
                            if line[1] not in family.keys():
                                family[line[1]] = {'Children': set()}  # Add a new family
                                currentTag = line[2]
                                currentFam = line[1]
                                line = gedFile.readline()
                                continue
                elif len(line) == 2:
                    if gedLine.Valid == 'Y':
                        currentTag = line[1]
                        line = gedFile.readline()
                        continue
                elif 'DEAT' in line:
                    if gedLine.Valid == 'Y':
                        currentTag = 'DEAT'
                        line = gedFile.readline()
                        continue
                elif line[1] == 'HUSB' or line[1] == 'WIFE' or line[1] == 'CHIL':
                    if gedLine.Valid == 'Y':
                        currentTag = line[1]

                # Logic for adding information to individuals based on where we are in the hierarchy
                if currentTag == 'INDI':
                    if line[0] != 0 and len(line) == 3:
                        if gedLine.Valid == 'Y':
                            if line[1] == 'NAME':
                                individual['Name'] = line[2]
                            elif line[1] == 'SEX':
                                individual['Gender'] = line[2]
                            elif line[1] == 'FAMC':
                                individual['Child'].add(line[2])
                            elif line[1] == 'FAMS':
                                individual['Spouse'].add(line[2])
                    line = gedFile.readline()
                    continue

                if currentTag == 'BIRT':
                    if line[0] != 0 and len(line) == 3:
                        if gedLine.Valid == 'Y':
                            if line[1] == 'DATE':
                                try:
                                    testDate = DateValidation.createValidDate(line[2])

                                    if DateValidation.validateDate(testDate):
                                        individual['Birthday'] = line[2]
                                        currentTag = 'INDI'
                                    else:
                                        today = date.today()
                                        us01Err = Error.Error(Error.ErrorEnum.US01)
                                        us01Err.alterErrMsg(testDate, today)
                                        errors.add(us01Err)
                                        individual['Birthday'] = line[2]
                                        currentTag = 'INDI'
                                except ValueError as err:
                                    print(str(err))
                                finally:
                                    currentTag = 'INDI'

                if currentTag == 'DEAT':
                    if line[0] != 0 and len(line) == 3:
                        if gedLine.Valid == 'Y':
                            if line[1] == 'DATE':
                                try:
                                    testDate = DateValidation.createValidDate(line[2])
                                    if DateValidation.validateDate(testDate):
                                        individual['Death'] = line[2]
                                    else:
                                        today = date.today()
                                        us01Err = Error.Error(Error.ErrorEnum.US01)
                                        us01Err.alterErrMsg(testDate, today)
                                        errors.add(us01Err)
                                        individual['Death'] = line[2]
                                except ValueError as err:
                                    print(str(err))
                                finally:
                                    currentTag = 'INDI'

                if currentTag == 'MARR':
                    if line[0] != 0 and len(line) == 3:
                        if gedLine.Valid == 'Y':
                            if line[1] == 'DATE':
                                try:
                                    testDate = DateValidation.createValidDate(line[2])
                                    if DateValidation.validateDate(testDate):
                                        family[currentFam]['Married'] = line[2]
                                    else:
                                        today = date.today()
                                        us01Err = Error.Error(Error.ErrorEnum.US01)
                                        us01Err.alterErrMsg(testDate, today)
                                        errors.add(us01Err)
                                except ValueError as err:
                                    print(str(err))

                if currentTag == 'DIV':
                    if line[0] != 0 and len(line) == 3:
                        if gedLine.Valid == 'Y':
                            if line[1] == 'DATE':
                                try:
                                    testDate = DateValidation.createValidDate(line[2])
                                    if DateValidation.validateDate(testDate):
                                        family[currentFam]['Divorced'] = line[2]
                                    else:
                                        today = date.today()
                                        us01Err = Error.Error(Error.ErrorEnum.US01)
                                        us01Err.alterErrMsg(testDate, today)
                                        errors.add(us01Err)

                                except ValueError as err:
                                    print(str(err))
                                    
                if currentTag == 'HUSB':
                    if line[0] != 0 and len(line) == 3:
                        if gedLine.Valid == 'Y':
                            if 'Spouse 1' in family[currentFam].keys():
                                family[currentFam]['Spouse 2'] = line[2]
                            else:
                                family[currentFam]['Spouse 1'] = line[2]

                if currentTag == 'WIFE':
                    if line[0] != 0 and len(line) == 3:
                        if gedLine.Valid == 'Y':
                            if 'Spouse 1' in family[currentFam].keys():
                                family[currentFam]['Spouse 2'] = line[2]
                            else:
                                family[currentFam]['Spouse 1'] = line[2]

                if currentTag == 'CHIL':
                    if line[0] != 0 and len(line) == 3:
                        if gedLine.Valid == 'Y':
                            family[currentFam]['Children'].add(line[2])

                if currentTag != 'INDI':
                    currentTag = ''

                line = gedFile.readline()

    except IOError as e:
        print('Error opening ' + sys.argv[1] + ': ' + str(e))

    finally:
        for k in family.keys():  # Add name of Spouse based on ID
            family[k]['Spouse 1 Name'] = members[family[k]['Spouse 1']]['Name']
            family[k]['Spouse 2 Name'] = members[family[k]['Spouse 2']]['Name']

            if 'Divorced' not in family[k].keys():  # 'NA' if not divorced
                family[k]['Divorced'] = 'NA'

            if len(family[k]['Children']) == 0:  # 'NA' if no children
                family[k]['Children'] = 'NA'

        for k, v in members.items():  # For each member, check if died
            if 'Death' in members[k].keys():  # If died, set 'N' for Alive and calculate age at death
                members[k]['Alive?'] = 'N'
                try:
                    birthday = DateValidation.createValidDate(members[k]['Birthday'])
                    death_day = DateValidation.createValidDate(members[k]['Death'])
                    if not DateValidation.validate_birth_before_death(birthday, death_day):
                        us03Err = Error.Error(Error.ErrorEnum.US03)
                        us03Err.alterErrMsg(death_day, birthday)
                        errors.add(us03Err)
                        members[k]['Age'] = date_difference(birthday, death_day)
                    else:
                        members[k]['Age'] = date_difference(birthday, death_day)
                except ValueError as err:
                    print(str(err))
            else:
                members[k]['Death'] = 'NA'
                members[k]['Alive?'] = 'Y'
                try:
                    birthday = DateValidation.createValidDate(members[k]['Birthday'])
                    members[k]['Age'] = date_difference(birthday)
                except ValueError as err:
                    print(str(err))

            if len(members[k]['Child']) == 0:  # if no children, 'NA'
                members[k]['Child'] = 'NA'

            if len(members[k]['Spouse']) == 0:  # if no spouse, 'NA'
                members[k]['Spouse'] = 'NA'

        gedFile.close()

        for f in family.keys():
            marriage_date_text = family[f]['Married'].split(' ', 2)
            marriage_date = date(int(marriage_date_text[2]), months[marriage_date_text[1]], int(marriage_date_text[0]))
            spouses = [family[f]['Spouse 1'], family[f]['Spouse 2']]
            divorce_date_text = ''

            if members[family[f]['Spouse 1']]['Death'] != 'NA':
                died_on = members[family[f]['Spouse 1']]['Death'].split(' ', 2)
                died_on_date = date(int(died_on[2]), int(months[died_on[1]]), int(died_on[0]))
                if not MarriageBeforeDeathValidation.marr_before_death(marriage_date, died_on_date):
                    us05Err = Error.Error(Error.ErrorEnum.US05)
                    us05Err.alterErrMsg(f)
                    errors.add(us05Err)

            if members[family[f]['Spouse 2']]['Death'] != 'NA':
                died_on = members[family[f]['Spouse 2']]['Death'].split(' ', 2)
                died_on_date = date(int(died_on[2]), int(months[died_on[1]]), int(died_on[0]))
                if not MarriageBeforeDeathValidation.marr_before_death(marriage_date, died_on_date):
                    us05Err = Error.Error(Error.ErrorEnum.US05)
                    us05Err.alterErrMsg(f)
                    errors.add(us05Err)

            if family[f]['Divorced'] != 'NA':
                divorce_date_text = family[f]['Divorced'].split(' ', 2)
                divorce_date = date(int(divorce_date_text[2]), months[divorce_date_text[1]],
                                     int(divorce_date_text[0]))

                if members[family[f]['Spouse 1']]['Death'] != 'NA':
                    died_on = members[family[f]['Spouse 1']]['Death'].split(' ', 2)
                    died_on_date = date(int(died_on[2]), int(months[died_on[1]]), int(died_on[0]))
                    if not DivorceBeforeDeathValidation.div_before_death(divorce_date, died_on_date):
                        us06Err = Error.Error(Error.ErrorEnum.US06)
                        us06Err.alterErrMsg(f)
                        errors.add(us06Err)

                if members[family[f]['Spouse 2']]['Death'] != 'NA':
                    died_on = members[family[f]['Spouse 2']]['Death'].split(' ', 2)
                    died_on_date = date(int(died_on[2]), int(months[died_on[1]]), int(died_on[0]))
                    if not DivorceBeforeDeathValidation.div_before_death(divorce_date, died_on_date):
                        us06Err = Error.Error(Error.ErrorEnum.US06)
                        us06Err.alterErrMsg(f)
                        errors.add(us06Err)

            for s in spouses:
                text_birthday = members[s]['Birthday'].split(' ', 2)
                birthdate = date(int(text_birthday[2]), months[text_birthday[1]], int(text_birthday[0]))
                if DateValidation.validateMarraigeDate(birthdate, marriage_date) is False:
                    us02Err = Error.Error(Error.ErrorEnum.US02)
                    us02Err.alterErrMsg(marriage_date, birthdate)
                    errors.add(us02Err)

                if divorce_date_text != '':
                    if DateValidation.validate_marraige_before_divorce(marriage_date, divorce_date) is False:
                        us04Err = Error.Error(Error.ErrorEnum.US04)
                        us04Err.alterErrMsg(divorce_date, marriage_date)
                        errors.add(us04Err)

                if not MarriageValidation.valid_age_at_marriage(birthdate, marriage_date):
                    us10Err = Error.Error(Error.ErrorEnum.US10)
                    us10Err.alterErrMsg(s, f)
                    errors.add(us10Err)

        # print(family)
        # print(members)

        return {'family': family, 'members': members}


def pretty_table(parsed_file_dict):
    # Set up PrettyTable
    x = PrettyTable()
    x.field_names = ['ID', 'Name', 'Gender', 'Birthday', 'Age', 'Alive?', 'Death', 'Child', 'Spouse']

    y = PrettyTable()
    y.field_names = ['ID', 'Married', 'Divorced', 'Spouse 1 ID', 'Spouse 1 Name', 'Spouse 2 ID', 'Spouse 2 Name', 'Children']

    print('== Individuals ==')
    for k in parsed_file_dict['members'].keys():
        x.add_row([parsed_file_dict['members'][k]['ID'], parsed_file_dict['members'][k]['Name'],
                   parsed_file_dict['members'][k]['Gender'], parsed_file_dict['members'][k]['Birthday'],
                   parsed_file_dict['members'][k]['Age'],
                   parsed_file_dict['members'][k]['Alive?'], parsed_file_dict['members'][k]['Death'],
                   parsed_file_dict['members'][k]['Child'], parsed_file_dict['members'][k]['Spouse']])
    print(x)
    print('\n== Families ==')
    for k in parsed_file_dict['family'].keys():
        y.add_row([k, parsed_file_dict['family'][k]['Married'], parsed_file_dict['family'][k]['Divorced'],
                   parsed_file_dict['family'][k]['Spouse 1'], parsed_file_dict['family'][k]['Spouse 1 Name'],
                   parsed_file_dict['family'][k]['Spouse 2'], parsed_file_dict['family'][k]['Spouse 2 Name'],
                   parsed_file_dict['family'][k]['Children']])

    print(y)

# Main
if __name__ == '__main__':
    # Validate command line args
    if len(sys.argv) < 2:
        print('Usage Error: No input file provided')
        quit()

    # File validation
    fileName, fileExtension = os.path.splitext((cwd + '/' + sys.argv[1]))

    if fileExtension != '.ged':
        print('Error input file must be in .ged format')
        quit()

    fileName += fileExtension

    parsed_file = parse_file(fileName)

    # US11 - Check for bigamy
    if not MarriageValidation.bigamy_check(parsed_file):
        us11Err = Error.Error(Error.ErrorEnum.US11)
        errors.add(us11Err)

    # US14 - Check for multiple births
    errors = FamilyValidation.check_multiple_births(parsed_file, errors)

    # Output the table
    pretty_table(parsed_file)

    print('Errors: ')
    if len(errors) == 0:
        print('None')
    else:
        for e in errors:
            print(e.getErrMsg())
