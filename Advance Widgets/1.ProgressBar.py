from tkinter import *
from tkinter import ttk

root = Tk()

progBar = ttk.Progressbar(root,orient=HORIZONTAL,length=200)
progBar.pack(pady=20)
progBar.config(mode='indeterminate')
progBar.start()
progBar.stop()
progBar.config(mode='determinate',maximum=50.0)
progBar.start()
progBar.stop()
val = DoubleVar()
progBar.config(variable=val)
scale = ttk.Scale(root,orient=HORIZONTAL,length=200,from_=0.0,to=50.0,variable=val)
scale.pack()

root.geometry('450x450+650+350')
root.mainloop()