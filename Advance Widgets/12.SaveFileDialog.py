from tkinter import *
from tkinter import ttk
from tkinter import filedialog

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

txtE = Text(root,width=25,height=15,wrap=WORD)
txtE.pack()
btn1 = ttk.Button(root,text='Open',command=openFile).pack(side=LEFT,padx=(130,20))
btn2 = ttk.Button(root,text='Save',command=saveFile).pack(side=LEFT)

root.geometry('450x450+350+250')
root.mainloop()