from tkinter import *
from tkinter import ttk
from typing import Collection

root = Tk()

#-----------------------------Logic---------------------------------------------------
chVar = IntVar()
chVar.set(0)
gender = StringVar()
months = StringVar()
numbers = []
year = StringVar()

for i in range(1,13):
    numbers.append(i)

def callEntr():
    """
    Enter Button Logic
    """
    print('Your Name :'+ent1.get())
    print('Your Password :'+ent2.get())
    print('Gender :'+gender.get())
    print('Month :'+months.get())
    print('Year :'+year.get())
    if chVar.get() == 1:
        print('Remember Me Selected!')
    else:
        print('Not Selected')
#-------------------------------------------------------------------------------------

#------------------------------Widget Property---------------------------------------
ent1 = ttk.Entry(root,width=30)
ent2 = ttk.Entry(root,width=30)
ent1.insert(0,'Please Enter Your User Name')
ent2.insert(0,'Please Enter Your Password')
lblTitle = ttk.Label(text='XXX Login',font=(('Arial'),22))
btn1 = ttk.Button(root,text='Enter',command=callEntr)
lblUN = ttk.Label(text='Your Name :',)
lblPW = ttk.Label(text='Your Password :')
chBox = Checkbutton(root,text='Remember Me!',variable=chVar,font=(('Arial'),16))
gradBtn = ttk.Radiobutton(root,text='Male',value='Male',variable=gender).grid(row=5,column=1,sticky=W)
gradBtn = ttk.Radiobutton(root,text='Female',value='Female',variable=gender).grid(row=5,column=1,sticky=E)
#comboBox = ttk.Combobox(root,textvariable=months,values=('Jan','Feb','Mar','Apr'),state='readonly')
comboBox = ttk.Combobox(root,textvariable=months,values=(numbers),state='readonly')
spinBox = ttk.Spinbox(root,from_=1990,to=2021,textvariable=year,state='readonly')
#-------------------------------------------------------------------------------------

#----------------------------Layout Property------------------------------------------
lblTitle.grid(row=0,column=0,columnspan=2)
lblUN.grid(row=1,column=0,sticky=W)
lblPW.grid(row=2,column=0,sticky=W)
ent1.grid(row=1,column=1,pady=2)
ent2.grid(row=2,column=1,pady=2)#pady = y axis or verticle gap and padx = x axis or horizontal gap
btn1.grid(row=3,column=1,sticky=E,pady=3)#E= east, W= west
chBox.grid(row=4,column=0,sticky=E,columnspan=2)
comboBox.grid(row=6,column=0)
spinBox.grid(row=7,column=1)
#-------------------------------------------------------------------------------------
root.geometry('500x450')
root.mainloop()
