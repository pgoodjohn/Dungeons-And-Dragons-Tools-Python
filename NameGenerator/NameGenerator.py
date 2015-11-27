'''
 ___  _____     Python - Name Generator Script - v 1.0
|    |_   _|    Skeleton of the Name Generator for the D&D tools suite.
|   _  | |      
|___|  | |
      /_ /      Pietro Goodjohn Bongiovanni - November 2015
'''

from random import randint

def generate(gender, race):
    #RACE == 1 IS DWARF
    if(race == 1):
        #GENDER == 0 IS MALE
        if (gender == 0):
            #Read dwarven names from file
            names = [line.strip() for line in open("DwarvenMaleNames.txt", 'r')]
        #GENDER == 1 IS FEMALE
        elif (gender == 1):
            names = [line.strip() for line in open("DwarvenFemaleNames.txt",'r')]
        #ERROR HANDLING
        else:
            names = ['Something went wrong with gender choice']

        #Generate surnames, can be better though
        surnames = [line.strip() for line in open("DwarvenMaleNames.txt", 'r')]
        j = 0
        while(j<(len(surnames)-1)):
            i = randint(0, 1)
            if (i == 0):
                surnames[j] = surnames[j] + 'sson'
            else:
                surnames[j] = surnames[j] + 'gloit'
            j += 1

    #RACE == 2 IS ELF
    elif(race==2):
        #GENDER == 0 IS MALE
        if (gender == 0):
            names = [line.strip() for line in open("ElvenMaleNames.txt", 'r')]
        #GENDER == 1 IS FEMALE
        elif (gender == 1):
            names = [line.strip() for line in open("ElvenFemaleNames.txt", 'r')]
        #ERROR HANDLING
        else:
            names = ['Something went wrong with gender choice']
        surnames = [line.strip() for line in open("ElvenSurnames.txt", 'r')]

    #RACE == 3 IS Human
    elif(race==3):
        #GENDER == 0 IS MALE
        if (gender == 0):
            names = [line.strip() for line in open("HumanMaleNames.txt", 'r')]
        #GENDER == 1 IS FEMALE
        elif (gender == 1):
            names = [line.strip() for line in open("HumanFemaleNames.txt", 'r')]
        #ERROR HANDLING
        else:
            names = ['Something went wrong with gender choice']
        surnames = [line.strip() for line in open("HumanSurnames.txt", 'r')]


    #ERROR HANDLING
    else:
        names = ['Something went wrong with chosing name']
        surnames = ['Something went wrong with chosing surname']

    #RANDOMIZING NAMES AND SAVING THEM
    rand1 = randint(0, (len(names)-1))
    rand2 = randint(0, (len(surnames)-1))
    string = names[rand1] + ' ' + surnames[rand2]
    return string

#print generate(1, 1)
