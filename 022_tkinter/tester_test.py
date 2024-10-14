from tkinter import *
from tkinter import messagebox

root = Tk()

root.title('This is TKinter app.')
root.geometry('800x600')

def cliked():
    response = messagebox.askyesnocancel('Title', 'Message')
    if response == 1:
        Label(root, text='You clicked YES').pack()
    else:
        Label(root, text="You clicked NO").pack()

Button(root, text='Click me', command=cliked).pack()

root.mainloop()
