from tkinter import *
from tkinter import ttk

root = Tk()

tBox = Text(root,width=60,height=20,wrap='word')
tBox.grid(row=0,column=0)

scroll = ttk.Scrollbar(root,orient=VERTICAL,command=tBox.yview)
scroll.grid(row=0,column=1,sticky=N+S)
tBox.config(yscrollcommand=scroll.set)

root.geometry('500x450')
root.mainloop()