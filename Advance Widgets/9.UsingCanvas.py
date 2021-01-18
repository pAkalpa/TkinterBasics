from tkinter import *

root = Tk()

canvas = Canvas(root,width=650,height=550)
canvas.pack()
#line = canvas.create_line(100,250,360,25)
#canvas.itemconfigure(line,fill='red',width=10)
#line2 = canvas.create_line(25,50,150,150,250,140,fill='yellow',width=5)
#text = canvas.create_text(80,100,text='Hello Python',font=(('Times'),15,'bold'))
rect = canvas.create_rectangle(150,150,250,200,fill='green',width=5)
oval = canvas.create_oval(350,350,250,200)
arc = canvas.create_arc(120,20,30,80,fill='red',width=3,start=0,extent=180)
icon = PhotoImage(file='files/ytlogo.png')
image = canvas.create_image(150,200,image=icon)
canvas.lift(rect)

root.geometry('650x550+350+250')
root.mainloop()