#/*
# * @Author: Pasindu Akalpa 
# * @Date: 2021-01-16 17:49:34 
# * @Last Modified by: Pasindu Akalpa 
# * @Last Modified time: 2021-01-16 17:49:34 
# */


from tkinter import *
from tkinter import ttk

root = Tk()

root.geometry('500x450')#Set Custom GUI Size

button1 = Button(root,text = 'Click Me!')#Tkinter Button
button2 = ttk.Button(root,text = 'Click Me!')#ttk button

#pack = Geometry Manager
button1.pack()
button2.pack()

root.mainloop()
