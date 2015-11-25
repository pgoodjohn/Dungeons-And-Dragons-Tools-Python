'''
 ___  _____     Python - Dice Roller - v 2.0
|    |_   _|    I took the script I had in the file DiceRoller.py and I placed into a friendly GUI.
|   _  | |      It's working and I'm very happy about it, after I've finished other scripts I'll come back.
|___|  | |      And make it a little more pleasant to the eye.
      /_ /      Pietro Goodjohn Bongiovanni - November 2015
'''

from Tkinter import *
from random import randint
from tkMessageBox import *

#Functions
def RollDices():
    '''
    This function rolls the dices, it gets the number of dices from entryDices
    and the type of dice from the radio button and then runs the script present also in the
    command line application DiceRoller.py
    '''
    if(entryDices.get()):
        diceNumber = entryDices.get()
        if(diceNumber.isdigit()):
            diceNumber = int(diceNumber)
            diceType = var.get()
            if(diceType):
                dice = 0
                diceTotal = 0;
                stringResult = ''
                for dice in range(0, diceNumber):
                    diceRoll = randint(1, diceType)
                    diceTotal = diceTotal + diceRoll
                    stringResult = stringResult + 'Dice number ' + str(dice+1) + ' result = ' + str(diceRoll) + '\n'
                    #print "Dice #%r = %r" % (dice+1, diceRoll)
                #print "Result is %r" % diceTotal
                text.config(state=NORMAL)
                labelResult.config(text = stringResult + 'Result is %d' % diceTotal)
                text.delete(1.0, END)
                text.insert(INSERT, stringResult + 'Result is %d' % diceTotal)
                text.config(state=DISABLED)
                #showinfo('Result', stringResult + 'Result is %d' % diceTotal)
            else:
                showerror('Error', 'Please choose a dice type')
                #print 'Error'
        else:
            showerror('Error', 'Please insert a numeric value in the number of dices')
    else:
        showerror('Error', 'Please insert a numeric value in the number of dices')
        #print 'Error'


main = Tk()
main.wm_title("Dice Roller")


var = IntVar()

#Dice Number Input
labelInput = Label(main, text = 'Number of Dices:')
entryDices = Entry(main)
entryDices.insert(1, '1')

#Result Label
stringResult = ''
labelResult = Label(main, text = stringResult)

text = Text(main)
text.insert(INSERT, stringResult)
text.config(height = 12, width = 30)



#Radio Buttons for dice Type
d20 = Radiobutton(main, text = "d20", variable = var, value = 20)
d12 = Radiobutton(main, text = "d12", variable = var, value = 12)
d10 = Radiobutton(main, text = "d10", variable = var, value = 10)
d8 = Radiobutton(main, text = "d8", variable = var, value = 8)
d6 = Radiobutton(main, text = "d6", variable = var, value = 6)
d4 = Radiobutton(main, text = "d4", variable = var, value = 4)
d100 = Radiobutton(main, text = "d100", variable = var, value = 100)

#Buttons to roll and quit.
roll = Button(main, text = 'Roll', command = RollDices)
quit = Button(main, text = 'Quit', command = quit)


#Grid Placement
#Dice Number Input
labelInput.grid(row = 0, column = 0)
entryDices.grid(row = 0, column = 1)

#Label Result
text.grid(row = 0, column = 3, rowspan = 5)

#Radio Buttons
d20.grid(row = 1, column = 0, sticky = W)
d12.grid(row = 1, column = 1, sticky = W)
d10.grid(row = 2, column = 0, sticky = W)
d8.grid(row = 2, column = 1, sticky = W)
d6.grid(row = 3, column = 0, sticky = W)
d4.grid(row = 3, column = 1, sticky = W)
d100.grid(row = 4, column = 0, sticky = W)

#Buttons
roll.grid(row = 4, column = 1, sticky = E)
quit.grid(row = 5, column = 1, sticky = E)
main.mainloop()
