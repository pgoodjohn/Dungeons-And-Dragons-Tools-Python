'''
 ___  _____     Python - Dice Roller - v 1.1
|    |_   _|    A simple command-line dice roller based on Python's random number generator for tabletop games.
|   _  | |      Update!! I made a GUI version, it uses the same script but is much nicer to use!
|___|  | |
      /_ /      Pietro Goodjohn Bongiovanni - November 2015
'''

from random import randint

while True:
    diceNumber = input('Choose number of dices ')
    diceType = input('Choose dice type ')
    dice = 0
    diceTotal = 0

    for dice in range(0, int(diceNumber)):
        diceRoll = randint(1, int(diceType))
        diceTotal = diceTotal + diceRoll
        print("Dice #%r = %r" % (dice+1, diceRoll))
    print("Result is %r" % diceTotal)
