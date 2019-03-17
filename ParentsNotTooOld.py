import re

#############################################
#### US 13
#### Check that the parents aren't too old 
#############################################

def parents_too_old(tags, ged_file):
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
