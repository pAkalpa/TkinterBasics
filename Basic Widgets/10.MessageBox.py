from tkinter import *
from tkinter import ttk
from tkinter import messagebox

root = Tk()

def callDel():
    """
    Delete
    """
    mbox = messagebox.askquestion('Delete','Are You Sure',icon='warning')#use varible to declare mbox if only want to take inputs
    if mbox == 'yes':
        print('Deleted')
    else:
        print('Not Deleted')

def callInf():
    """
    Info Message Box
    """
    messagebox.showinfo('Success','Well Done')

btn1 = ttk.Button(root,text='Delete',command=callDel).grid(row=0,column=0,pady=25,padx=50)
btn2 = ttk.Button(root,text='Info',command=callInf).grid(row=0,column=1)

root.geometry('350x250')
root.mainloop()