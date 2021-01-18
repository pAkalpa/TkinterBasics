from tkinter import *
from tkinter import ttk

root = Tk()

def printVal():
    """
    Print Value of List Box
    """
    selectedItm = listB.curselection()
    for item in selectedItm:
        print(listB.get(item))

def deleteVal():
    """
    Delete Values From List Box
    """
    selectedItm = listB.curselection()
    for item in selectedItm:
        listB.delete(item)

listB = Listbox(root,width=40,height=15,selectmode=MULTIPLE)
listB.pack(pady=25)
listB.insert(0,'Python')
listB.insert(1,'C++')
listB.insert(2,'C#')
listB.insert(3,'PHP')

btn1 = ttk.Button(root,text='Print',command=printVal).place(x=250,y=300)
btn2 = ttk.Button(root,text='Delete',command=deleteVal).place(x=350,y=300)

root.geometry('650x650+650+200')
root.mainloop()