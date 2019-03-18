from datetime import datetime
from MarriageValidation import create_date
import re

######################################
#### US 9 
#### Check that the birth was before 
#### the death of the parents
######################################

def old_birth_before_death(tags, ged_file):
    for family in ged_file: #loop through the gedcom file
        if family['CHIL'] != 'NONE' and family['MARR'] != 'NONE': #if they have child and are married
            get_husband = int(re.sub('\D', '', str(family['HUSB'])))-1 #extract husband
            get_wife = int(re.sub('\D', '', str(family['WIFE'])))-1 #extract wife
            
            
            for child in family['CHIL']: #loop through gedcom file

                get_child = int(re.sub('\D', '',child))-1 #get children
                calc_birth = datetime.strptime(tags[get_child]['BIRT'], '%Y-%m-%d') #determine date of birth of child

                #determine if child died before mother's death
                if tags[get_wife]['DEAT'] != 'NA' and datetime.strptime(tags[get_wife]['DEAT'], '%Y-%m-%d') < calc_birth:
                    print('Error, birth occurred after mothers death!')
                    return False

                #determine if child died before father's death
                if tags[get_husband]['DEAT'] != 'NA' and datetime.strptime(tags[get_husband]['DEAT'], '%Y-%m-%d') < calc_birth:
                    print('Error, birth occurred after fathers death!')
                    return False
    
    return True

# retains the date comparison logic from above, but receives input during file data read
def birt_before_death(birth, death):
    if death < birth:
        return False
    return True


# utilizing dict from parsed file
def birth_before_death(parent_death, child_birth):
    p_death = create_date(parent_death.split(' ', 2)[2], parent_death.split(' ', 2)[1], parent_death.split(' ', 2)[0])
    c_birth = create_date(child_birth.split(' ', 2)[2], child_birth.split(' ', 2)[1], child_birth.split(' ', 2)[0])

    if p_death == c_birth:
        return True
    elif p_death.year > c_birth.year:
        return True
    elif p_death.year == c_birth.year and p_death.month > c_birth.month:
        return True
    elif p_death.year == c_birth.year and p_death.month == c_birth.month and p_death.day > c_birth.day:
        return True
    else:
        return False

