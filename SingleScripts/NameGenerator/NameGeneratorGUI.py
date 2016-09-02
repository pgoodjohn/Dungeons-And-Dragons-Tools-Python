'''
 ___  _____     Python - Name Generator GUI- v 1.0
|    |_   _|    Name Generator for fantasy charachters. I want to add more names to the ones I have.
|   _  | |      I want to add more races and more stuff, and probably I will also ad some kind of option to create some sort of
|___|  | |      family like Parents, Sons, Granparents and maybe Greatgranparents.
      /_ /      Pietro Goodjohn Bongiovanni - November 2015
'''

from tkinter import *
import NameGenerator
from tkinter.messagebox import *

def create():
    gendervar = gender.get()
    if(gendervar == 0 or gendervar == 1):
        racevar = race.get()
        if(racevar):
            string = NameGenerator.generate(gendervar,racevar)
            text.config(state=NORMAL)
            text.delete(1.0, END)
            text.insert(INSERT,string)
            text.config(state=DISABLED)
        else:
            showerror('Error', 'Please select a race')
    else:
        showerror('Error', 'Please select a gender')

main = Tk()
main.wm_title('Name Generator')

#initializing the two variables
gender = IntVar()
race = IntVar()

#Labels
genderLabel = Label(main, text = 'Gender:')
raceLabel = Label(main, text = 'Race:')

#Radio button for gender
male = Radiobutton(main, text = 'Male', variable = gender, value = 0)
female = Radiobutton(main, text = 'Female', variable = gender, value = 1)

#Radio button for race
dwarf = Radiobutton(main, text = 'Dwarf', variable = race, value = 1)
elves = Radiobutton(main, text = 'Elves', variable = race, value = 2)
human = Radiobutton(main, text = 'Human', variable = race, value = 3)
gnome = Radiobutton(main, text = 'Gnome', variable = race, value = 4)
halfelf = Radiobutton(main, text = 'Half Elf', variable = race, value = 5)
orc = Radiobutton(main, text = 'Orc', variable = race, value = 6)
halfling = Radiobutton(main, text = 'Halfling', variable = race, value = 7)

#Text widget were the result of every single dice and the result of the sum of dices will be displayed
text = Text(main)
text.config(state=DISABLED)
text.config(height = 6, width = 25)

#Buttons
create = Button(main, text = 'Generate Name', command = create)
quit = Button(main, text = 'Quit', command = quit)

#Geometry
main.grid_columnconfigure(0,weight=1)
main.grid_columnconfigure(1,weight=1)
main.grid_columnconfigure(2,weight=1)
main.grid_columnconfigure(3,weight=1)
main.grid_rowconfigure(0,weight=1)
main.grid_rowconfigure(1,weight=1)
main.grid_rowconfigure(2,weight=1)
main.grid_rowconfigure(3,weight=1)
main.grid_rowconfigure(4,weight=1)
main.grid_rowconfigure(5,weight=1)
main.grid_rowconfigure(6,weight=1)
main.grid_rowconfigure(7,weight=1)
main.grid_rowconfigure(8,weight=1)

text.grid(row = 0, column = 0, columnspan = 3, sticky = E+W)
genderLabel.grid(row = 1, column = 0, sticky = NW)
raceLabel.grid(row = 1, column = 1, sticky = NW)
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
quit.grid(row = 4, column = 3, sticky = NW)

'''
text.pack()
genderLabel.pack()
raceLabel.pack()
dwarf.pack()
elves.pack()
human.pack()
male.pack()
female.pack()
create.pack()
quit.pack()
'''
main.mainloop()
