from datetime import datetime
import re


def marriage_before_death(tags, ged_file): # pass in the tags and the gedcom file
    for person in tags: # loop through each tag
        if person['SPOUSE'] != 'NONE' and person['DEAT'] != 'NA': # if the person has a spouse and they are not dead (yet)
            date_of_death = datetime.strptime(person['DEAT'], '%Y-%m-%d') # date of death = strip the date from the death tag (use regex to get the year, month and day)
            for spouse in person['SPOUSE']: 
                family = int(re.sub('\D', '', spouse)) - 1
                marriage_date = datetime.strptime(ged_file[family]['MARR'], '%Y-%m-%d') # marriage date
                if marriage_date > date_of_death: # if marriage date is marriage date is greater than the date of date
                    print("Fail") # print error message
                    return False

    return True # if it is less than, than success


# retains the date comparison logic from above, but receives input during file data read
def marr_before_death(divorce, death):
    if divorce > death:
        return False
    return True
