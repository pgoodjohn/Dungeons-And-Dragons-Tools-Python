'''
 ___  _____     Python - Dice Roller - v 2.1
|    |_   _|    I took the script I had in the file DiceRoller.py and I placed into a friendly GUI.
|   _  | |      It's working and I'm very happy about it, after I've finished other scripts I'll come back.
|___|  | |      And make it a little more pleasant to the eye.
      /_ /      In version 2.1 I added a much needed modifier box so that you can get a result with the modifier
                already added.
                Pietro Goodjohn Bongiovanni - November 2015
'''

from Tkinter import *
from random import randint
from tkMessageBox import *

#Functions
def RollDices():
    '''
    This function rolls the dices, it gets the number of dices from dicesEntry
    and the type of dice from the radio button and then runs the script present also in the
    command line application DiceRoller.py
    '''
    if(dicesEntry.get()):
        if(modifierEntry.get()):
            diceNumber = dicesEntry.get()
            modifier = modifierEntry.get()
            if(diceNumber.isdigit()):
                if(modifier.isdigit()):
                    diceNumber = int(diceNumber)
                    modifier = int(modifier)
                    diceType = var.get()
                    if(diceType):
                        dice = 0
                        diceTotal = 0;
                        stringResult = ''
                        for dice in range(0, diceNumber):
                            diceRoll = randint(1, diceType)
                            diceTotal = diceTotal + diceRoll
                            stringResult = stringResult + 'Dice number ' + str(dice+1) + ' result = ' + str(diceRoll) + '\n'

                        text.config(state=NORMAL)
                        text.delete(1.0, END)
                        text.insert(INSERT, stringResult + 'Result is %d, with the modifier is %d' % (diceTotal,diceTotal+modifier))
                        text.config(state=DISABLED)
                    else:
                        showerror('Error', 'Please choose a dice type')
                else:
                    showerror('Error', 'Please insert a numeric value in the modifier field')
            else:
                showerror('Error', 'Please insert a numeric value in the number of dices field')

        else:
            showerror('Error', 'Please insert a numeric value in the modifier field')
    else:
        showerror('Error', 'Please insert a numeric value in the number of dices field')

#Starting the window, I'll have to add an icon and some other stuff later.
main = Tk()
main.wm_title("Dice Roller")

#Defining the variable of the Radio Button
var = IntVar()

#Dice Number Input, the value is then got inside the function RollDices
dicesLabel = Label(main, text = 'Number of Dices:')
dicesEntry = Entry(main)
dicesEntry.insert(1, '1')

#Modifier Input, same as the Dice Number
modifierLabel = Label(main, text = 'Modifier: +')
modifierEntry = Entry(main)
modifierEntry.insert(1, '0')

#Text widget were the result of every single dice and the result of the sum of dices will be displayed
text = Text(main)
text.config(state=DISABLED)
text.config(height = 12, width = 50)

#Radio Buttons for dice Type
d20 = Radiobutton(main, text = "d20", variable = var, value = 20)
d12 = Radiobutton(main, text = "d12", variable = var, value = 12)
d10 = Radiobutton(main, text = "d10", variable = var, value = 10)
d8 = Radiobutton(main, text = "d8", variable = var, value = 8)
d6 = Radiobutton(main, text = "d6", variable = var, value = 6)
d4 = Radiobutton(main, text = "d4", variable = var, value = 4)
d100 = Radiobutton(main, text = "d100", variable = var, value = 100)

#Buttons to rolling dices and closing the application.
roll = Button(main, text = 'Roll', command = RollDices)
quit = Button(main, text = 'Quit', command = quit)

#Grid Placement
#Dice Number Input
dicesLabel.grid(row = 0, column = 0)
dicesEntry.grid(row = 0, column = 1)

#Modifier Input
modifierLabel.grid(row = 1, column = 0)
modifierEntry.grid(row = 1, column = 1)

#Text Result
text.grid(row = 0, column = 3, rowspan = 6)

#Radio Buttons
d20.grid(row = 2, column = 0, sticky = W)
d12.grid(row = 2, column = 1, sticky = W)
d10.grid(row = 3, column = 0, sticky = W)
d8.grid(row = 3, column = 1, sticky = W)
d6.grid(row = 4, column = 0, sticky = W)
d4.grid(row = 4, column = 1, sticky = W)
d100.grid(row = 5, column = 0, sticky = W)

#Buttons
roll.grid(row = 5, column = 1, sticky = E)
quit.grid(row = 6, column = 1, sticky = E)

main.mainloop()
