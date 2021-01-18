from tkinter import *

root = Tk()
root.title('Frames')

frame = Frame(root,height=300,width=300,bg='red',bd=7,relief=SUNKEN)
frame.pack(fill=X)
btn1 = Button(frame,text='Button 1')
btn1.pack(side=LEFT,padx=20,pady=50)
btn2 = Button(frame,text='Button 2')
btn2.pack(side=LEFT,padx=20,pady=50)
searchbar = LabelFrame(root,text='Search Box',padx=20,pady=20,bg='#fcd45d')
lbl = Label(searchbar,text='Search',bg='#fcd45d')
lbl.pack(side=LEFT,padx=10)
searchbar.pack(side=TOP,padx=10)
entry = Entry(searchbar)
entry.pack(side=LEFT,padx=10)
btn3 = Button(searchbar,text='Search')
btn3.pack(side=LEFT,padx=10)

root.geometry('650x650+400+50')
root.mainloop()