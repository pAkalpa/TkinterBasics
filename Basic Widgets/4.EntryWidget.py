from tkinter import *
from tkinter import ttk

root = Tk()
root.geometry('300x300')

ent1 = ttk.Entry(root,width=30)
ent2 = ttk.Entry(root,width=30)

ent1.insert(0,'Please Enter Your Name')#Entry Hint
ent2.config(show='\u2022')#make text to charater like password entry

def callRe():
    """
    Show Entry 1 and Entry 2 Inputs in Terminal
    """
    #ent1.state(['disabled'])#use (['!disabled']) for normal
    #ent2.state(['disabled'])
    btn1.state(['disabled'])
    val1 = ent1.get()
    val2 = ent2.get()
    print('Your Name is '+val1+'\nYour Password is '+val2)

btn1 = ttk.Button(root,text='Reveal!',command=callRe)
ent1.state(['readonly'])#This is useful for key sharing and clipboard like applications

ent1.pack()
ent2.pack()
btn1.pack()

root.mainloop()
