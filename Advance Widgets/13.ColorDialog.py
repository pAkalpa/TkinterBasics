from tkinter import *
from tkinter import ttk
from tkinter import filedialog,colorchooser
import tkinter

root = Tk()

def openFile():
    """
    open file dialog
    """
    filenme = filedialog.askopenfilename(initialdir='/',title='Select a File',filetypes=(('Txt Files','.txt'),('All Files','*.*')))
    content = open(filenme).read()
    txtE.insert(END,content)

def saveFile():
    """
    save file dialog
    """
    mFile = filedialog.asksaveasfile(mode='w',defaultextension='.txt')
    if mFile is None:
        return
    content = txtE.get(1.0,'end-1c')
    mFile.write(content)

def changeColor():
    """
    change color
    """
    color = colorchooser.askcolor()
    txtE.configure(fg=color[1])

txtE = Text(root,width=25,height=15,wrap=WORD)
txtE.pack(pady=(0,1))
btn1 = ttk.Button(root,text='Open',command=openFile).pack(side=LEFT,padx=(95,20))
btn2 = ttk.Button(root,text='Save',command=saveFile).pack(side=LEFT)
btn3 = ttk.Button(root,text='Color',command=changeColor).pack(side=LEFT,padx=(20,0))

root.geometry('450x450+350+250')
root.mainloop()