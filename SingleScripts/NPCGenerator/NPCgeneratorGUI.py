from Tkinter import *
import npcgenerator

def GenerateRandom():
    string = npcgenerator.generateNPC()
    text.config(state=NORMAL)
    text.delete(1.0, END)
    text.insert(INSERT, string)
    text.config(state=DISABLED)

root = Tk()

generate = Button(root, text = 'Generate', command = GenerateRandom)
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
quit.grid(row = 2, column = 0, sticky = E)
root.mainloop()
