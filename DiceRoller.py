'''
 ___  _____     Python - Dice Roller - v 1.0
|    |_   _|    A simple command-line dice roller based on Python's random number generator for tabletop games.
|   _  | |
|___|  | |
      /_ /      Pietro Goodjohn Bongiovanni - November 2015
'''

from random import randint

while True:
    diceNumber = input('Choose number of dices ')
    diceType = input('Choose dice type ')
    dice = 0
    diceTotal = 0;

    '''while (i < diceNumber):
        diceRoll = randint(1, diceType)
        diceTotal = diceTotal + diceRoll
        print "Dice #%r = %r " % (i + 1, diceRoll)
        i += 1'''

    for dice in range(0, diceNumber):
        diceRoll = randint(1, diceType)
        diceTotal = diceTotal + diceRoll
        print "Dice #%r = %r" % (dice+1, diceRoll)
    print "Result is %r" % diceTotal
