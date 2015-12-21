'''
 ___  _____     Python - Name Generator Script - v 1.0
|    |_   _|    Skeleton of the Name Generator for the D&D tools suite.
|   _  | |      This is the next change we need to do
|___|  | |
      /_ /      Pietro Goodjohn Bongiovanni - November 2015
'''

#https://en.wikipedia.org/wiki/Dragonlance
#check out merkov chain to get it to improve https://en.wikipedia.org/wiki/Markov_chain

from random import randint

def generate(gender, race):
    #RACE == 1 IS DWARF
    if(race == 1):
        #GENDER == 0 IS MALE
        if (gender == 0):
            #Read dwarven names from file
            names = [line.strip() for line in open("/Users/pietrobongiovanni/GitHub/Dungeons-And-Dragons-Tools-Python/SingleScripts/NameGenerator/DwarvenMaleNames.dat", 'r')]
        #GENDER == 1 IS FEMALE
        elif (gender == 1):
            names = [line.strip() for line in open("/Users/pietrobongiovanni/GitHub/Dungeons-And-Dragons-Tools-Python/SingleScripts/NameGenerator/DwarvenFemaleNames.dat",'r')]
        #ERROR HANDLING
        else:
            names = ['Something went wrong with gender choice']

        #Generate surnames, can be better though
        surnames = [line.strip() for line in open("/Users/pietrobongiovanni/GitHub/Dungeons-And-Dragons-Tools-Python/SingleScripts/NameGenerator/DwarvenMaleNames.dat", 'r')]
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
            names = [line.strip() for line in open("/Users/pietrobongiovanni/GitHub/Dungeons-And-Dragons-Tools-Python/SingleScripts/NameGenerator/ElvenMaleNames.dat", 'r')]
        #GENDER == 1 IS FEMALE
        elif (gender == 1):
            names = [line.strip() for line in open("/Users/pietrobongiovanni/GitHub/Dungeons-And-Dragons-Tools-Python/SingleScripts/NameGenerator/ElvenFemaleNames.dat", 'r')]
        #ERROR HANDLING
        else:
            names = ['Something went wrong with gender choice']
        surnames = [line.strip() for line in open("/Users/pietrobongiovanni/GitHub/Dungeons-And-Dragons-Tools-Python/SingleScripts/NameGenerator/ElvenSurnames.dat", 'r')]

    #RACE == 3 IS Human
    #Check this for more human names http://www.uesp.net/wiki/Lore:Orc_Names
    elif(race==3):
        #GENDER == 0 IS MALE
        if (gender == 0):
            names = [line.strip() for line in open("/Users/pietrobongiovanni/GitHub/Dungeons-And-Dragons-Tools-Python/SingleScripts/NameGenerator/HumanMaleNames.dat", 'r')]
        #GENDER == 1 IS FEMALE
        elif (gender == 1):
            names = [line.strip() for line in open("/Users/pietrobongiovanni/GitHub/Dungeons-And-Dragons-Tools-Python/SingleScripts/NameGenerator/HumanFemaleNames.dat", 'r')]
        #ERROR HANDLING
        else:
            names = ['Something went wrong with gender choice']
        surnames = [line.strip() for line in open("/Users/pietrobongiovanni/GitHub/Dungeons-And-Dragons-Tools-Python/SingleScripts/NameGenerator/HumanSurnames.dat", 'r')]

    #RACE == 4 IS Gnome
    elif(race==4):
        #GENDER == 0 IS MALE
        if (gender == 0):
            names = [line.strip() for line in open("/Users/pietrobongiovanni/GitHub/Dungeons-And-Dragons-Tools-Python/SingleScripts/NameGenerator/GnomeMaleNames.dat", 'r')]
        #GENDER == 1 IS FEMALE
        elif (gender == 1):
            names = [line.strip() for line in open("/Users/pietrobongiovanni/GitHub/Dungeons-And-Dragons-Tools-Python/SingleScripts/NameGenerator/GnomeFemaleNames.dat", 'r')]
        #ERROR HANDLING
        else:
            names = ['Something went wrong with gender choice']
        surnames = [line.strip() for line in open("/Users/pietrobongiovanni/GitHub/Dungeons-And-Dragons-Tools-Python/SingleScripts/NameGenerator/GnomeSurnames.dat", 'r')]

    #RACE == 5 IS Half Elf
    elif(race==5):
        #GENDER == 0 IS MALE
        if (gender == 0):
            names = [line.strip() for line in open("/Users/pietrobongiovanni/GitHub/Dungeons-And-Dragons-Tools-Python/SingleScripts/NameGenerator/HalfElvenMaleNames.dat", 'r')]
        #GENDER == 1 IS FEMALE
        elif (gender == 1):
            names = [line.strip() for line in open("/Users/pietrobongiovanni/GitHub/Dungeons-And-Dragons-Tools-Python/SingleScripts/NameGenerator/HalfElvenFemaleNames.dat", 'r')]
        #ERROR HANDLING
        else:
            names = ['Something went wrong with gender choice']
        surnames = [line.strip() for line in open("/Users/pietrobongiovanni/GitHub/Dungeons-And-Dragons-Tools-Python/SingleScripts/NameGenerator/HalfElvenSurnames.dat", 'r')]

    #RACE == 6 IS Half Orc
    #File is already massive, find more at http://www.uesp.net/wiki/Lore:Orc_Names
    elif(race==6):
        #GENDER == 0 IS MALE
        if (gender == 0):
            names = [line.strip() for line in open("/Users/pietrobongiovanni/GitHub/Dungeons-And-Dragons-Tools-Python/SingleScripts/NameGenerator/OrkishMaleNames.dat", 'r')]
        #GENDER == 1 IS FEMALE
        elif (gender == 1):
            names = [line.strip() for line in open("/Users/pietrobongiovanni/GitHub/Dungeons-And-Dragons-Tools-Python/SingleScripts/NameGenerator/OrkishFemaleNames.dat", 'r')]
        #ERROR HANDLING
        else:
            names = ['Something went wrong with gender choice']
        surnames = [line.strip() for line in open("/Users/pietrobongiovanni/GitHub/Dungeons-And-Dragons-Tools-Python/SingleScripts/NameGenerator/OrkishSurnames.dat", 'r')]

    #RACE == 7 IS Halfling
    #Halflings have also prefixes and suffixes so... check this out http://www.angelfire.com/rpg/annwn/nameshalf.html
    elif(race==7):
        #GENDER == 0 IS MALE
        if (gender == 0):
            names = [line.strip() for line in open("/Users/pietrobongiovanni/GitHub/Dungeons-And-Dragons-Tools-Python/SingleScripts/NameGenerator/HalflingMaleNames.dat", 'r')]
        #GENDER == 1 IS FEMALE
        elif (gender == 1):
            names = [line.strip() for line in open("/Users/pietrobongiovanni/GitHub/Dungeons-And-Dragons-Tools-Python/SingleScripts/NameGenerator/HalflingFemaleNames.dat", 'r')]
        #ERROR HANDLING
        else:
            names = ['Something went wrong with gender choice']
        surnames = [line.strip() for line in open("/Users/pietrobongiovanni/GitHub/Dungeons-And-Dragons-Tools-Python/SingleScripts/NameGenerator/HalflingSurnames.dat", 'r')]


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
