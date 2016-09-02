from tkinter import *

import os.path
directory,filename = os.path.split(__file__)
import sys
sys.path.append(directory)
import npcgenerator

def GenerateRandom():
    string = npcgenerator.generateNPC(0)
    text.config(state=NORMAL)
    text.delete(1.0, END)
    text.insert(INSERT, string)
    text.config(state=DISABLED)

def GenerateCitizen():
    string = npcgenerator.generateNPC(1)
    text.config(state=NORMAL)
    text.delete(1.0, END)
    text.insert(INSERT, string)
    text.config(state=DISABLED)


root = Tk()

generate = Button(root, text = 'Generate a Non-Citizen', command = GenerateRandom)
generate2 = Button(root, text = 'Generate a Citizen', command = GenerateCitizen)
quit = Button(root, text = 'Quit', command = quit)

text = Text(root)
text.config(state=DISABLED)
text.config(height = 12, width = 50)

root.grid_columnconfigure(0,weight=1)
root.grid_rowconfigure(0,weight=1)
root.grid_rowconfigure(1,weight=1)
root.grid_rowconfigure(2,weight=1)

text.grid(row = 0, column = 0, sticky = E+W)
generate.grid(row = 1, column = 0, sticky = E)
generate2.grid(row = 2, column = 0, sticky = E)
quit.grid(row = 3, column = 0, sticky = E)
root.mainloop()
