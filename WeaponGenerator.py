'''
 ___  _____     Python - Magic Weapon Generator for D&D 3.5 - Version 0.01
|    |_   _|    Just wrote the baseline of the code
|   _  | |      I'll get to add all the kind of weapons I thought and all the magical effects.
|___|  | |      Some magical effects are not indicated in any manual of D&D and might be a little bit too OP, feel free to adapt them!
      /_ /      Pietro Goodjohn Bongiovanni - November 2015
'''

from random import randint

def categoryOfWeapon(int):
    global weaponType
    if int > 100:
        print 'Something went wrong with the dice roller.'
    else:
        #print 'Dice roller working properly"
        if int > 0 and int < 26:
            weaponType = 'Sword' # Swords, dagger, schyte
        elif int > 25 and int < 51:
            weaponType = 'Ranged' # Bows, crossbows
        elif int > 50 and int < 76:
            weaponType = 'Hammer' # Axes, Hammers, Maces
        elif int > 75 and int < 101:
            weaponType = 'Magic' # Wands, Staffs

def typeOfWeapon(string):
    dice = randint(1,100)
    global magicWeapon
    global weaponDamage

    #print dice

    if string == 'Sword':
        if dice > 0 and dice < 21:
            magicWeapon = 'Dagger'
            weaponDamage = '1d4, 19-20 x2'
        elif dice > 20 and dice < 41:
            magicWeapon = 'Longsword (1H)'
            weaponDamage = '1d6, 19-20 x2'
        elif dice > 40 and dice < 61:
            magicWeapon = 'Greatsword (2H)'
            weaponDamage = '2d6, 19-20 x2'
        elif dice > 60 and dice < 81:
            magicWeapon = 'Schyte (2H)'
            weaponDamage = '2d4, x4'
        elif dice > 80 and dice < 101:
            magicWeapon = 'Bastard Sword'
            weaponDamage = '1d10, 19-20 x2'
    elif string == 'Ranged':
        if dice > 0 and dice < 13:
            magicWeapon = 'Crossbow'
            weaponDamage = '1d8, 19-20 x2'
        elif dice > 12 and dice < 38:
            magicWeapon = 'Longbow'
            weaponDamage = '1d8, x3'
        elif dice > 37 and dice < 51:
            magicWeapon = 'Composite Longbow'
            weaponDamage = '1d8, x3'
        elif dice > 50 and dice < 76:
            magicWeapon = 'Shortbow'
            weaponDamage = '1d6, x3'
        elif dice > 75 and dice < 88:
            magicWeapon = 'Composite Shortbow'
            weaponDamage = '1d6, x3'
        elif dice > 87 and dice <101:
            magicWeapon = 'Repeating Crossbow'
            weaponDamage = '1d8, 19-20 x2'
    elif string == 'Hammer':
        if dice > 0 and dice < 26:
            magicWeapon = 'Morningstar (1H)'
            weaponDamage = '1d8, x2'
        elif dice > 25 and dice < 51:
            magicWeapon = 'Warhammer (1H)'
            weaponDamage = '1d8, x3'
        elif dice > 50 and dice < 76:
            magicWeapon = 'Waraxe (1H)'
            weaponDamage = '1d10, x3'
        elif dice > 75 and dice < 86:
            magicWeapon = 'Greataxe (2H)'
            weaponDamage = '1d12, x3'
        elif dice > 85 and dice < 96:
            magicWeapon = 'Great club (2H)'
            weaponDamage = '1d10, x2'
        elif dice > 95 and dice < 101:
            magicWeapon = 'Great Hammer (2H, requireas 18 in strenght)'
            weaponDamage = '1d12, 19-20 x3'
    elif string == 'Magic': # Still have to figure out how to generate wands and staff... Right now i decide every time it generates one
                            # I'll think about an automation when I finish my finals at school
        if dice > 0 and dice < 51:
            magicWeapon = 'Wand'
            weaponDamage = 'n charges of random spell'
        elif dice > 20 and dice < 41:
            magicWeapon = 'Staff'
            weaponDamage = '1d6, 19-20 x2, n charges of random spell'
    else:
        magicWeapon = 'something went wrong'
        weaponDamage = 'oops'


weaponGenerated = randint(1, 100)
#print weaponGenerated

categoryOfWeapon(weaponGenerated)

#print weaponType

typeOfWeapon(weaponType)

print magicWeapon + ' ' + weaponDamage

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
