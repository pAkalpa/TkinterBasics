from tkinter import *
from tkinter import ttk

root = Tk()

tabs = ttk.Notebook(root)
tabs.pack(fill=BOTH,expand=True)
#icon = PhotoImage(file='')
tab1 = ttk.Frame(tabs)
tab2 = ttk.Frame(tabs)
tabs.add(tab1,text='First Tab')
#tabs.add(tab2,text='Second Tab',image=icon,compound=LEFT) #add icons to Tabs
tabs.add(tab2,text='Second Tab')
lbl = ttk.Label(tab1,text='Hello').place(x=200,y=20)
btn = ttk.Button(tab2,text='Click Me!').place(x=250,y=50)#use tabs as frame for use ui elements in all the tabs

root.geometry('650x650+650+200')
root.mainloop()