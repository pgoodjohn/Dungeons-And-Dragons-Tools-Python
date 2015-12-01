'''
 ___  _____     Python - Name Generator Script - v 1.0
|    |_   _|    Skeleton of the Name Generator for the D&D tools suite.
|   _  | |      This is the next change we need to do
|___|  | |      http://stackoverflow.com/questions/7165749/open-file-in-a-relative-location-in-python
      /_ /      Pietro Goodjohn Bongiovanni - November 2015
'''

#https://en.wikipedia.org/wiki/Dragonlance
#check out merkov chain to get it to improve https://en.wikipedia.org/wiki/Markov_chain

from random import randint
import sys
sys.path.insert(0, '/Users/pietrobongiovanni/GitHub/Dungeons-And-Dragons-Tools-Python/NameGenerator/')

def generate(gender, race):
    #RACE == 1 IS DWARF
    if(race == 1):
        #GENDER == 0 IS MALE
        if (gender == 0):
            #Read dwarven names from file
            names = [line.strip() for line in open("/Users/pietrobongiovanni/GitHub/Dungeons-And-Dragons-Tools-Python/NameGenerator/DwarvenMaleNames.txt", 'r')]
        #GENDER == 1 IS FEMALE
        elif (gender == 1):
            names = [line.strip() for line in open("/Users/pietrobongiovanni/GitHub/Dungeons-And-Dragons-Tools-Python/NameGenerator/DwarvenFemaleNames.txt",'r')]
        #ERROR HANDLING
        else:
            names = ['Something went wrong with gender choice']

        #Generate surnames, can be better though
        surnames = [line.strip() for line in open("/Users/pietrobongiovanni/GitHub/Dungeons-And-Dragons-Tools-Python/NameGenerator/DwarvenMaleNames.txt", 'r')]
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
            names = [line.strip() for line in open("/Users/pietrobongiovanni/GitHub/Dungeons-And-Dragons-Tools-Python/NameGenerator/ElvenMaleNames.txt", 'r')]
        #GENDER == 1 IS FEMALE
        elif (gender == 1):
            names = [line.strip() for line in open("/Users/pietrobongiovanni/GitHub/Dungeons-And-Dragons-Tools-Python/NameGenerator/ElvenFemaleNames.txt", 'r')]
        #ERROR HANDLING
        else:
            names = ['Something went wrong with gender choice']
        surnames = [line.strip() for line in open("/Users/pietrobongiovanni/GitHub/Dungeons-And-Dragons-Tools-Python/NameGenerator/ElvenSurnames.txt", 'r')]

    #RACE == 3 IS Human
    #Check this for more human names http://www.uesp.net/wiki/Lore:Orc_Names
    elif(race==3):
        #GENDER == 0 IS MALE
        if (gender == 0):
            names = [line.strip() for line in open("/Users/pietrobongiovanni/GitHub/Dungeons-And-Dragons-Tools-Python/NameGenerator/HumanMaleNames.txt", 'r')]
        #GENDER == 1 IS FEMALE
        elif (gender == 1):
            names = [line.strip() for line in open("/Users/pietrobongiovanni/GitHub/Dungeons-And-Dragons-Tools-Python/NameGenerator/HumanFemaleNames.txt", 'r')]
        #ERROR HANDLING
        else:
            names = ['Something went wrong with gender choice']
        surnames = [line.strip() for line in open("/Users/pietrobongiovanni/GitHub/Dungeons-And-Dragons-Tools-Python/NameGenerator/HumanSurnames.txt", 'r')]

    #RACE == 4 IS Gnome
    elif(race==4):
        #GENDER == 0 IS MALE
        if (gender == 0):
            names = [line.strip() for line in open("/Users/pietrobongiovanni/GitHub/Dungeons-And-Dragons-Tools-Python/NameGenerator/GnomeMaleNames.txt", 'r')]
        #GENDER == 1 IS FEMALE
        elif (gender == 1):
            names = [line.strip() for line in open("/Users/pietrobongiovanni/GitHub/Dungeons-And-Dragons-Tools-Python/NameGenerator/GnomeFemaleNames.txt", 'r')]
        #ERROR HANDLING
        else:
            names = ['Something went wrong with gender choice']
        surnames = [line.strip() for line in open("/Users/pietrobongiovanni/GitHub/Dungeons-And-Dragons-Tools-Python/NameGenerator/GnomeSurnames.txt", 'r')]

    #RACE == 5 IS Half Elf
    elif(race==5):
        #GENDER == 0 IS MALE
        if (gender == 0):
            names = [line.strip() for line in open("/Users/pietrobongiovanni/GitHub/Dungeons-And-Dragons-Tools-Python/NameGenerator/HalfElvenMaleNames.txt", 'r')]
        #GENDER == 1 IS FEMALE
        elif (gender == 1):
            names = [line.strip() for line in open("/Users/pietrobongiovanni/GitHub/Dungeons-And-Dragons-Tools-Python/NameGenerator/HalfElvenFemaleNames.txt", 'r')]
        #ERROR HANDLING
        else:
            names = ['Something went wrong with gender choice']
        surnames = [line.strip() for line in open("/Users/pietrobongiovanni/GitHub/Dungeons-And-Dragons-Tools-Python/NameGenerator/HalfElvenSurnames.txt", 'r')]

    #RACE == 6 IS Half Orc
    #File is already massive, find more at http://www.uesp.net/wiki/Lore:Orc_Names
    elif(race==6):
        #GENDER == 0 IS MALE
        if (gender == 0):
            names = [line.strip() for line in open("/Users/pietrobongiovanni/GitHub/Dungeons-And-Dragons-Tools-Python/NameGenerator/OrkishMaleNames.txt", 'r')]
        #GENDER == 1 IS FEMALE
        elif (gender == 1):
            names = [line.strip() for line in open("/Users/pietrobongiovanni/GitHub/Dungeons-And-Dragons-Tools-Python/NameGenerator/OrkishFemaleNames.txt", 'r')]
        #ERROR HANDLING
        else:
            names = ['Something went wrong with gender choice']
        surnames = [line.strip() for line in open("/Users/pietrobongiovanni/GitHub/Dungeons-And-Dragons-Tools-Python/NameGenerator/OrkishSurnames.txt", 'r')]

    #RACE == 7 IS Halfling
    #Halflings have also prefixes and suffixes so... check this out http://www.angelfire.com/rpg/annwn/nameshalf.html
    elif(race==7):
        #GENDER == 0 IS MALE
        if (gender == 0):
            names = [line.strip() for line in open("/Users/pietrobongiovanni/GitHub/Dungeons-And-Dragons-Tools-Python/NameGenerator/HalflingMaleNames.txt", 'r')]
        #GENDER == 1 IS FEMALE
        elif (gender == 1):
            names = [line.strip() for line in open("/Users/pietrobongiovanni/GitHub/Dungeons-And-Dragons-Tools-Python/NameGenerator/HalflingFemaleNames.txt", 'r')]
        #ERROR HANDLING
        else:
            names = ['Something went wrong with gender choice']
        surnames = [line.strip() for line in open("/Users/pietrobongiovanni/GitHub/Dungeons-And-Dragons-Tools-Python/NameGenerator/HalflingSurnames.txt", 'r')]


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
