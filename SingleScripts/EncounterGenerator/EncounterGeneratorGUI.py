'''
 ___  _____     Python - Encounter Generator - v 1.0
|    |_   _|
|   _  | |
|___|  | |
      /_ /      Pietro Goodjohn Bongiovanni - December 2015
'''

import tkinter as tk
from tkinter import *
from tkinter.messagebox import *
from random import randint


import EncounterGenerator as ec
import os.path
directory,filename = os.path.split(__file__)


class EncounterGenerator(tk.Frame):
    def __init__(self, root):
        tk.Frame.__init__(self, root)

        self.place = IntVar()
        self.placemodifier = IntVar()

        self.text = Text(root) #self
        self.text.config(state=DISABLED)
        self.text.config(height = 12, width = 50)

        smalltown = Radiobutton(root, text = 'Small Town', variable = self.place, value = 1)#self
        town = Radiobutton(root, text = 'Town', variable = self.place, value = 2)#self
        metropolis = Radiobutton(root, text = 'Metropolis', variable = self.place, value = 3)#self
        encounter = Button(root, text = 'Generate Encounter', command = self.encounter)#self
        quit = Button(root, text = 'Quit', command = self.quit) #self

        self.text.pack()
        smalltown.pack()
        town.pack()
        metropolis.pack()
        encounter.pack()
        quit.pack()

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

    def quit(self):
        sys.exit()


if __name__ == '__main__':
    root = tk.Tk()
    root.wm_title("Encounter Generator")

    app = EncounterGenerator(root)

    root.grid_columnconfigure(0,weight=1)
    root.grid_rowconfigure(0,weight=1)
    root.mainloop()
