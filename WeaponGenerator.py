'''
 ___  _____     Python - Magic Weapon Generator for D&D 3.5 - Version 0.0
|    |_   _|    Just wrote the baseline of the code
|   _  | |      I'll get to add all the kind of weapons I thought and all the magical effects.
|___|  | |      Some magical effects are not indicated in any manual of D&D and might be a little bit too OP, feel free to adapt them!
      /_ /      Pietro Goodjohn Bongiovanni - November 2015
'''

from random import randint

def categoryOfWeapon(int):
    global weaponType
    if int > 100:
        print 'something wrong brah'
    else:
        print 'everything\'s cool brah'
        if int > 0 and int < 26:
            weaponType = 'Dagger'
            #print 'i did change'
        elif int > 25 and int < 51:
            weaponType = 'Sword'
        elif int > 51 and int < 76:
            weaponType = 'Ranged'
        elif int > 76 and int < 101:
            weaponType = 'Magic'

def typeOfWeapon(string):
    dice = randint(1,100)

    if string == 'Dagger':
        if dice > 0 and < 26:
            pass
        elif dice > 25 and < 51:
            pass
        elif dice > 51 and dice < 76:
            pass
        elif dice > 76 and dice < 101:
            pass

weaponGenerated = randint(1, 100)
#print weaponGenerated

typeOfWeapon(weaponGenerated)

print weaponType

'''
if dice > 0 and < 26:
    pass
elif dice > 25 and < 51:
    pass
elif dice > 51 and dice < 76:
    pass
elif dice > 76 and dice < 101:
    pass
'''
