from tkinter import *
from tkinter import ttk

root = Tk()

panedW = ttk.PanedWindow(root,orient=HORIZONTAL)
panedW.pack(fill=BOTH,expand=TRUE)
frm1 = ttk.Frame(panedW,width=100,height=500,relief=SUNKEN)
frm2 = ttk.Frame(panedW,width=300,height=500,relief=SUNKEN)
frm3 = ttk.Frame(panedW,width=75,height=500,relief=SUNKEN)
panedW.add(frm1,weight=1)
panedW.add(frm2,weight=3)
panedW.insert(1,frm3)

lbl1 = ttk.Label(frm1,text='Hello').grid(row=0,column=0,pady=25)
btn1 = ttk.Button(frm1,text='Click Me').grid(row=1,column=0,padx=20,pady=25)

root.geometry('650x650+650+200')
root.mainloop()