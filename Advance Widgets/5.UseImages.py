from tkinter import *
from tkinter import ttk

root = Tk()
root.title('Using Images')

lbl = ttk.Label(root,text='Using Images',font=(('Times'),18))
lbl.pack()
logo = PhotoImage(file='filepath(relative or absolute)')
lbl_img = ttk.Label(root,image=logo)
lbl_img.pack()

root.geometry('350x350')
root.mainloop()