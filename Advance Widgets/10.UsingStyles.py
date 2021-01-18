from tkinter import *
from tkinter import ttk
from ttkthemes import themed_tk as tk

root = tk.ThemedTk()
root.get_themes()
root.set_theme('yaru')

text_nme = ttk.Label(root,text='Name :').grid(row=0,column=0,pady=20)
text_snme = ttk.Label(root,text='Surname :').grid(row=1,column=0)
text_msg = ttk.Label(root,text='Message :')
input_nme = ttk.Entry(root,width=30)
input_snme = ttk.Entry(root,width=30)
input_nme.insert(0,'Please Enter Your Name')
input_snme.insert(0,'Please Enter Your Surname')
input_nme.grid(row=0,column=1)
input_snme.grid(row=1,column=1)
ttk.Radiobutton(root,text='Male',value='Male').grid(row=2,column=1,sticky=E,pady=15)
ttk.Radiobutton(root,text='Female',value='Female').grid(row=2,column=1)
msgText = Text(root,width=25,height=15,wrap=WORD).grid(row=3,column=1)
btn1 = ttk.Button(root,text='Send',width=10).grid(row=4,column=1,sticky=W)
btn2 = ttk.Button(root,text='Clear',width=10).grid(row=4,column=1,sticky=E)

root.geometry('400x550+350+250')
root.mainloop()