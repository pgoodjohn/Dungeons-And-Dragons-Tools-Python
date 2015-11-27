'''
 ___  _____     Python - Magic Weapon Generator for D&D 3.5 - Version 1.1
|    |_   _|    GUI For my magic weapon generator!
|   _  | |      The WeaponGenerator script is still not ready, but I made some adjustments to use it in this
|___|  | |      GUI, next step is finishing the script, then go on with other projects!!
      /_ /      Pietro Goodjohn Bongiovanni - November 2015
'''

from Tkinter import *
from random import randint
import WeaponGenerator

main = Tk()
main.wm_title("Magic Weapon Generator")

def Generate():
    weapon = WeaponGenerator.generate()
    text.config(state=NORMAL)
    text.delete(1.0, END)
    text.insert(INSERT, weapon)
    text.config(state=DISABLED)

weapon = ''

text = Text(main)
text.config(state=DISABLED)
text.config(height = 5, width = 75)

generate = Button(main, text = 'Generate', command = Generate)
quit = Button(main, text = 'Quit', command = quit)

text.pack(side = LEFT, fill = BOTH, expand = YES)
generate.pack(side = LEFT)
quit.pack(side = RIGHT)
'''
text.grid(row = 0, column = 0, rowspan = 2)
generate.grid(row = 0, column = 1)
quit.grid(row = 1, column = 1)
'''
main.mainloop()
