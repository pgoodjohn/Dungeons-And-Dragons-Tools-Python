'''
 ___  _____     Python - Name Generator Script - v 1.0
|    |_   _|    Skeleton of the Name Generator for the D&D tools suite.
|   _  | |      This is the next change we need to do
|___|  | |
      /_ /      Pietro Goodjohn Bongiovanni - November 2015
'''

#https://en.wikipedia.org/wiki/Dragonlance

from random import randint
import random
from collections import defaultdict
import os.path
directory,filename = os.path.split(__file__)
import sys
sys.path.append(directory)

space = ' '
chain = defaultdict(list)

def markov(list):
    for name in list:
        strippedName = name.lower().strip()
        pairs = zip(strippedName, strippedName[1:])
        for first, second in pairs:
          chain[first].append(second)
          chain[strippedName[-1]].append(space)
          chain[space].append(strippedName[0])
def generate_surname():
    name = []
    current = space
    while not (current == space and name):
        current = random.choice(chain[current])
        name.append(current)
    return ''.join(name).strip().capitalize()


def generate(gender, race):
    #RACE == 1 IS DWARF
    if(race == 1):
        #GENDER == 0 IS MALE
        if (gender == 0):
            #Read dwarven names from file
            names = [line.strip() for line in open(''.join((directory,"/DwarvenMaleNames.dat")), 'r')]
        #GENDER == 1 IS FEMALE
        elif (gender == 1):
            names = [line.strip() for line in open(''.join((directory,"/DwarvenFemaleNames.dat")),'r')]
        #ERROR HANDLING
        else:
            names = ['Something went wrong with gender choice']
        #Generate surnames, can be better though
        surnames = [line.strip() for line in open(''.join((directory,"/DwarvenMaleNames.dat")), 'r')]
        j = 0
        while(j<(len(surnames)-1)):
            i = randint(0, 1)
            if (i == 0):
                surnames[j] = surnames[j] + 'sson'
            else:
                surnames[j] = surnames[j] + 'gloit'
            j += 1
        dice = randint(0, len(surnames)-1)
        surname = surnames[dice]

    #RACE == 2 IS ELF
    elif(race==2):
        #GENDER == 0 IS MALE
        if (gender == 0):
            names = [line.strip() for line in open(''.join((directory,"/ElvenMaleNames.dat")), 'r')]
        #GENDER == 1 IS FEMALE
        elif (gender == 1):
            names = [line.strip() for line in open(''.join((directory,"/ElvenFemaleNames.dat")), 'r')]
        #ERROR HANDLING
        else:
            names = ['Something went wrong with gender choice']
        markov(names)
        generate_surname()
        surname = ''
        while len(surname) < 4:
            surname = generate_surname()

    #RACE == 3 IS Human
    #Check this for more human names http://www.uesp.net/wiki/Lore:Orc_Names
    elif(race==3):
        #GENDER == 0 IS MALE
        if (gender == 0):
            names = [line.strip() for line in open(''.join((directory,"/HumanMaleNames.dat")), 'r')]
        #GENDER == 1 IS FEMALE
        elif (gender == 1):
            names = [line.strip() for line in open(''.join((directory,"/HumanFemaleNames.dat")), 'r')]
        #ERROR HANDLING
        else:
            names = ['Something went wrong with gender choice']
        markov(names)
        generate_surname()
        surname = ''
        while len(surname) < 4:
            surname = generate_surname()

    #RACE == 4 IS Gnome
    elif(race==4):
        #GENDER == 0 IS MALE
        if (gender == 0):
            names = [line.strip() for line in open(''.join((directory,"/GnomeMaleNames.dat")), 'r')]
        #GENDER == 1 IS FEMALE
        elif (gender == 1):
            names = [line.strip() for line in open(''.join((directory,"/GnomeFemaleNames.dat")), 'r')]
        #ERROR HANDLING
        else:
            names = ['Something went wrong with gender choice']
        markov(names)
        generate_surname()
        surname = ''
        while len(surname) < 4:
            surname = generate_surname()

    #RACE == 5 IS Half Elf
    elif(race==5):
        #GENDER == 0 IS MALE
        if (gender == 0):
            names = [line.strip() for line in open(''.join((directory,"./HalfElvenMaleNames.dat")), 'r')]
        #GENDER == 1 IS FEMALE
        elif (gender == 1):
            names = [line.strip() for line in open(''.join((directory,"./HalfElvenFemaleNames.dat")), 'r')]
        #ERROR HANDLING
        else:
            names = ['Something went wrong with gender choice']
        markov(names)
        generate_surname()
        surname = ''
        while len(surname) < 4:
            surname = generate_surname()

    #RACE == 6 IS Half Orc
    #File is already massive, find more at http://www.uesp.net/wiki/Lore:Orc_Names
    elif(race==6):
        #GENDER == 0 IS MALE
        if (gender == 0):
            names = [line.strip() for line in open(''.join((directory,"./OrkishMaleNames.dat")), 'r')]
        #GENDER == 1 IS FEMALE
        elif (gender == 1):
            names = [line.strip() for line in open(''.join((directory,"./OrkishFemaleNames.dat")), 'r')]
        #ERROR HANDLING
        else:
            names = ['Something went wrong with gender choice']
        markov(names)
        generate_surname()
        surname = ''
        while len(surname) < 4:
            surname = generate_surname()

    #RACE == 7 IS Halfling
    #Halflings have also prefixes and suffixes so... check this out http://www.angelfire.com/rpg/annwn/nameshalf.html
    elif(race==7):
        #GENDER == 0 IS MALE
        if (gender == 0):
            names = [line.strip() for line in open(''.join((directory,"/HalflingMaleNames.dat")), 'r')]
        #GENDER == 1 IS FEMALE
        elif (gender == 1):
            names = [line.strip() for line in open(''.join((directory,"/HalflingFemaleNames.dat")), 'r')]
        #ERROR HANDLING
        else:
            names = ['Something went wrong with gender choice']
        markov(names)
        generate_surname()
        surname = ''
        while len(surname) < 4:
            surname = generate_surname()


    #ERROR HANDLING
    else:
        names = ['Something went wrong with chosing name']
        surnames = ['Something went wrong with chosing surname']

    #RANDOMIZING NAMES AND SAVING THEM
    rand1 = randint(0, (len(names)-1))
    #rand2 = randint(0, (len(surnames)-1))
    string = names[rand1] + ' ' + surname
    return string
