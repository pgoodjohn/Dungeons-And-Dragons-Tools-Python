'''
 ___  _____     Python - Wand Generator - v 1.0
|    |_   _|
|   _  | |
|___|  | |
      /_ /      Pietro Goodjohn Bongiovanni - December 2015
'''

from random import randint

def generateWand():
    '''
    Druid /Warrior / Thief / Mage / Monk / Paladin / Ranger / Wizard
    '''
    dice = randint(1,2)
    #BARD
    if dice == 1:
        dice = randint(0,6)
        if(dice == 0):
            bard = [line.strip() for line in open("/Users/pietrobongiovanni/GitHub/Dungeons-And-Dragons-Tools-Python/SingleScripts/WeaponGenerator/DatFiles/Bard/Bard0SpellList.txt", 'r')]
            spell = 'Lvl 0 '
        elif(dice == 1):
            bard = [line.strip() for line in open("/Users/pietrobongiovanni/GitHub/Dungeons-And-Dragons-Tools-Python/SingleScripts/WeaponGenerator/DatFiles/Bard/Bard1SpellList.txt", 'r')]
            spell = 'Lvl 1 '
        elif(dice == 2):
            bard = [line.strip() for line in open("/Users/pietrobongiovanni/GitHub/Dungeons-And-Dragons-Tools-Python/SingleScripts/WeaponGenerator/DatFiles/Bard/Bard2SpellList.txt", 'r')]
            spell = 'Lvl 2 '
        elif(dice == 3):
            bard = [line.strip() for line in open("/Users/pietrobongiovanni/GitHub/Dungeons-And-Dragons-Tools-Python/SingleScripts/WeaponGenerator/DatFiles/Bard/Bard3SpellList.txt", 'r')]
            spell = 'Lvl 3 '
        elif(dice == 4):
            bard = [line.strip() for line in open("/Users/pietrobongiovanni/GitHub/Dungeons-And-Dragons-Tools-Python/SingleScripts/WeaponGenerator/DatFiles/Bard/Bard4SpellList.txt", 'r')]
            spell = 'Lvl 4 '
        elif(dice == 5):
            bard = [line.strip() for line in open("/Users/pietrobongiovanni/GitHub/Dungeons-And-Dragons-Tools-Python/SingleScripts/WeaponGenerator/DatFiles/Bard/Bard5SpellList.txt", 'r')]
            spell = 'Lvl 5 '
        elif(dice == 6):
            bard = [line.strip() for line in open("/Users/pietrobongiovanni/GitHub/Dungeons-And-Dragons-Tools-Python/SingleScripts/WeaponGenerator/DatFiles/Bard/Bard6SpellList.txt", 'r')]
            spell = 'Lvl 6 '
        else:
            bard = 'derp'
            return bard
        dice = randint(0, len(bard)-1)
        spell = spell + bard[dice]
    #CLERIC
    elif dice == 2:
        dice = randint(0,9)
        if(dice == 0):
            cleric = [line.strip() for line in open("/Users/pietrobongiovanni/GitHub/Dungeons-And-Dragons-Tools-Python/SingleScripts/WeaponGenerator/DatFiles/Cleric/Cleric0SpellList.txt", 'r')]
            spell = 'Lvl 0 '
        elif(dice == 1):
            cleric = [line.strip() for line in open("/Users/pietrobongiovanni/GitHub/Dungeons-And-Dragons-Tools-Python/SingleScripts/WeaponGenerator/DatFiles/Cleric/Cleric1SpellList.txt", 'r')]
            spell = 'Lvl 1 '
        elif(dice == 2):
            cleric = [line.strip() for line in open("/Users/pietrobongiovanni/GitHub/Dungeons-And-Dragons-Tools-Python/SingleScripts/WeaponGenerator/DatFiles/Cleric/Cleric2SpellList.txt", 'r')]
            spell = 'Lvl 2 '
        elif(dice == 3):
            cleric = [line.strip() for line in open("/Users/pietrobongiovanni/GitHub/Dungeons-And-Dragons-Tools-Python/SingleScripts/WeaponGenerator/DatFiles/Cleric/Cleric3SpellList.txt", 'r')]
            spell = 'Lvl 3 '
        elif(dice == 4):
            cleric = [line.strip() for line in open("/Users/pietrobongiovanni/GitHub/Dungeons-And-Dragons-Tools-Python/SingleScripts/WeaponGenerator/DatFiles/Cleric/Cleric4SpellList.txt", 'r')]
            spell = 'Lvl 4 '
        elif(dice == 5):
            cleric = [line.strip() for line in open("/Users/pietrobongiovanni/GitHub/Dungeons-And-Dragons-Tools-Python/SingleScripts/WeaponGenerator/DatFiles/Cleric/Cleric5SpellList.txt", 'r')]
            spell = 'Lvl 5 '
        elif(dice == 6):
            cleric = [line.strip() for line in open("/Users/pietrobongiovanni/GitHub/Dungeons-And-Dragons-Tools-Python/SingleScripts/WeaponGenerator/DatFiles/Cleric/Cleric6SpellList.txt", 'r')]
            spell = 'Lvl 6 '
        elif(dice == 7):
            cleric = [line.strip() for line in open("/Users/pietrobongiovanni/GitHub/Dungeons-And-Dragons-Tools-Python/SingleScripts/WeaponGenerator/DatFiles/Cleric/Cleric7SpellList.txt", 'r')]
            spell = 'Lvl 7 '
        elif(dice == 8):
            cleric = [line.strip() for line in open("/Users/pietrobongiovanni/GitHub/Dungeons-And-Dragons-Tools-Python/SingleScripts/WeaponGenerator/DatFiles/Cleric/Cleric8SpellList.txt", 'r')]
            spell = 'Lvl 8 '
        elif(dice == 9):
            cleric = [line.strip() for line in open("/Users/pietrobongiovanni/GitHub/Dungeons-And-Dragons-Tools-Python/SingleScripts/WeaponGenerator/DatFiles/Cleric/Cleric9SpellList.txt", 'r')]
            spell = 'Lvl 9 '
        else:
            cleric = 'derp'
        dice = randint(0, len(cleric)-1)
        spell = spell + cleric[dice]

    return spell
