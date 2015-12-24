'''
 ___  _____     Python - Wand Generator - v 1.0
|    |_   _|    To do:
|   _  | |            -
|___|  | |
      /_ /      Pietro Goodjohn Bongiovanni - December 2015
'''

from random import randint

def generateWand():
    dice = randint(1,5)
    #BARD
    if dice == 1:
        dice = randint(0,100)
        if(dice < 50):
            try:
                bard = [line.strip() for line in open("/Users/pietrobongiovanni/GitHub/Dungeons-And-Dragons-Tools-Python/SingleScripts/WeaponGenerator/DatFiles/Bard/Bard0SpellList.txt", 'r')]
            except:
                bard = 'Error opening the file for Bard Level 0 Spells'
        elif(dice >= 50 and dice < 75):
            try:
                bard = [line.strip() for line in open("/Users/pietrobongiovanni/GitHub/Dungeons-And-Dragons-Tools-Python/SingleScripts/WeaponGenerator/DatFiles/Bard/Bard1SpellList.txt", 'r')]
            except:
                bard = 'Error opening the file for Bard Level 1 Spells'
        elif(dice >= 75 and dice < 90):
            try:
                bard = [line.strip() for line in open("/Users/pietrobongiovanni/GitHub/Dungeons-And-Dragons-Tools-Python/SingleScripts/WeaponGenerator/DatFiles/Bard/Bard2SpellList.txt", 'r')]
            except:
                bard = 'Error opening the file for Bard Level 2 Spells'
        elif(dice >= 90 and dice < 95):
            try:
                bard = [line.strip() for line in open("/Users/pietrobongiovanni/GitHub/Dungeons-And-Dragons-Tools-Python/SingleScripts/WeaponGenerator/DatFiles/Bard/Bard3SpellList.txt", 'r')]
            except:
                bard = 'Error opening the file for Bard Level 3 Spells'
        elif(dice >= 95):
            try:
                bard = [line.strip() for line in open("/Users/pietrobongiovanni/GitHub/Dungeons-And-Dragons-Tools-Python/SingleScripts/WeaponGenerator/DatFiles/Bard/Bard4SpellList.txt", 'r')]
            except:
                bard = 'Error opening the file for Bard Level 4 Spells'
        else:
            bard = 'Error with a dice.'
            return bard
        dice = randint(0, len(bard)-1)
        spell = bard[dice]
    #CLERIC
    elif dice == 2:
        dice = randint(0,100)
        if(dice < 50):
            try:
                cleric = [line.strip() for line in open("/Users/pietrobongiovanni/GitHub/Dungeons-And-Dragons-Tools-Python/SingleScripts/WeaponGenerator/DatFiles/Cleric/Cleric0SpellList.txt", 'r')]
            except:
                cleric = 'Error opening the file for Cleric Level 0 Spells'
        elif(dice >= 50 and dice < 75):
            try:
                cleric = [line.strip() for line in open("/Users/pietrobongiovanni/GitHub/Dungeons-And-Dragons-Tools-Python/SingleScripts/WeaponGenerator/DatFiles/Cleric/Cleric1SpellList.txt", 'r')]
            except:
                cleric = 'Error opening the file for Cleric Level 1 Spells'
        elif(dice >= 75 and dice < 90):
            try:
                cleric = [line.strip() for line in open("/Users/pietrobongiovanni/GitHub/Dungeons-And-Dragons-Tools-Python/SingleScripts/WeaponGenerator/DatFiles/Cleric/Cleric2SpellList.txt", 'r')]
            except:
                cleric = 'Error opening the file for Cleric Level 2 Spells'
        elif(dice >= 90 and dice < 95):
            try:
                cleric = [line.strip() for line in open("/Users/pietrobongiovanni/GitHub/Dungeons-And-Dragons-Tools-Python/SingleScripts/WeaponGenerator/DatFiles/Cleric/Cleric3SpellList.txt", 'r')]
            except:
                cleric = 'Error opening the file for Cleric Level 3 Spells'
        elif(dice >= 95):
            try:
                cleric = [line.strip() for line in open("/Users/pietrobongiovanni/GitHub/Dungeons-And-Dragons-Tools-Python/SingleScripts/WeaponGenerator/DatFiles/Cleric/Cleric4SpellList.txt", 'r')]
            except:
                cleric = 'Error opening the file for Cleric Level 4 Spells'
        else:
            cleric = 'derp'
        dice = randint(0, len(cleric)-1)
        spell = cleric[dice]
    #DRUID
    elif dice == 3:
        dice = randint(0,100)
        if(dice < 50):
            try:
                druid = [line.strip() for line in open("/Users/pietrobongiovanni/GitHub/Dungeons-And-Dragons-Tools-Python/SingleScripts/WeaponGenerator/DatFiles/Druid/Druid0SpellList.txt", 'r')]
            except:
                druid = 'Error opening the file for Druid Level 0 Spells'
        elif(dice >= 50 and dice < 75):
            try:
                druid = [line.strip() for line in open("/Users/pietrobongiovanni/GitHub/Dungeons-And-Dragons-Tools-Python/SingleScripts/WeaponGenerator/DatFiles/Druid/Druid1SpellList.txt", 'r')]
            except:
                druid = 'Error opening the file for Druid Level 1 Spells'
        elif(dice >= 75 and dice < 90):
            try:
                druid = [line.strip() for line in open("/Users/pietrobongiovanni/GitHub/Dungeons-And-Dragons-Tools-Python/SingleScripts/WeaponGenerator/DatFiles/Druid/Druid2SpellList.txt", 'r')]
            except:
                druid = 'Error opening the file for Druid Level 2 Spells'
        elif(dice >= 90 and dice < 95):
            try:
                druid = [line.strip() for line in open("/Users/pietrobongiovanni/GitHub/Dungeons-And-Dragons-Tools-Python/SingleScripts/WeaponGenerator/DatFiles/Druid/Druid3SpellList.txt", 'r')]
            except:
                druid = 'Error opening the file for Druid Level 3 Spells'
        elif(dice >= 95):
            try:
                druid = [line.strip() for line in open("/Users/pietrobongiovanni/GitHub/Dungeons-And-Dragons-Tools-Python/SingleScripts/WeaponGenerator/DatFiles/Druid/Druid4SpellList.txt", 'r')]
            except:
                druid = 'Error opening the file for Druid Level 4 Spells'
        dice = randint(0, len(druid)-1)
        spell = druid[dice]
    #PALADIN
    elif dice == 4:
        dice = randint(0, 100)
        if(dice < 50):
            try:
                paladin = [line.strip() for line in open("/Users/pietrobongiovanni/GitHub/Dungeons-And-Dragons-Tools-Python/SingleScripts/WeaponGenerator/DatFiles/Paladin/Paladin1SpellList.txt", 'r')]
            except:
                paladin = 'Error opening the file for Paladin Level 1 Spells'
        elif(dice >= 50 and dice < 80):
            try:
                paladin = [line.strip() for line in open("/Users/pietrobongiovanni/GitHub/Dungeons-And-Dragons-Tools-Python/SingleScripts/WeaponGenerator/DatFiles/Paladin/Paladin2SpellList.txt", 'r')]
            except:
                paladin = 'Error opening the file for Paladin Level 2 Spells'
        elif(dice >= 80 and dice < 95):
            try:
                paladin = [line.strip() for line in open("/Users/pietrobongiovanni/GitHub/Dungeons-And-Dragons-Tools-Python/SingleScripts/WeaponGenerator/DatFiles/Paladin/Paladin3SpellList.txt", 'r')]
            except:
                paladin = 'Error opening the file for Paladin Level 3 Spells'
        elif(dice >= 95):
            try:
                paladin = [line.strip() for line in open("/Users/pietrobongiovanni/GitHub/Dungeons-And-Dragons-Tools-Python/SingleScripts/WeaponGenerator/DatFiles/Paladin/Paladin4SpellList.txt", 'r')]
            except:
                paladin = 'Error opening the file for Paladin Level 4 Spells'
        dice = randint(0, len(paladin)-1)
        spell = paladin[dice]
    #RANGER
    elif dice == 4:
        dice = randint(0, 100)
        if(dice < 50):
            try:
                ranger = [line.strip() for line in open("/Users/pietrobongiovanni/GitHub/Dungeons-And-Dragons-Tools-Python/SingleScripts/WeaponGenerator/DatFiles/Paldin/Ranger1SpellList.txt", 'r')]
            except:
                ranger = 'Error opening the file for Ranger Level 1 Spells'
        elif(dice >= 50 and dice < 75):
            try:
                ranger = [line.strip() for line in open("/Users/pietrobongiovanni/GitHub/Dungeons-And-Dragons-Tools-Python/SingleScripts/WeaponGenerator/DatFiles/Paladin/Ranger2SpellList.txt", 'r')]
            except:
                ranger = 'Error opening the file for Ranger Level 2 Spells'
        elif(dice >= 80 and dice < 95):
            try:
                ranger = [line.strip() for line in open("/Users/pietrobongiovanni/GitHub/Dungeons-And-Dragons-Tools-Python/SingleScripts/WeaponGenerator/DatFiles/Paladin/Ranger3SpellList.txt", 'r')]
            except:
                ranger = 'Error opening the file for Ranger Level 3 Spells'
        elif(dice >= 95):
            try:
                ranger = [line.strip() for line in open("/Users/pietrobongiovanni/GitHub/Dungeons-And-Dragons-Tools-Python/SingleScripts/WeaponGenerator/DatFiles/Paladin/Ranger4SpellList.txt", 'r')]
            except:
                ranger = 'Error opening the file for Ranger Level 4 Spells'
        dice = randint(0, len(ranger)-1)
        spell = ranger[dice]
    #MAGE/WIZARD
    elif dice == 5:
        dice = randint(0,100)
        if(dice < 50):
            try:
                mage = [line.strip() for line in open("/Users/pietrobongiovanni/GitHub/Dungeons-And-Dragons-Tools-Python/SingleScripts/WeaponGenerator/DatFiles/Mage/Mage0SpellList.txt", 'r')]
            except:
                mage = 'Error opening the file for Mage/Wizard Level 0 Spells'
        elif(dice >= 50 and dice < 75):
            try:
                mage = [line.strip() for line in open("/Users/pietrobongiovanni/GitHub/Dungeons-And-Dragons-Tools-Python/SingleScripts/WeaponGenerator/DatFiles/Mage/Mage1SpellList.txt", 'r')]
            except:
                mage = 'Error opening the file for Mage/Wizard Level 1 Spells'
        elif(dice >= 75 and dice < 90):
            try:
                mage = [line.strip() for line in open("/Users/pietrobongiovanni/GitHub/Dungeons-And-Dragons-Tools-Python/SingleScripts/WeaponGenerator/DatFiles/Mage/Mage2SpellList.txt", 'r')]
            except:
                mage = 'Error opening the file for Mage/Wizard Level 2 Spells'
        elif(dice >= 90 and dice < 95):
            try:
                mage = [line.strip() for line in open("/Users/pietrobongiovanni/GitHub/Dungeons-And-Dragons-Tools-Python/SingleScripts/WeaponGenerator/DatFiles/Mage/Mage3SpellList.txt", 'r')]
            except:
                mage = 'Error opening the file for Mage/Wizard Level 3 Spells'
        elif(dice >= 95):
            try:
                mage = [line.strip() for line in open("/Users/pietrobongiovanni/GitHub/Dungeons-And-Dragons-Tools-Python/SingleScripts/WeaponGenerator/DatFiles/Mage/Mage4SpellList.txt", 'r')]
            except:
                mage = 'Error opening the file for Mage/Wizard Level 4 Spells'
        dice = randint(0, len(mage)-1)
        spell = mage[dice]
    return spell
