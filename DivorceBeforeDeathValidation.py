from datetime import datetime
import re

def divorce_before_death(tags, ged_file): # pass in the tags and gedcom file
    for person in tags: # loop through each tag
        if person['SPOUSE'] != 'NONE' and person['DEAT'] != 'NA': # if the person has a spouse and are not dead
            death = datetime.strptime(person['DEAT'], '%Y-%m-%d') # date of death and use regex to extract date
            for spouse in person['SPOUSE']: # for each spouse
                family = int(re.sub('\D', '', spouse)) - 1
                if ged_file[family]['DIV'] != 'NONE': # check gedcom file family
                    divorce = datetime.strptime(ged_file[family]['DIV'], '%Y-%m-%d') # extract divorce date
                    if divorce > death:
                        print("Fail")
                        return False
    return True


# retains the date comparison logic from above, but receives input during file data read
def div_before_death(divorce, death):
    if divorce > death:
        return False
    return True
