from random import randint

def encounter(place):
    '''
    Ok, how do i want this one to work.
    How do encounters work while playing?
    I know where players are at so i have to get that somehow, i get an variable
    and i relate ints to different places(city, forest, hills... etc).
    I should also know their level so i probably need to get also that
    From that I have to randomize the encounter
    I'll have to have different files for the places, in these files there will
    be the enemies, weaker enemies will be in more lines, stronger enemies will
    be in less lines, some lines will be empty.
    I'll take a random number and choose randomly from the enemies in the list
    who the players will face.
    I think this should in theory work.

    Will this one generate evil AND good encounters?
    Will the master be able to choose if evil or good or also that will be random?
    Uhm... Interesting.
    Maybe I'll add some spice to the encounters.

    I like how the encounters are handled in the masters manual. Probably will go
    on that same line.
    '''
    #LETS START FROM A BIG IF THAT CHECK WHERE THE PLAYERS' AT

    #PLACE == 1 --> URBAN
    if (place == 1):
        encounterArray = [line.strip() for line in open("/Users/pietrobongiovanni/GitHub/Dungeons-And-Dragons-Tools-Python/SingleScripts/EncounterGenerator/UrbanEncounters.dat", 'r')]
        dice = randint(0, len(encounterArray)-1)
        enemiesString = encounterArray[dice]
    else:
        enemiesString = 'We had a problem Sir'
    return enemiesString

#print encounter(1)
