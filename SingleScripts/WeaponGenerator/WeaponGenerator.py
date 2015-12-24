'''
 ___  _____     Python - Magic Weapon Generator for D&D 3.5 - Version 0.1
|    |_   _|
|   _  | |
|___|  | |
      /_ /      Pietro Goodjohn Bongiovanni - November 2015
'''

from random import randint
import WandGenerator as wg

def categoryOfWeapon():
    dice = randint(1, 4)
    if dice == 1:
        weaponType = 'Sword' # Swords, dagger, schyte
    elif dice == 2:
        weaponType = 'Ranged' # Bows, crossbows
    elif dice == 3:
        weaponType = 'Hammer' # Axes, Hammers, Maces
    elif dice == 4:
        weaponType = 'Magic' # Wands, Staffs
    return weaponType

def typeOfWeapon(string):
    global magicWeapon
    global weaponDamage
    global flag
    flag = 0
    if string == 'Sword':
        dice = randint(1,5)
        if dice == 1:
            magicWeapon = 'Dagger'
            weaponDamage = '1d4, 19-20 x2.'
        elif dice == 2:
            magicWeapon = 'Longsword (1H)'
            weaponDamage = '1d6, 19-20 x2.'
        elif dice == 3:
            magicWeapon = 'Greatsword (2H)'
            weaponDamage = '2d6, 19-20 x2.'
        elif dice == 4:
            magicWeapon = 'Schyte (2H)'
            weaponDamage = '2d4, x4.'
        elif dice == 5:
            magicWeapon = 'Bastard Sword'
            weaponDamage = '1d10, 19-20 x2.'
        else:
            magicWeapon = 'Oops something went wrong in chosing type of weapon, %r' % string
            weaponDamage = 'Check it out.'
            return
    elif string == 'Ranged':
        dice = randint(1,100)
        if dice > 0 and dice < 13:
            magicWeapon = 'Crossbow'
            weaponDamage = '1d8, 19-20 x2.'
        elif dice > 12 and dice < 38:
            magicWeapon = 'Longbow'
            weaponDamage = '1d8, x3.'
        elif dice > 37 and dice < 51:
            magicWeapon = 'Composite Longbow'
            weaponDamage = '1d8, x3.'
        elif dice > 50 and dice < 76:
            magicWeapon = 'Shortbow'
            weaponDamage = '1d6, x3.'
        elif dice > 75 and dice < 88:
            magicWeapon = 'Composite Shortbow'
            weaponDamage = '1d6, x3.'
        elif dice > 87 and dice <101:
            magicWeapon = 'Repeating Crossbow'
            weaponDamage = '1d8, 19-20 x2.'
        else:
            magicWeapon = 'Oops something went wrong in chosing type of weapon, %r' % string
            weaponDamage = 'Check it out.'
            return
    elif string == 'Hammer':
        dice = randint(1,100)
        if dice > 0 and dice < 26:
            magicWeapon = 'Morningstar (1H)'
            weaponDamage = '1d8, x2.'
        elif dice > 25 and dice < 51:
            magicWeapon = 'Warhammer (1H)'
            weaponDamage = '1d8, x3.'
        elif dice > 50 and dice < 76:
            magicWeapon = 'Waraxe (1H)'
            weaponDamage = '1d10, x3.'
        elif dice > 75 and dice < 86:
            magicWeapon = 'Greataxe (2H)'
            weaponDamage = '1d12, x3.'
        elif dice > 85 and dice < 96:
            magicWeapon = 'Great club (2H)'
            weaponDamage = '1d10, x2.'
        elif dice > 95 and dice < 101:
            magicWeapon = 'Great Hammer (2H, requireas 18 in strenght)'
            weaponDamage = '1d12, 19-20 x3.'
        else:
            magicWeapon = 'Oops something went wrong in chosing type of weapon, %r' % string
            weaponDamage = 'Check it out'
            return
    elif string == 'Magic':
        dice = randint(1,2)
        if dice == 1:
            magicWeapon = 'Wand of '
            weaponDamage = wg.generateWand() + ' (50 charges)'
            flag = 1
        elif dice == 2:
            magicWeapon = 'Staff. '
            weaponDamage = '1d6, 19-20 x2,  '
            weaponDamage = weaponDamage + wg.generateWand() + ' (50 charges)'
            flag = 1
        else:
            magicWeapon = 'Oops something went wrong in chosing type of weapon, %r' % string
            weaponDamage = 'Check it out'
            return
    else:
        magicWeapon = 'Oops something went wrong!'
        weaponDamage = '%s was not an expected string' % string
    return magicWeapon + ' ' + weaponDamage

def magicEffect():
    global name
    global effect
    try:
        effects = [line.strip() for line in open("/Users/pietrobongiovanni/GitHub/Dungeons-And-Dragons-Tools-Python/SingleScripts/WeaponGenerator/DatFiles/MagicEffects.txt", 'r')]
    except:
        effects = 'Error'
    dice = randint (0, len(effects)-1)
    return effects[dice]

def generate():
    weaponCat = categoryOfWeapon()
    typeOfWeapon(weaponCat)
    effect = magicEffect()
    if flag == 0:
        if effect == '.':
            result = magicWeapon + effect + '\n' + weaponDamage
        else:
            result = magicWeapon + ' ' + effect + '\n' + weaponDamage
    else:
        result = magicWeapon + weaponDamage
    return result
