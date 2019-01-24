import tkinter
from tkinter import simpledialog
from tkinter import ttk
from tkinter import StringVar
from tkinter import Label
#################
import Enigma
#################

machine = Enigma.Enigma()
machine.init_Rotors()





window = tkinter.Tk()
turing = StringVar()
# to rename the title of the window
window.title("Enigma Machine")
#
uInput = StringVar()
# pack is used to show the object in the window
encLab = tkinter.Label(window, text="Encrypt").grid(row=0)
decLab = tkinter.Label(window, text="Decrypt").grid(row=1)
decrypt = tkinter.Label(window,textvariable=turing).grid(row=1,column=1)
terminate = tkinter.Button(window, text='Quit', command=window.quit).grid(row=2, column=2, pady=4)


def encode(turing):
    text = uInput.get()
    answer = ""
    for x in text:
        answer = answer + machine.start(x)
    turing.set(answer)

def plugConnect():
    sPlug = simpledialog.askstring("Input", "Enter PlugBoard Connections",
                                   parent=window)
    machine.board.get_connections(sPlug)
    machine.board.connect_plugs()


encodeButton = tkinter.Button(window, text='Encode', command=lambda: encode(turing)).grid(row = 2, column=1)
plugButton = tkinter.Button(window, text='PlugBoard', command=lambda: plugConnect()).grid(row = 3)
####
encrypt = tkinter.Entry(window, textvariable = uInput)
####
encrypt.grid(row=0,column=1)
###


cmd_button = ttk.Button(window, text="Example")




window.mainloop()
