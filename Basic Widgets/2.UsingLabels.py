#/*
# * @Author: Pasindu Akalpa 
# * @Date: 2021-01-16 17:59:41 
# * @Last Modified by:   Pasindu Akalpa 
# * @Last Modified time: 2021-01-16 17:59:41 
# */

from tkinter import *

root = Tk()
label = Label(root,text='Hello Python')
#label['text'] = 'Hello Tkinter' You Can Use All the .config in one line 
label.config(text='Hello Tkinter, Tkinter is Python GUI developing module.')
label.config(fg='red')#foreground color or text color
#label.config(bg='yellow')#backgroud color of label
label.config(wraplength='150')#wrap label text in pixels
label.config(font='Times 15')#Change Font and Font Size
label.config(justify=RIGHT)#Text Alignment 
label.pack()
root.geometry('300x250')
root.mainloop()
