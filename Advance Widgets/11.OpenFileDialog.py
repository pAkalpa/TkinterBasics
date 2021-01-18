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

txtE = Text(root,width=25,height=15)
txtE.pack()
btn1 = ttk.Button(root,text='Open',command=openFile).pack()

root.geometry('450x450+350+250')
root.mainloop()