"""
 ___  _____     Python - Dice Roller - v 2.1.1
|    |_   _|    I took the script I had in the file DiceRoller.py and I placed into a friendly GUI.
|   _  | |      It's working and I'm very happy about it, after I've finished other scripts I'll come back.
|___|  | |      And make it a little more pleasant to the eye.
      /_ /      In version 2.1 I added a much needed modifier box so that you can get a result with the modifier
                already added.
                Pietro Goodjohn Bongiovanni - November 2015
"""
import tkinter as tk
from tkinter import *
from tkinter.messagebox import *
from random import randint
import tkinter.ttk
import sys
import os

from random import randint

class DiceRoller(tk.Frame):
    def __init__(self,root):
        tk.Frame.__init__(self, root)
        #Defining the variable of the Radio Button
        self.var = IntVar()
        self.dicesEntry = IntVar()
        self.modifierEntry = IntVar()

        #Dice Number Input, the value is then got inside the function RollDices
        dicesLabel = Label(self, text = 'Number of Dices:')
        self.dicesEntry = Entry(self)
        self.dicesEntry.insert(1, '1')

        #Modifier Input, same as the Dice Number
        modifierLabel = Label(self, text = 'Modifier: +')
        self.modifierEntry = Entry(self)
        self.modifierEntry.insert(1, '0')

        #Text widget were the result of every single dice and the result of the sum of dices will be displayed
        self.text = Text(self)
        self.text.config(state=DISABLED)
        self.text.config(height = 12, width = 50)

        #Radio Buttons for dice Type
        d20 = Radiobutton(self, text = "d20", variable = self.var, value = 20)
        d12 = Radiobutton(self, text = "d12", variable = self.var, value = 12)
        d10 = Radiobutton(self, text = "d10", variable = self.var, value = 10)
        d8 = Radiobutton(self, text = "d8", variable = self.var, value = 8)
        d6 = Radiobutton(self, text = "d6", variable = self.var, value = 6)
        d4 = Radiobutton(self, text = "d4", variable = self.var, value = 4)
        d100 = Radiobutton(self, text = "d100", variable = self.var, value = 100)

        #Buttons to rolling dices and closing the application.
        roll = Button(self, text = 'Roll', command = self.RollDices)

        #Grid Placement
        #Dimension Scaling
        self.grid_columnconfigure(0,weight=1)
        self.grid_columnconfigure(1,weight=1)
        self.grid_columnconfigure(2,weight=1)
        self.grid_columnconfigure(3,weight=1)
        self.grid_rowconfigure(0,weight=1)
        self.grid_rowconfigure(1,weight=1)
        self.grid_rowconfigure(2,weight=1)
        self.grid_rowconfigure(3,weight=1)
        self.grid_rowconfigure(4,weight=1)
        self.grid_rowconfigure(5,weight=1)

        #Dice Number Input
        dicesLabel.grid(row = 0, column = 0)
        self.dicesEntry.grid(row = 0, column = 1)

        #Modifier Input
        modifierLabel.grid(row = 1, column = 0)
        self.modifierEntry.grid(row = 1, column = 1)

        #Text Result
        self.text.grid(row = 0, column = 3, rowspan = 6, sticky = NW + SE)

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

    def RollDices(self):
        '''
        This function rolls the dices, it gets the number of dices from dicesEntry
        and the type of dice from the radio button and then runs the script present also in the
        command line application DiceRoller.py


        '''
        if(self.dicesEntry.get()):
            if(self.modifierEntry.get()):
                diceNumber = self.dicesEntry.get()
                modifier = self.modifierEntry.get()
                if(diceNumber.isdigit()):
                    try:
                        modifier = int(modifier)
                        diceNumber = int(diceNumber)
                        diceType = self.var.get()
                        if(diceType):
                            dice = 0
                            diceTotal = 0
                            stringResult = ''
                            for dice in range(0, diceNumber):
                                diceRoll = randint(1, diceType)
                                diceTotal = diceTotal + diceRoll
                                stringResult = stringResult + 'Dice number ' + str(dice+1) + ' result = ' + str(diceRoll) + '\n'

                            self.text.config(state=NORMAL)
                            self.text.delete(1.0, END)
                            self.text.insert(INSERT, stringResult + 'Result is %d, with the modifier is %d' % (diceTotal,diceTotal+modifier))
                            self.text.config(state=DISABLED)
                        else:
                            showerror('Error', 'Please choose a dice type')
                    except:
                        showerror('Error', 'Please insert a numeric value in the modifier field')
                else:
                    showerror('Error', 'Please insert a numeric value in the number of dices field')

            else:
                showerror('Error', 'Please insert a numeric value in the modifier field')
        else:
            showerror('Error', 'Please insert a numeric value in the number of dices field')
#LAUNCH APPLICATION
if __name__ == '__main__':
    root = tk.Tk()
    root.wm_title("D&D Tools")

    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    root.geometry('%dx%d' %(3*screen_width/4, screen_height/2))

    notebook = tkinter.ttk.Notebook(root)

    tab1 = DiceRoller(root)

    notebook.add(tab1, text = 'Dice Roller')

    root.grid_columnconfigure(0,weight=1)
    root.grid_rowconfigure(0,weight=1)
    notebook.grid(row = 0, column = 0, sticky = NW + SE)
    root.mainloop()
