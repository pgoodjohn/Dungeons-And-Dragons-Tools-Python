'''
 ___  _____     Python - Magic Weapon Generator for D&D 3.5 - Version 1.1
|    |_   _|    GUI For my magic weapon generator!
|   _  | |      The WeaponGenerator script is still not ready, but I made some adjustments to use it in this
|___|  | |      GUI, next step is finishing the script, then go on with other projects!!
      /_ /      Pietro Goodjohn Bongiovanni - November 2015
'''

from Tkinter import *
from random import randint
import tkMessageBox
import WeaponGenerator
import WandGenerator

main = Tk()
main.wm_title("Magic Weapon Generator")

def Generate():
    weapon = WeaponGenerator.generate()
    text.config(state=NORMAL)
    text.delete(1.0, END)
    text.insert(INSERT, weapon)
    text.config(state=DISABLED)

def WandGenerate():
    spell = WandGenerator.generateWand()
    text.config(state=NORMAL)
    text.delete(1.0, END)
    text.insert(INSERT, spell)
    text.config(state=DISABLED)

def Legend():
    tkMessageBox.showwarning(
            "Legend",
            '''
            PH: Player's Handbook v3.5
            DMG: Dungeon Master's Guide v3.5
            MM: Monster's Guide v3.5
            MM3: Monster's Manual
            CWar: Complete Warrior
            CDiv: Complete Divine
            CArc: Complete Arcane
            CAdv: Complete Adventurer
            RoS: Races of Stone
            RoD: Races of Destiny
            RotW: Races of the Wild
            RoE: Races of Eberron
            BoED: Book of Exalted Deeds
            UA: Unhearted Arcana
            FR: Forgotten Realms Campaign Setting
            MoF: Magic of Faerun
            LoD: Lords of Darkness
            RoF: Races of Faerun
            SM: Silver Marches
            Und: Underdark
            PGF: Player's Guide of Faerun
            DR###: Dragon Magazine (with issue number)
            DU##: Dungeon Magazine (with issue number)
            3.5up: D&D v.3.5 Accessory Update
            PH3.5e: Player's Handbook v.3.5 Errata
            PGFe: Player's Guide to Faerun Errata
            CDivErrata: Complete Divine Errata
            CArc: Complete Arcane Errata
            EbErrata: Eberron Errata
            '''
        )
    return

weapon = ''

text = Text(main)
text.config(state=DISABLED)
text.config(height = 5, width = 75)

generate = Button(main, text = 'Generate', command = Generate)
wand = Button(main, text = 'Generate Wand', command = WandGenerate)
legend = Button(main, text = 'Legend', command = Legend)
quit = Button(main, text = 'Quit', command = quit)

text.pack(side = LEFT, fill = BOTH, expand = YES)
generate.pack(side = LEFT)
wand.pack(side = LEFT)
legend.pack(side = LEFT)
quit.pack(side = RIGHT)
'''
text.grid(row = 0, column = 0, rowspan = 2)
generate.grid(row = 0, column = 1)
quit.grid(row = 1, column = 1)
'''
main.mainloop()
