from random import randint
import sys
sys.path.insert(0, '/Users/pietrobongiovanni/GitHub/Dungeons-And-Dragons-Tools-Python/NameGenerator')
import NameGenerator

#STUFF TO USE!!! I LOVE IT http://neverwinter.gamepedia.com/Half-Elf#Names

def generateNPC():
    NPCrace = generateRACE()
    NPCclass = generateCLASS()
    NPCgender = generateGENDER()
    NPCcharachteristics = generateCHAR()
    npc = NameGenerator.generate(GENDERFlag, RACEflag)
    npc = npc + ' ' + '(' + NPCgender + ') ' + NPCrace + ' ' + NPCclass + ' '
    npc = npc + NPCcharachteristics
    return npc

def generateRACE():
    '''
    Dwarf
    Elf
    Human
    Gnome
    Half-Elf
    Half-Orc
    Halfling
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
    Barbarian
    Bard
    Cleric
    Druid
    Warrior
    Thief
    Mage
    Monk
    Paladin
    Ranger
    Wizard
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

#print generateNPC()
