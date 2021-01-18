from tkinter import *
from tkinter import ttk

root = Tk()

def tView(event):
    """
    tree view bind
    """
    item = treeView.identify('item',event.x,event.y)
    print('You Clicked on {}'.format(treeView.item(item,'text')))

treeView = ttk.Treeview(root)
treeView.pack()

treeView.insert('','0','item1',text='First Item')
treeView.insert('','1','item2',text='Second Item')
treeView.insert('','2','item3',text='Third Item')
treeView.insert('','3','item4',text='Forth Item')
treeView.move('item2','item1','end')
treeView.bind('<Double-1>',tView)

root.geometry('650x450+350+250')
root.mainloop()