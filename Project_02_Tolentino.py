# Jonathan P. Tolentino
# CS 555
# Project 02
# 02/02/2019

'''
1. Modify the program to save information about individuals and families in lists (or collections)
so that they can be examined later. You may assume that the number of individuals in any file is always
less than 5000, and the number of families is always less than 1000. (The team should agree on how this is done,
but only one team member needs to do this.)

2. After reading all of the data, print the unique identifiers and names of each of the individuals in order by their
unique identifiers. Then, for each family, print the unique identifiers and names of the husbands and wives, in order
by unique family identifiers. (The team should agree on how this is done, but only one team member needs to do this.)
'''


import sys
import os
from datetime import date

cwd = os.path.dirname(os.path.realpath(__file__))


class GEDCOM_Line:

    Level = 0
    Tag = 'default'
    Valid = 'N'
    Args = ''

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
                     'DIV', 'DATE', 'HEAD', 'TRLR', 'NOTE'}

        if self.Tag in validTags:
            self.Valid = 'Y'
        else:
            self.Valid = 'N'


months = {'JAN': 1, 'FEB': 2, 'MAR': 3, 'APR': 4, 'MAY': 5, 'JUN': 6,
          'JUL': 7, 'AUG': 8, 'SEP': 9, 'OCT': 10, 'NOV': 11,'DEC': 12}


def calculate_age(birthday):
    today = date.today()
    return today.year - birthday.year - ((today.month, today.day) < (birthday.month, birthday.day))

def calculate_age_death(birthday, death_day):
    return death_day.year - birthday.year - ((death_day.month, death_day.day) < (birthday.month, birthday.day))


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

try:
    with open(fileName) as gedFile:

        family = {}
        individual = {}
        members = {}

        currentIndi, currentFam, currentTag = '', '', ''


        line = gedFile.readline()

        # Parse the file
        while line:
            gedLine = GEDCOM_Line()
            gedLine.Parse(line)
            gedLine.Validate()
            line = line.rstrip()
            line = line.split(' ', 2)

            if line[0] == '0' and len(line) == 3:
                if individual:
                    members[individual['ID']] = individual
                    individual = {}

                if gedLine.Valid == 'Y':
                    if line[2] == 'INDI':
                        if line[1] not in members.keys():
                            individual['ID'] = line[1]
                            individual['Child'] = set()
                            individual['Spouse'] = set()
                            # print(individual)
                            currentTag = line[2]
                            line = gedFile.readline()
                            continue
                    if line[2] == 'FAM':
                        if line[1] not in family.keys():
                            family[line[1]] = {'Children': set()}
                            # print(family)
                            currentTag = line[2]
                            currentFam = line[1]
                            line = gedFile.readline()
                            continue
            elif len(line) == 2:
                if gedLine.Valid == 'Y':
                    currentTag = line[1]
                    line = gedFile.readline()
                    continue
            elif line[1] == 'HUSB' or line[1] == 'WIFE' or line[1] == 'CHIL':
                if gedLine.Valid == 'Y':
                    currentTag = line[1]

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
                            individual['Birthday'] = line[2]
                            currentTag = 'INDI'

            if currentTag == 'DEAT':
                if line[0] != 0 and len(line) == 3:
                    if gedLine.Valid == 'Y':
                        if line[1] == 'DATE':
                            individual['Death'] = line[2]
                            currentTag = 'INDI'

            if currentTag == 'MARR':
                if line[0] != 0 and len(line) == 3:
                    if gedLine.Valid == 'Y':
                        if line[1] == 'DATE':
                            family[currentFam]['Married'] = line[2]

            if currentTag == 'DIV':
                if line[0] != 0 and len(line) == 3:
                    if gedLine.Valid == 'Y':
                        if line[1] == 'DATE':
                            family[currentFam]['Divorced'] = line[2]

            if currentTag == 'HUSB':
                if line[0] != 0 and len(line) == 3:
                    if gedLine.Valid == 'Y':
                        family[currentFam]['Spouse 1'] = line[2]

            if currentTag == 'WIFE':
                if line[0] != 0 and len(line) == 3:
                    if gedLine.Valid == 'Y':
                        family[currentFam]['Spouse 2'] = line[2]

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

    for k in family.keys():
        family[k]['Spouse 1 Name'] = members[family[k]['Spouse 1']]['Name']
        family[k]['Spouse 2 Name'] = members[family[k]['Spouse 2']]['Name']

    for k, v in members.items():
        if 'Death' in members[k].keys():
            members[k]['Alive?'] = 'N'
            birthday = members[k]['Birthday'].split(' ', 2)
            death_day = members[k]['Death'].split(' ', 2)
            members[k]['Age'] = calculate_age_death(date(int(birthday[2]), int(months[birthday[1]]), int(birthday[0])),
                                                    date(int(death_day[2]), int(months[death_day[1]]), int(death_day[0])))
        else:
            members[k]['Alive?'] = 'Y'
            birthday = members[k]['Birthday'].split(' ', 2)
            members[k]['Age'] = calculate_age(date(int(birthday[2]), int(months[birthday[1]]), int(birthday[0])))

        if len(members[k]['Child']) == 0:
            members[k]['Child'] = 'NA'

        if len(members[k]['Spouse']) == 0:
            members[k]['Spouse'] = 'NA'

    print('== Individuals ==\n')
    for k,v in members.items():
        print(k, v)
    print('\n== Families ==\n')
    for k, v in family.items():
        print(k, v)

    gedFile.close()
