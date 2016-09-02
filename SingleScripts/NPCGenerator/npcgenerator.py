'''
 ___  _____     Python - NPC Generator - v 1.0
|    |_   _|
|   _  | |
|___|  | |
      /_ /      Pietro Goodjohn Bongiovanni - December 2015
'''

from random import randint
import sys
import os.path
directory,filename = os.path.split(__file__)
sys.path.insert(0, directory)
import NameGenerator

#https://www.reddit.com/r/DnDBehindTheScreen/comments/3py5dm/random_tables_superquick_town_npcs/

def generateNPC(n):
    if (n == 0):
        #0 is a warrior NPC
        NPCclass = generateCLASS()
    elif (n==1):
        npc = generateCITIZEN()
    NPCrace = generateRACE()
    NPCgender = generateGENDER()
    NPCcharachteristics = generateCHAR()
    if (n == 0):
        npc = NameGenerator.generate(GENDERFlag, RACEflag)
        npc = npc + ' ' + '(' + NPCgender + ') ' + NPCrace + ' ' + NPCclass + ' '
        npc = npc + NPCcharachteristics
        return npc
    else:
        return npc

def generateRACE():
    '''
    Dwarf / Elf / Human / Gnome / Half-Elf / Half-Orc / Halfling
    '''
    global RACEflag
    i = randint(1,7)
    if i == 1:
        NPCrace = 'Dwarf'
        RACEflag = 1
    elif i == 2:
        NPCrace = 'Elf'
        RACEflag = 2
    elif i == 3:
        NPCrace = 'Human'
        RACEflag = 3
    elif i == 4:
        NPCrace = 'Gnome'
        RACEflag = 4
    elif i == 5:
        NPCrace = 'Half-Elf'
        RACEflag = 5
    elif i == 6:
        NPCrace = 'Half-Orc'
        RACEflag = 6
    elif i == 7:
        NPCrace = 'Halfling'
        RACEflag = 7
    else:
        NPCrace = 'error'
    return NPCrace

def generateCLASS():
    '''
    Barbarian / Bard / Cleric / Druid /Warrior / Thief / Mage / Monk / Paladin / Ranger / Wizard
    '''
    i = randint(0,10)
    if i == 0:
        NPCclass = 'Barbarian'
    elif i == 1:
        NPCclass = 'Bard'
    elif i == 2:
        NPCclass = 'Cleric'
    elif i == 3:
        NPCclass = 'Druid'
    elif i == 4:
        NPCclass = 'Warrior'
    elif i == 5:
        NPCclass = 'Thief'
    elif i == 6:
        NPCclass = 'Mage'
    elif i == 7:
        NPCclass = 'Monk'
    elif i == 8:
        NPCclass = 'Paladin'
    elif i == 9:
        NPCclass = 'Ranger'
    elif i == 10:
        NPCclass = 'Wizard'
    else:
        NPCclass = 'error'
    return NPCclass

def generateGENDER():
    gender = randint(0, 1)
    global GENDERFlag
    if gender == 0:
        gender = 'Male'
        GENDERFlag = 0
    elif gender == 1:
        gender = 'Female'
        GENDERFlag = 1
    else:
        'error'
    return gender

def generateCHAR():
    #CHECK OUT JUSTISAURU'S METHODS https://sites.google.com/site/justisaursdd/tar-pit-dugout/justisaurs27-25-23abilityscoregeneration
    dice = 0
    flag = 0
    STR = 0
    DEX = 0
    COS = 0
    INT = 0
    WIS = 0
    CAR = 0
    #DWARF = 1 ELF = 2 HUMAN = 3 GNOME = 4 HALF ELF = 5 HALF ORC = 6 HALFLING = 7
    #STR generation
    for dice in range(0, 3):
        diceroll = randint(1, 6)
        if diceroll == 1 and flag == 0:
            diceroll = randint(1, 6)
            STR = STR + diceroll
            flag == 1
        else:
            STR = STR + diceroll
        #Race modificator (+Half orc(6), -Halfling(7), -Gnome(4))
        if RACEflag == 6:
            STR = STR + 2
        elif RACEflag == 7 or RACEflag == 4:
            STR = STR - 2
        else:
            pass

    #DEX generation
    for dice in range(0, 3):
        diceroll = randint(1, 6)
        if diceroll == 1 and flag == 0:
            diceroll = randint(1, 6)
            DEX = DEX + diceroll
            flag == 1
        else:
            DEX = DEX + diceroll
        #Race modificator (+Elf(2), +Halfling(7))
        if RACEflag == 2 or RACEflag == 7:
            DEX = DEX + 2
        else:
            pass

    #COS generation
    for dice in range(0, 3):
        diceroll = randint(1, 6)
        if diceroll == 1 and flag == 0:
            diceroll = randint(1, 6)
            COS = COS + diceroll
            flag == 1
        else:
            COS = COS + diceroll
        #Race modificator (+Dwarf(1), +Gnome(4), -Elf(2))
        if RACEflag == 1 or RACEflag == 4:
            COS = COS + 2
        elif RACEflag == 2:
            COS = COS - 2
        else:
            pass

    #INT generation
    for dice in range(0, 3):
        diceroll = randint(1, 6)
        if diceroll == 1 and flag == 0:
            diceroll = randint(1, 6)
            INT = INT + diceroll
            flag == 1
        else:
            INT = INT + diceroll
        #Race modificator (-Half Orc(6))
        if RACEflag == 6:
            INT = INT - 2
        else:
            pass

    #WIS generator
    for dice in range(0, 3):
        diceroll = randint(1, 6)
        if diceroll == 1 and flag == 0:
            diceroll = randint(1, 6)
            WIS = WIS + diceroll
            flag == 1
        else:
            WIS = WIS + diceroll
        #Race modificator (NULL)

    #CAR generator
    for dice in range(0, 3):
        diceroll = randint(1, 6)
        if diceroll == 1 and flag == 0:
            diceroll = randint(1, 6)
            CAR = CAR + diceroll
            flag == 1
        else:
            CAR = CAR + diceroll
        #Race modificator(-Dwarf(1), -Half-Orc(6))
        if RACEflag == 1 or RACEflag == 6:
            CAR = CAR - 2
        else:
            pass

    charachteristcs = 'Str = %d, Dex = %d, Cos = %d, Int = %d, Wis = %d, Char = %d' % (STR, DEX, COS, INT, WIS, CAR)
    return charachteristcs

def generateCITIZEN():
    NPCrace = generateRACE()
    NPCgender = generateGENDER()
    citizen = NameGenerator.generate(GENDERFlag, RACEflag)
    #Decide what is the profession of the citizen.
    dice = randint(1,10);
    #dice = 3 #this one is just for debugging
    #ALCHEMIST
    if (dice == 1):
        dice = randint(1,6)
        if (dice == 1):
            NPCprofession = 'an Alchemist, more specifically an apothecary'
        elif (dice == 2):
            NPCprofession = 'an alchemist, more specifically a hedge wizard'
        elif (dice == 3):
            NPCprofession = 'an alchemist, more specifically an herbalist'
        elif (dice == 4):
            NPCprofession = 'an alchemist, more specifically a poisonmaker'
        elif (dice == 5):
            NPCprofession = 'an alchemist, more specifically a potioneer'
        elif (dice == 6):
            NPCprofession = 'an alchemist, more specifically a pyromancer'
        else:
            NPCprofession = 'error in single prof'
        if NPCgender == 'Male':
            NPCprofession = NPCprofession + ', and he'
        elif NPCgender == 'Female':
            NPCprofession = NPCprofession + ', and she'
        else:
            NPCprofession = 'error with the gender'
        dice = randint(1,4)
        if (dice == 1):
            NPCprofession = NPCprofession + ' is looking for delivery help '
        elif (dice == 2):
            NPCprofession = NPCprofession + ' is looking for new recipes '
        elif (dice == 3):
            NPCprofession = NPCprofession + ' is looking for purchasers '
        elif (dice == 4):
            NPCprofession = NPCprofession + ' is looking for rare ingredients '
        else:
            NPCprofession = 'error with the lookings'
        dice = randint(1,4)
        if (dice == 1):
            NPCprofession = NPCprofession + 'and carries several vials of acids.'
        elif (dice == 2):
            NPCprofession = NPCprofession + 'and carries several curatives.'
        elif (dice == 3):
            NPCprofession = NPCprofession + 'and carries an unusual potion.'
        elif (dice == 4):
            NPCprofession = NPCprofession + 'and carries a pyrophoric substance.'
        else:
            NPCprofession = 'error with the carries'

    #BANDIT
    elif (dice == 2):
        dice = randint(1,6)
        if (dice == 1):
            NPCprofession = 'a bandit, more specifically an assassin'
        elif (dice == 2):
            NPCprofession = 'a bandit, more specifically a confidence artist'
        elif (dice == 3):
            NPCprofession = 'a bandit, more specifically a gambler'
        elif (dice == 4):
            NPCprofession = 'a bandit, more specifically a poacher'
        elif (dice == 5):
            NPCprofession = 'a bandit, more specifically a smuggler'
        elif (dice == 6):
            NPCprofession = 'a bandit, more specifically a thief'
        else:
            NPCprofession = 'error in single prof'
        if NPCgender == 'Male':
            NPCprofession = NPCprofession + ', and he'
        elif NPCgender == 'Female':
            NPCprofession = NPCprofession + ', and she'
        else:
            NPCprofession = 'error with the gender'
        dice = randint(1,6)
        if (dice == 1):
            NPCprofession = NPCprofession + ' is looking for accomplices for a specific task'
        elif (dice == 2):
            NPCprofession = NPCprofession + ' is looking for revenge against a rival criminal'
        elif (dice == 3):
            NPCprofession = NPCprofession + ' is looking for an easy mark'
        elif (dice == 4):
            NPCprofession = NPCprofession + ' is looking for extra muscle for some work'
        elif (dice == 5):
            NPCprofession = NPCprofession + ' is looking for rumors that may lead to a big score'
        elif (dice == 6):
            NPCprofession = NPCprofession + ' is looking for a owdy evening of carousing'
        else:
            NPCprofession = 'error with the lookings'
        dice = randint(1,6)
        if (dice == 1):
            NPCprofession = NPCprofession + ' and carries a crossbow with poisoned darts.'
        elif (dice == 2):
            NPCprofession = NPCprofession + ' and carries several daggers.'
        elif (dice == 3):
            NPCprofession = NPCprofession + ' and carries a short sword.'
        elif (dice == 4):
            NPCprofession = NPCprofession + ' and carries a lucky charm.'
        elif (dice == 5):
            NPCprofession = NPCprofession + ' and carries the token of a love.'
        elif (dice == 6):
            NPCprofession = NPCprofession + ' and carries letters for blackmail.'
        else:
            NPCprofession = 'error with the carries'

    #LAW OFFICIAL
    elif (dice == 3):
        dice = randint(1,4)
        if (dice == 1):
            NPCprofession = 'a law official, more specifically a constable'
        elif (dice == 2):
            NPCprofession = 'a law official, more specifically a sheriff'
        elif (dice == 3):
            NPCprofession = 'a law official, more specifically a guard captain'
        elif (dice == 4):
            NPCprofession = 'a law official, more specifically a magistrate'
        else:
            NPCprofession = 'error in single prof'
        if NPCgender == 'Male':
            NPCprofession = NPCprofession + ', and he'
        elif NPCgender == 'Female':
            NPCprofession = NPCprofession + ', and she'
        else:
            NPCprofession = 'error with the gender'
        dice = randint(1,6)
        if (dice == 1):
            NPCprofession = NPCprofession + ' is seeking someone to capture a fugitive'
        elif (dice == 2):
            NPCprofession = NPCprofession + ' is seeking someone to catch a thief'
        elif (dice == 3):
            NPCprofession = NPCprofession + ' is seeking someone to guard a specific location or person'
        elif (dice == 4):
            NPCprofession = NPCprofession + ' is seeking someone to investigate a disappearance'
        elif (dice == 5):
            NPCprofession = NPCprofession + ' is seeking someone to solve a murder mystery'
        elif (dice == 6):
            NPCprofession = NPCprofession + ' is seeking someone to have an ale with'
        else:
            NPCprofession = 'error with the lookings'
        dice = randint(1,4)
        if (dice == 1):
            NPCprofession = NPCprofession + ' and carries an arrest warrant for an outlaw.'
        elif (dice == 2):
            NPCprofession = NPCprofession + ' and carries a proclamation for a reward.'
        elif (dice == 3):
            NPCprofession = NPCprofession + ' and carries a knife or sword of the office.'
        elif (dice == 4):
            NPCprofession = NPCprofession + ' and carries a pocketbook of local laws.'
        else:
            NPCprofession = 'error with the carries'

    #NOBLE
    elif (dice == 4):
        dice = randint(1,6)
        if (dice == 1):
            NPCprofession = 'a noble, more specifically a kinght'
        elif (dice == 2):
            NPCprofession = 'a noble, more specifically an old lord'
        elif (dice == 3):
            NPCprofession = 'a noble, more specifically a young lord'
        elif (dice == 4):
            NPCprofession = 'a noble, more specifically an old lady'
        elif (dice == 5):
            NPCprofession = 'a noble, more specifically a young lady'
        elif (dice == 6):
            NPCprofession = 'a noble, more specifically a wealthy merchant'
        else:
            NPCprofession = 'error in single prof'
        if NPCgender == 'Male':
            NPCprofession = NPCprofession + ', and he'
        elif NPCgender == 'Female':
            NPCprofession = NPCprofession + ', and she'
        else:
            NPCprofession = 'error with the gender'
        dice = randint(1,6)
        if (dice == 1):
            NPCprofession = NPCprofession + ' is looking for someone to dispose of an enemy'
        elif (dice == 2):
            NPCprofession = NPCprofession + ' is looking for someone to negotiate a trade contract'
        elif (dice == 3):
            NPCprofession = NPCprofession + ' is looking for someone to prepare an army for war'
        elif (dice == 4):
            NPCprofession = NPCprofession + ' is looking for someone to sabotage a rival'
        elif (dice == 5):
            NPCprofession = NPCprofession + ' is looking for someone to secure marriage'
        elif (dice == 6):
            NPCprofession = NPCprofession + ' is looking for someone to have a good time with'
        else:
            NPCprofession = 'error with the lookings'
        dice = randint(1,6)
        if (dice == 1):
            NPCprofession = NPCprofession + ' and carries several deeds and titles.'
        elif (dice == 2):
            NPCprofession = NPCprofession + ' and carries a family heirloom.'
        elif (dice == 3):
            NPCprofession = NPCprofession + ' and carries several inventories and invoices.'
        elif (dice == 4):
            NPCprofession = NPCprofession + ' and carries a some very valuable jewels.'
        elif (dice == 5):
            NPCprofession = NPCprofession + ' and carries a compromising love letter.'
        elif (dice == 6):
            NPCprofession = NPCprofession + ' and carries a letter from a powerful lord or lady.'
        else:
            NPCprofession = 'error with the carries'

    #PRIEST
    elif (dice == 5):
        dice = randint(1,6)
        if (dice == 1):
            NPCprofession = 'a priest, more specifically an acolyte'
        elif (dice == 2):
            NPCprofession = 'a priest, more specifically a healer'
        elif (dice == 3):
            NPCprofession = 'a priest, more specifically a monk'
        elif (dice == 4):
            NPCprofession = 'a priest, more specifically a preacher'
        elif (dice == 5):
            NPCprofession = 'a priest, more specifically a scholar'
        elif (dice == 6):
            NPCprofession = 'a priest, more specifically a witch-hunter'
        else:
            NPCprofession = 'error in single prof'
        if NPCgender == 'Male':
            NPCprofession = NPCprofession + ', and he'
        elif NPCgender == 'Female':
            NPCprofession = NPCprofession + ', and she'
        else:
            NPCprofession = 'error with the gender'
        dice = randint(1,4)
        if (dice == 1):
            NPCprofession = NPCprofession + ' is looking for new coverts'
        elif (dice == 2):
            NPCprofession = NPCprofession + ' is looking for heretics'
        elif (dice == 3):
            NPCprofession = NPCprofession + ' is looking for an relics and rare lore'
        elif (dice == 4):
            NPCprofession = NPCprofession + ' is looking for the bottom of a goblet'
        else:
            NPCprofession = 'error with the lookings'
        dice = randint(1,4)
        if (dice == 1):
            NPCprofession = NPCprofession + ' and carries a well-used cudgel.'
        elif (dice == 2):
            NPCprofession = NPCprofession + ' and carries a prominently displayed holy symbol.'
        elif (dice == 3):
            NPCprofession = NPCprofession + ' and carries a pocketbook of sacred texts.'
        elif (dice == 4):
            NPCprofession = NPCprofession + ' and carries a wineskin.'
        else:
            NPCprofession = 'error with the carries'

    #SEER
    elif (dice == 6):
        dice = randint(1,6)
        if (dice == 1):
            NPCprofession = 'a seer, more specifically an astrologer'
        elif (dice == 2):
            NPCprofession = 'a seer, more specifically a fortune teller'
        elif (dice == 3):
            NPCprofession = 'a seer, more specifically a mystic'
        elif (dice == 4):
            NPCprofession = 'a seer, more specifically a lorekeeper'
        elif (dice == 5):
            NPCprofession = 'a seer, more specifically a prophet'
        elif (dice == 6):
            NPCprofession = 'a seer, more specifically a psychic'
        else:
            NPCprofession = 'error in single prof'
        if NPCgender == 'Male':
            NPCprofession = NPCprofession + ', and he'
        elif NPCgender == 'Female':
            NPCprofession = NPCprofession + ', and she'
        else:
            NPCprofession = 'error with the gender'
        dice = randint(1,4)
        if (dice == 1):
            NPCprofession = NPCprofession + ' is looking for new clients for reading'
        elif (dice == 2):
            NPCprofession = NPCprofession + ' is looking for the answer to a riddle or prophecy'
        elif (dice == 3):
            NPCprofession = NPCprofession + ' is looking for an relics and news regarding a missing person'
        elif (dice == 4):
            NPCprofession = NPCprofession + ' is looking for some juicy gossip'
        else:
            NPCprofession = 'error with the lookings'
        dice = randint(1,4)
        if (dice == 1):
            NPCprofession = NPCprofession + ' and carries a crystall ball.'
        elif (dice == 2):
            NPCprofession = NPCprofession + ' and carries a dowsing rod.'
        elif (dice == 3):
            NPCprofession = NPCprofession + ' and carries a large, sharp-pointed knife.'
        elif (dice == 4):
            NPCprofession = NPCprofession + ' and carries several star charts.'
        else:
            NPCprofession = 'error with the carries'

    #SMITH
    elif (dice == 7):
        dice = randint(1,4)
        if (dice == 1):
            NPCprofession = 'a smith, more specifically an armorer'
        elif (dice == 2):
            NPCprofession = 'a smith, more specifically a blacksmith'
        elif (dice == 3):
            NPCprofession = 'a smith, more specifically a farrier'
        elif (dice == 4):
            NPCprofession = 'a smith, more specifically a weaponsmith'
        else:
            NPCprofession = 'error in single prof'
        if NPCgender == 'Male':
            NPCprofession = NPCprofession + ', and he'
        elif NPCgender == 'Female':
            NPCprofession = NPCprofession + ', and she'
        else:
            NPCprofession = 'error with the gender'
        dice = randint(1,4)
        if (dice == 1):
            NPCprofession = NPCprofession + ' is looking for a new apprentice'
        elif (dice == 2):
            NPCprofession = NPCprofession + ' is looking for a journeyman craftsman'
        elif (dice == 3):
            NPCprofession = NPCprofession + ' is looking for rare metals'
        elif (dice == 4):
            NPCprofession = NPCprofession + ' is looking for a mug of strong ale'
        else:
            NPCprofession = 'error with the lookings'
        dice = randint(1,4)
        if (dice == 1):
            NPCprofession = NPCprofession + ' and carries a hammer.'
        elif (dice == 2):
            NPCprofession = NPCprofession + ' and carries a metal trinket made by the smith.'
        elif (dice == 3):
            NPCprofession = NPCprofession + ' and carries a contract commisioning a weapon.' #might insert the weapon randomizer... but maybe not because too much coding
        elif (dice == 4):
            NPCprofession = NPCprofession + ' and carries little more than a few coins.'
        else:
            NPCprofession = 'error with the carries'

    #TRAVELER
    elif (dice == 8):
        dice = randint(1,8)
        if (dice == 1):
            NPCprofession = 'a traveler, more specifically an exile'
        elif (dice == 2):
            NPCprofession = 'a traveler, more specifically a ministrel'
        elif (dice == 3):
            NPCprofession = 'a traveler, more specifically a peddler'
        elif (dice == 4):
            NPCprofession = 'a traveler, more specifically a pilgrim'
        elif (dice == 5):
            NPCprofession = 'a traveler, more specifically a refugee'
        elif (dice == 6):
            NPCprofession = 'a traveler, more specifically a sellsword'
        elif (dice == 7):
            NPCprofession = 'a traveler, more specifically a storyteller'
        elif (dice == 8):
            NPCprofession = 'a traveler, more specifically a treasure hunter'
        else:
            NPCprofession = 'error in single prof'
        if NPCgender == 'Male':
            NPCprofession = NPCprofession + ', and he'
        elif NPCgender == 'Female':
            NPCprofession = NPCprofession + ', and she'
        else:
            NPCprofession = 'error with the gender'
        dice = randint(1,10)
        if (dice == 1):
            NPCprofession = NPCprofession + ' is looking for accomplices on a quest.'
        elif (dice == 2):
            NPCprofession = NPCprofession + ' is looking for the answer to a riddle.'
        elif (dice == 3):
            NPCprofession = NPCprofession + ' is looking for an audience to entertain.'
        elif (dice == 4):
            NPCprofession = NPCprofession + ' is looking for a long lost friend'
        elif (dice == 5):
            NPCprofession = NPCprofession + ' is looking for the return of something stolen.'
        elif (dice == 6):
            NPCprofession = NPCprofession + ' is looking for revenge against a bitter rival.'
        elif (dice == 7):
            NPCprofession = NPCprofession + ' is looking for a permanent home.'
        elif (dice == 8):
            NPCprofession = NPCprofession + ' is looking for steady work.'
        elif (dice == 9):
            NPCprofession = NPCprofession + ' is looking for traveling companions.'
        elif (dice == 10):
            NPCprofession = NPCprofession + ' is looking for drinking companions.'
        else:
            NPCprofession = 'error with the lookings'

    #BARMAN
    elif (dice == 9):
        if (NPCgender == 'Male'):
            NPCprofession = 'a Barman, and he'
        elif (NPCgender == 'Female'):
            NPCprofession = ' Barmaid, and she'
        else:
            NPCprofession = 'error with gender at stage 1'
        dice = randint(1,8)
        if (dice == 1):
            NPCprofession = NPCprofession + ' greets you with a mug of ale'
        elif (dice == 2):
            NPCprofession = NPCprofession + ' greets you with a goblet of wine'
        elif (dice == 3):
            NPCprofession = NPCprofession + ' greets you with a glass of water'
        elif (dice == 4):
            NPCprofession = NPCprofession + ' greets you with an offer to move to a better table'
        elif (dice == 5):
            NPCprofession = NPCprofession + ' greets you with a look of exasperation'
        elif (dice == 6):
            NPCprofession = NPCprofession + ' greets you with a warm handshake'
        elif (dice == 7):
            NPCprofession = NPCprofession + ' greets you with a pat on the back'
        elif (dice == 8):
            NPCprofession = NPCprofession + ' greets you with a pretty smile'
        else:
            NPCprofession = 'error with the greetings'
        if NPCgender == 'Male':
            NPCprofession = NPCprofession + ', and he'
        elif NPCgender == 'Female':
            NPCprofession = NPCprofession + ', and she'
        else:
            NPCprofession = 'error with the gender'
        dice = randint(1,6)
        if (dice == 1):
            NPCprofession = NPCprofession + ' is looking for an excuse to kick you out'
        elif (dice == 2):
            NPCprofession = NPCprofession + ' is looking for somoeone more important to talk to'
        elif (dice == 3):
            NPCprofession = NPCprofession + ' is looking for someone to do some pest removal'
        elif (dice == 4):
            NPCprofession = NPCprofession + ' is looking for a big tip'
        elif (dice == 5):
            NPCprofession = NPCprofession + ' is looking for a good joke or story'
        elif (dice == 6):
            NPCprofession = NPCprofession + ' is looking for the bottom of a bottle'
        else:
            NPCprofession = 'error with the lookings'
        dice = randint(1,4)
        if (dice == 1):
            NPCprofession = NPCprofession + ' and carries a filthy rag.'
        elif (dice == 2):
            NPCprofession = NPCprofession + ' and carries a pristine silk handkerchief.'
        elif (dice == 3):
            NPCprofession = NPCprofession + ' and carries a piece of cospicuous jewelry.'
        elif (dice == 4):
            NPCprofession = NPCprofession + ' and carries an unusual belt purse.'
        else:
            NPCprofession = 'error with the carries'

    #PAESANT
    elif (dice == 10):
        dice = randint(1,8)
        if (dice == 1):
            NPCprofession = 'an old farmer'
        elif (dice == 2):
            NPCprofession = 'a middle-aged farmer'
        elif (dice == 3):
            NPCprofession = 'a young farmer'
        elif (dice == 4):
            NPCprofession = 'a farm kid'
        elif (dice == 5):
            if NPCgender == 'Female':
                NPCprofession = 'an old farmwife'
            elif NPCgender == 'Male':
                NPCprofession = 'an old farm-man'
        elif (dice == 6):
            if NPCgender == 'Female':
                NPCprofession = 'a tough farmwife'
            elif NPCgender == 'Male':
                NPCprofession = 'a tough farm-man'
        elif (dice == 7):
            if NPCgender == 'Female':
                NPCprofession = 'a young maid'
            elif NPCgender == 'Male':
                NPCprofession = 'a young maidman'
        elif (dice == 8):
            if NPCgender == 'Female':
                NPCprofession = 'a country girl'
            elif NPCgender == 'Male':
                NPCprofession = 'a country boy'
        else:
            NPCprofession = 'error in single prof'
        if NPCgender == 'Male':
            NPCprofession = NPCprofession + ', and he'
        elif NPCgender == 'Female':
            NPCprofession = NPCprofession + ', and she'
        else:
            NPCprofession = 'error with the gender'
        dice = randint(1,8)
        if (dice == 1):
            NPCprofession = NPCprofession + ' is seeking someone to lend a hand on a laborious task.'
        elif (dice == 2):
            NPCprofession = NPCprofession + ' is seeking someone to repair a tool or farming implements.'
        elif (dice == 3):
            NPCprofession = NPCprofession + ' is seeking someone to help locate a missing beast.'
        elif (dice == 4):
            NPCprofession = NPCprofession + ' is seeking someone to help locate a missing person.'
        elif (dice == 5):
            NPCprofession = NPCprofession + ' is seeking someone to hHelp secure an audience with the lord/lady.'
        elif (dice == 6):
            NPCprofession = NPCprofession + ' is seeking someone to purchase or distribute crops.'
        elif (dice == 7):
            NPCprofession = NPCprofession + ' is seeking someone to purchase some livestock.'
        elif (dice == 8):
            NPCprofession = NPCprofession + ' is seeking someone to listen to a tale of woe.'
        else:
            NPCprofession = 'error with the lookings'
    else:
        NPCprofession = 'Error with the profession'
    citizen = NameGenerator.generate(GENDERFlag, RACEflag)
    citizen = citizen + ', ' +  NPCrace + ' (' + NPCgender+ ') ' + NPCprofession
    return citizen

#print generateNPC(1)
