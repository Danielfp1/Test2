from tkinter import *

import pyperclip
import time

arq=open('arq.txt',"r")

root = Tk()
class Fun:
    def __init__(self, cont, pausa,aux):
        self.cont=cont
        self.pausa = pausa
        self.aux = aux

ob = Fun(100,0,"")

def run():
    while pausa:
        ob.cont=ob.cont+1
        print(ob.cont)
        linha=arq.readline()
        print (linha)
        pyperclip.copy(linha)
        time.sleep(5)
        if pausa==0:
            break

def pausa():
	pausa= not pausa


button1 = Button(root,text="Run",fg="Green",command=run)
button2 = Button(root,text="Pausar",fg="red",command=pausa)
button2.pack()
button1.pack()

root.mainloop()

#da pra tu ler? responde no whats :3