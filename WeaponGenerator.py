'''
 ___  _____     Python - Magic Weapon Generator for D&D 3.5 - Version 0.02
|    |_   _|    Baseline of the code is ready.
|   _  | |      Types of weapons are in, still have to think about magic weapons work. Started adding magical effects. Modifiers are a thing too... I forgot... I will add them later even though they really depend mostly on the encounter level... Stream of consciusness here, I'll think about it when i get some sleep
|___|  | |      Some magical effects are not indicated in any manual of D&D and might be a little bit too OP, feel free to adapt them!
      /_ /      Pietro Goodjohn Bongiovanni - November 2015
'''

from random import randint

def categoryOfWeapon(int):
    global weaponType
    if int > 100 or int == 0:
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
        else:
            magicWeapon = 'Oops something went wrong in chosing type of weapon, %r' % string
            weaponDamage = 'Check it out :&'
            return
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
        else:
            magicWeapon = 'Oops something went wrong in chosing type of weapon, %r' % string
            weaponDamage = 'Check it out :&'
            return
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
        else:
            magicWeapon = 'Oops something went wrong in chosing type of weapon, %r' % string
            weaponDamage = 'Check it out :&'
            return
    elif string == 'Magic': # Still have to figure out how to generate wands and staff... Right now i decide every time it generates one
                            # I'll think about an automation when I finish my finals at school and the rest of the code I'm working on
        if dice > 0 and dice < 51:
            magicWeapon = 'Wand'
            weaponDamage = 'n charges of random spell'
        elif dice > 20 and dice < 101:
            magicWeapon = 'Staff'
            weaponDamage = '1d6, 19-20 x2, n charges of random spell'
        else:
            magicWeapon = 'Oops something went wrong in chosing type of weapon, %r' % string
            weaponDamage = 'Check it out'
            return
    else:
        magicWeapon = 'Oops something went wrong!'
        weaponDamage = '%s was not an expected string' % string

def magicEffect(int):
    global effect
    global name
    #dice = randint(1, 30)
    if dice == 1:
        global subdice
        subdice = randint(1,6)
        if subdice == 1:
            name = 'of powerful Strength'
            effect = 'Increase strength of +3'
        elif subdice == 2:
            name = 'of powerful Dexterity'
            effect = 'Increase dexterity of +3'
        elif subdice == 3:
            name = 'of powerful Costitution'
            effect = 'Increase constitution of +3'
        elif subdice == 4:
            name = 'of powerful Intelligence'
            effect = 'Increase intelligence of +3'
        elif subdice == 5:
            name = 'of powerful Wisdom'
            effect = 'Increase wisdom of +3'
        elif subdice == 6:
            name = 'of powerful Charisma'
            effect = 'Increase charisma of +3'
        else:
            name = 'Ooops something whent wrong when dice was equal to %d and subdice to %d' % (dice, subdice)
            effect = ''
    elif dice == 2:
        name = 'of Strength'
        effect = 'Increase Strength of +2'
    elif dice == 3:
        name = ' '
        effect = ' '
    elif dice == 4:
        name = 'of the Evil Slaughter'
        effect = 'basic attacks deal +2d6 damage to Evil targets'
    elif dice == 5:
        name = 'of Detect Good'
        effect = 'grants the wielder the ability to Detect Good' #unlimited time? some times a day? Still have to think about it
    elif dice == 6:
        name = 'of Freezing'
        effect = '25% chance of freezing an enemy for one round'
    elif dice == 7:
        name = 'of Lockpicking'
        effect = 'once per day, the wielder can pick a lock he wants for free'
    elif dice == 8:
        name = 'of Invisibility'
        effect = 'grants invisibility to the wielder 1 minute per day'
    elif dice == 9:
        name = 'of the Humanoid Slayer'
        effect = 'basic attacks deal +3d6 to humanoid targets'
    elif dice == 10:
        name = 'of Detect Magic'
        effect = 'once a day, grants the wielder a successful action of Detect Magic'
    elif dice == 11:
        name = 'of Light'
        effect = 'creates light in a circular region around the wielder with range 9m'
    elif dice == 12:
        subdice = randint (1,3)
        if subdice == 1:
            name = 'of strong Reflexes'
            effect = 'The wielder gets a bonus of +3 to his Reflexes saving throw'
        elif subdice == 2:
            name = 'of strong Fortitude'
            effect = 'The wielder gets a bonus of +3 to his Fortitude saving throw'
        elif subdice == 3:
            name = 'of strong Will'
            effect = 'The wielder gets a bonus of +3 to his Will saving throw'
        else:
            name = 'Ooops something went wrong when dice was equal to %d and subdice to %d' % (dice, subdice)
            effect = ''
    elif dice == 13:
        name = ''
        effect = ''
    elif dice == 14:
        name = 'of Dexterity'
        effect = 'increase dexterity of +2'
    elif dice == 15:
        name = 'of Revelation'
        effect = 'once per day, reveals to the wielder the position of all the enemies in a room'
    elif dice == 16:
        name = 'of Darkvision'
        effect = 'grants darkvision to the wielder'
    elif dice == 17:
        name = 'of Persuation'
        effect = 'once per day, grants the ability to the wielder to obtain anything he wants from a person'
    elif dice == 18:
        name = 'of Transmutation'
        effect = 'Once per day, can transmute any material into gold, the transformation will last for one hour'
        effect = effect + ' The amount of gold produced is equal to 1/5 of the weight of material transuted'
    elif dice == 19:
        name = 'of Fortitude'
        effect = 'The wielder gets a bonus of +2 to his Fortitude saving throw'
    elif dice == 20:
        name = 'of Wisdom'
        effect = 'Increases Wisdom of +2'
    elif dice == 21:
        name = 'of Magic Leaking'
        effect = 'Basic attacks have a 25% chance of inflicting Magic Leaking for 1d4 turns (1d4 damage per turn, stacking)'
    elif dice == 22:
        name = 'of the Disorder Seeker'
        effect = 'Basic attacks of the wielder deal +2d6 damage to neutral creatures'
    elif dice == 23:
        name = 'of Charisma'
        effect = 'Increases Charisma of +2'
    elif dice == 24:
        name = 'of Absorption'
        effect = 'Each time the wielder kills an enemy, this weapon gains the power of the enemy\'s weapons'
    elif dice == 25:
        name = 'of Magic Shield'
        effect = 'Once per day, the wielder gains a Magic Shield (+3 AC) for one minute'
    elif dice == 26:
        name = ''
        effect = ''
    elif dice == 27:
        name = 'of Defence'
        effect = '+2 AC'
    elif dice == 28:
        name = 'of Reflexes'
        effect = 'The wielder gets a bonus of +2 to his Reflexes saving throw'
    elif dice == 29:
        name = ''
        effect = ''
    elif dice == 30:
        name = 'of Lifestealing'
        effect = 'Basic attacks have 25% chance of healing the wielder of 1d4hp'
    elif dice == 31:
        name = 'of Order Bringer'
        effect = 'Basic attacks deals +2d6 vs chaotic targets'
    elif dice == 32:
        name = 'of Seeking the Invisible'
        effect = 'The wielder gains the ability to see invisible things for one minute per day'
    elif dice == 33:
        name = 'of Detect Evil'
        effect = 'Grants the wielder the ability to Detect Good' #same situation of detect good
    elif dice == 34:
        name = ''
        effect = ''
    elif dice == 35:
        name = 'of Will'
        effect = 'The wielder gets a bonus of +2 to his Will saving throw'
    elif dice == 36:
        name = 'of Spell Storing'
        effect = 'can store any spell and launch it once per day, but it must be charged by a spellcaster'
    elif dice == 37:
        name = 'of Rapidity'
        effect = 'Grants the wielder the ability to perform another full attack per turn'
    elif dice == 38:
        name = 'of Range'
        effect = 'Melee weapon have 1,5m of extended range; ranged weapons have 30m of extended range'
    elif dice == 39:
        name = 'of Sunfire'
        effect = 'Deals 1d4 damage every turn to adjacent enemies'
    elif dice == 40:
        name = 'of Intelligence'
        effect = 'Increases the Intelligence of +2'
    elif dice == 41:
        name = 'of Discord'
        effect = 'Deals 1d8 extra damage, it has a 50% chance of hitting the wrong target'
    elif dice == 42:
        name = 'of the Diehard'
        effect = 'Grants the wielder the feat of Diehard'
    elif dice == 43:
        name = ''
        effect = ''
    elif dice == 44:
        name = ''
        effect = ''
    elif dice == 45:
        name = ''
        effect = ''
    elif dice == 46:
        name = ''
        effect = ''
    elif dice == 47:
        name = ''
        effect = ''
    elif dice == 48:
        name = ''
        effect = ''
    elif dice == 49:
        name = ''
        effect = ''
    elif dice == 50:
        name = ''
        effect = ''
    else:
        name = 'Ooops something went wrong when dice was equal to %d' % dice
        effect = ''

dice = randint(1, 100)
#print weaponGenerated

categoryOfWeapon(dice)
#print weaponType

typeOfWeapon(weaponType)

dice = randint (1, 40)

magicEffect(dice)

print magicWeapon + ' ' + name + '.'
print weaponDamage + '; ' + effect + '.'

'''
if dice > 0 and < 26:
    pass
elif dice > 25 and < 51:
    pass
elif dice > 51 and dice < 76:
    pass
elif dice > 76 and dice < 101:
    pass

elif dice == :
    name = ''
    effect = ''
'''
