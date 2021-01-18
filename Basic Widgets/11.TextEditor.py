from tkinter import *

root = Tk()

def callSave():
    """
    text editor save function
    """
    text = txtEdit.get(1.0,END)
    file = open('Teditor.txt','a')
    file.write(text)
    file.write('\n')
    file.close()

txtEdit = Text(root,width=30,height=10,font=(('Times'),15),wrap=WORD)
txtEdit.insert(INSERT,'Type Something...')
txtEdit.grid(row=0,column=0,pady=20,padx=40)
btn = Button(root,text='Save',width=10,height=1,command=callSave)
btn.grid(row=3,column=0)

root.geometry('550x550')
root.mainloop()