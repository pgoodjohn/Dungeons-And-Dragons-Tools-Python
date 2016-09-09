'''
 ___  _____     Python - Dungeons And Dragons Tools
|    |_   _|    Finally I managed to crap everything I made so far in a single GUI.
|   _  | |      I'm still working on the single script as well as on the GUI of this window so it should get better!
|___|  | |      Right now tho I am very happy with the result.
      /_ /      Pietro Goodjohn Bongiovanni - December 2015
'''

import tkinter as tk
from tkinter import *
from tkinter.messagebox import *
from random import randint
import tkinter.ttk as ttk
import sys
import os
sys.path.insert(0, './SingleScripts/WeaponGenerator')
import WeaponGenerator as wg
sys.path.insert(0, './SingleScripts/NameGenerator')
import NameGenerator as ng
sys.path.insert(0, './SingleScripts/NPCGenerator')
import npcgenerator as npc
sys.path.insert(0, './SingleScripts/EncounterGenerator')
import EncounterGenerator as ec

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
                            diceTotal = 0;
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

class WeaponGenerator(tk.Frame):
    def __init__(self,root):
        tk.Frame.__init__(self, root)
        weapon = ''

        self.text = Text(self)
        self.text.config(state=DISABLED)
        self.text.config(height = 5, width = 75)

        generate = Button(self, text = 'Generate', command = self.Generate)

        self.text.pack(side = LEFT, fill = BOTH, expand = YES)
        generate.pack(side = LEFT)

    def Generate(self):
        weapon = wg.generate()
        self.text.config(state=NORMAL)
        self.text.delete(1.0, END)
        self.text.insert(INSERT, weapon)
        self.text.config(state=DISABLED)

class NameGenerator(tk.Frame):
    def __init__(self,root):
        tk.Frame.__init__(self, root)

        #initializing the two variables
        self.gender = IntVar()
        self.race = IntVar()

        #Labels
        self.genderLabel = Label(self, text = 'Gender:')
        self.raceLabel = Label(self, text = 'Race:')

        #Radio button for gender
        male = Radiobutton(self, text = 'Male', variable = self.gender, value = 0)
        female = Radiobutton(self, text = 'Female', variable = self.gender, value = 1)

        #Radio button for race
        dwarf = Radiobutton(self, text = 'Dwarf', variable = self.race, value = 1)
        elves = Radiobutton(self, text = 'Elves', variable = self.race, value = 2)
        human = Radiobutton(self, text = 'Human', variable = self.race, value = 3)
        gnome = Radiobutton(self, text = 'Gnome', variable = self.race, value = 4)
        halfelf = Radiobutton(self, text = 'Half Elf', variable = self.race, value = 5)
        orc = Radiobutton(self, text = 'Orc', variable = self.race, value = 6)
        halfling = Radiobutton(self, text = 'Halfling', variable = self.race, value = 7)

        #Text widget were the result of every single dice and the result of the sum of dices will be displayed
        self.text = Text(self)
        self.text.config(state=DISABLED)
        self.text.config(height = 6, width = 26)

        #Buttons
        create = Button(self, text = 'Generate Name', command = self.create)

        #Geometry
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
        self.grid_rowconfigure(6,weight=1)
        self.grid_rowconfigure(7,weight=1)
        self.grid_rowconfigure(8,weight=1)

        self.text.grid(row = 0, column = 0, columnspan = 3, sticky = E+W)
        self.genderLabel.grid(row = 1, column = 0, sticky = NW)
        self.raceLabel.grid(row = 1, column = 1, sticky = NW)
        dwarf.grid(row = 2, column = 1, sticky = NW)
        elves.grid(row = 3, column = 1, sticky = NW)
        human.grid(row = 4, column = 1, sticky = NW)
        gnome.grid(row = 5, column = 1, sticky = NW)
        halfelf.grid(row = 6, column = 1, sticky = NW)
        orc.grid(row = 7, column = 1, sticky = NW)
        halfling.grid(row = 8, column = 1, sticky = NW)
        male.grid(row = 2, column = 0, sticky = NW)
        female.grid(row = 3, column = 0, sticky = NW)
        create.grid(row = 2, column = 3, sticky = NW)

    def create(self):
        self.gendervar = self.gender.get()
        if(self.gendervar == 0 or self.gendervar == 1):
            racevar = self.race.get()
            if(racevar):
                string = ng.generate(self.gendervar,racevar)
                self.text.config(state=NORMAL)
                self.text.delete(1.0, END)
                self.text.insert(INSERT,string)
                self.text.config(state=DISABLED)
            else:
                showerror('Error', 'Please select a race')
        else:
            showerror('Error', 'Please select a gender')

class NPCGenerator(tk.Frame):
    def __init__(self,root):
        tk.Frame.__init__(self, root)

        generateFighter = Button(self, text = 'Generate Fighter', command = self.GenerateFighter)
        generateCitizen = Button(self, text = 'Genereate Citizen', command = self.GenerateCitizen)
        quit = Button(root, text = 'Quit', command = self.quit)

        self.text = Text(self)
        self.text.config(state=DISABLED)
        self.text.config(height = 12, width = 50)

        self.grid_columnconfigure(0,weight=1)
        self.grid_rowconfigure(0,weight=1)
        self.grid_rowconfigure(1,weight=1)
        self.grid_rowconfigure(2,weight=1)

        self.text.grid(row = 0, column = 0, sticky = SE+NW)
        generateFighter.grid(row = 0, column = 1, sticky = E)
        generateCitizen.grid(row = 1, column = 1, sticky = E)
        #quit.grid(row = 2, column = 0, sticky = W)

    def GenerateFighter(self):
        string = npc.generateNPC(0)
        self.text.config(state=NORMAL)
        self.text.delete(1.0, END)
        self.text.insert(INSERT, string)
        self.text.config(state=DISABLED)

    def GenerateCitizen(self):
        string = npc.generateNPC(1)
        self.text.config(state=NORMAL)
        self.text.delete(1.0, END)
        self.text.insert(INSERT, string)
        self.text.config(state=DISABLED)

    def quit(self):
        sys.exit()

class EncounterGenerator(tk.Frame):
    def __init__(self, root):
        tk.Frame.__init__(self, root)

        self.place = IntVar()
        self.placemodifier = IntVar()

        self.text = Text(self) #self
        self.text.config(state=DISABLED)
        self.text.config(height = 12, width = 50)

        town = Radiobutton(self, text = 'Town', variable = self.place, value = 1)#self
        jungle = Radiobutton(self, text = 'Jungle', variable = self.place, value = 2, state = DISABLED)
        desert = Radiobutton(self, text = 'Desert', variable = self.place, value = 3, state = DISABLED)
        plane = Radiobutton(self, text = 'Other Plane', variable = self.place, value = 4, state = DISABLED)

        encounter = Button(self, text = 'Generate Encounter', command = self.encounter)#self

        self.grid_columnconfigure(0,weight=1)
        self.grid_rowconfigure(0,weight=1)
        self.grid_rowconfigure(1,weight=1)
        self.grid_rowconfigure(2,weight=1)
        self.grid_rowconfigure(3,weight=1)
        self.grid_rowconfigure(4,weight=1)
        self.grid_rowconfigure(5,weight=1)

        self.text.grid(row = 0, column = 0, rowspan = 10, sticky = NW+SE)
        town.grid(row = 1, column = 1)
        jungle.grid(row = 2, column = 1)
        desert.grid(row = 3, column = 1)
        plane.grid(row = 4, column = 1)
        encounter.grid(row = 5, column = 1)

    def encounter(self):
        placevar = self.place.get()
        if(placevar):
            string = ec.encounter(placevar)
            self.text.config(state=NORMAL)
            self.text.delete(1.0, END)
            self.text.insert(INSERT,string)
            self.text.config(state=DISABLED)
        else:
            showerror('Error', 'Please select a place')

#LAUNCH APPLICATION
if __name__ == '__main__':
    root = tk.Tk()
    root.wm_title("D&D Tools")

    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    root.geometry('%dx%d' %(3*screen_width/4, screen_height/2))

    notebook = ttk.Notebook(root)

    tab1 = DiceRoller(root)
    tab2 = WeaponGenerator(root)
    tab3 = NameGenerator(root)
    tab4 = NPCGenerator(root)
    tab5 = EncounterGenerator(root)

    notebook.add(tab1, text = 'Dice Roller')
    notebook.add(tab2, text = 'Weapon Generator')
    notebook.add(tab3, text = 'Name Generator')
    notebook.add(tab4, text = 'NPC Generator')
    notebook.add(tab5, text = 'Encounter Generator')

    root.grid_columnconfigure(0,weight=1)
    root.grid_rowconfigure(0,weight=1)
    notebook.grid(row = 0, column = 0, sticky = NW + SE)
    root.mainloop()
