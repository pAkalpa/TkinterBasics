from tkinter import *
from typing import Counter
import time
root = Tk()

def callback():
    """
    Change Label Text and Properties
    """
    label.config(text='You Clicked Me!',fg='red',bg='yellow')
    btn['state'] = 'disabled'
       

label = Label(root,text='Hello Python')
label.pack()
btn = Button(root,text='Click Me!',command=callback)
btn.pack()
root.geometry('350x300')
root.mainloop()