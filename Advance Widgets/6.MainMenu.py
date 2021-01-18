from tkinter import *
from tkinter import messagebox

root = Tk()

menuBar = Menu(root)
root.config(menu=menuBar)

def callExit():
    """
    Exit Program
    """
    mbox = messagebox.askquestion('Exit','Are You Sure to Exit?',icon='warning')
    if mbox == 'yes':
        root.destroy()

fileMenu = Menu(menuBar,tearoff=0) #tearoff = small dashed line
menuBar.add_cascade(label='File',menu=fileMenu)
newIco = PhotoImage(file='files/file.png')
fileMenu.add_command(label='New',image=newIco,compound=LEFT)
fileMenu.add_separator()
openIco = PhotoImage(file='files/open.png')
fileMenu.add_command(label='Open',image=openIco,compound=LEFT)
fileMenu.add_separator()
fileMenu.add_command(label='Save')
fileMenu.add_separator()
fileMenu.add_command(label='Exit',command=callExit)

editMenu = Menu(menuBar,tearoff=0)
menuBar.add_cascade(label='Edit',menu=editMenu)
editMenu.add_command(label='Undo')
editMenu.add_command(label='Redo')
editMenu.add_separator()
editMenu.add_command(label='Cut')
editMenu.add_command(label='Copy')
editMenu.add_command(label='Paste')

aboutMenu = Menu(menuBar,tearoff=0)
menuBar.add_cascade(label='About',menu=aboutMenu)

root.geometry('650x650+350+100')
root.mainloop()