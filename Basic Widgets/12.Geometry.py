from tkinter import *

root = Tk()

titl = Label(root,text='Place Geometry Manager',font=(('Verdana'),15))
un_txt = Label(root,text='Name :')
pw_txt = Label(root,text='Password :')
un_ent = Entry(root,width=30)
pw_ent = Entry(root,width=30)
btn1 = Button(root,text='Save')
btn2 = Button(root,text='Click Me',bg='red')

titl.place(x=100,y=20)
un_txt.place(x=20,y=80)
pw_txt.place(x=20,y=110)
un_ent.place(x=100,y=80)
pw_ent.place(x=100,y=110)
btn1.place(x=250,y=140)
btn2.place(relx=0.5,rely=0.5,anchor='center')

root.geometry('450x450+650+350')#650+350 means location of window in main screen
root.mainloop()