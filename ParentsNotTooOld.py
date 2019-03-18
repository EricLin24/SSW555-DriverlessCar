import re
from MarriageValidation import create_date, at_least_age

#############################################
#### US 12
#### Check that the parents aren't too old 
#############################################

def old_parents_too_old(tags, ged_file):
    for family in ged_file: #loop through ged file
        if family['CHIL']:
            get_husband = int(re.sub('\D', '', str(family['HUSB']))) - 1 #extract husband
            get_wife = int(re.sub('\D', '', str(family['WIFE']))) - 1 #extract wife
            
            for children in family['CHIL']: #for each child in family
                get_child = int(re.sub('\D', '', children)) - 1 #extract child
                get_age = tags[get_child]['AGE'] #get age

                if int(tags[get_wife]['AGE']) - int(get_age) > 60: #check if moms age is older than 60
                    print('Mother is too old.')
                    return False
                
                if int(tags[get_husband]['AGE']) - int(get_age) > 80: #check if father's age is older than 80
                    print('Father is too old')
                    return False
        
    return True

# retains the date comparison logic from above, but receives input during file data read
def check_parent_age(parent_age, old_age):
    if old_age > parent_age:
        return False
    return True


def parent_age_check(max_age, parent_birth, child_birth):
    p_birth = create_date(parent_birth.split(' ', 2)[2], parent_birth.split(' ', 2)[1], parent_birth.split(' ', 2)[0])
    c_birth = create_date(child_birth.split(' ', 2)[2], child_birth.split(' ', 2)[1], child_birth.split(' ', 2)[0])

    if at_least_age(max_age, p_birth, c_birth) is True:
        return False

    return True



