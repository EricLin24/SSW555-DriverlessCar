from datetime import datetime
import re

######################################
#### US 9 
#### Check that the birth was before 
#### the death of the parents
######################################

def birth_before_death(tags, ged_file):
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



    