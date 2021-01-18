from tkinter import *
from tkinter import ttk

root = Tk()

#------------------------------Widget Property---------------------------------------
ent1 = ttk.Entry(root,width=30)
ent2 = ttk.Entry(root,width=30)
ent1.insert(0,'Please Enter Your User Name')
ent2.insert(0,'Please Enter Your Password')
lblTitle = ttk.Label(text='XXX Login',font=(('Arial'),22))
btn1 = ttk.Button(root,text='Enter')
lblUN = ttk.Label(text='Your Name :',)
lblPW = ttk.Label(text='Your Password :')
#-------------------------------------------------------------------------------------

#----------------------------Layout Property------------------------------------------
lblTitle.grid(row=0,column=0,columnspan=2)
lblUN.grid(row=1,column=0,sticky=W)
lblPW.grid(row=2,column=0,sticky=W)
ent1.grid(row=1,column=1)
ent2.grid(row=2,column=1)#pady = y axis gap and padx = x axis gap
btn1.grid(row=3,column=1,sticky=E,pady=3)#E= east, W= west
#-------------------------------------------------------------------------------------
root.geometry('500x450')
root.mainloop()
