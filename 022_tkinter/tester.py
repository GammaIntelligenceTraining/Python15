# from tkinter import *
# from tkinter import messagebox
#
# root = Tk()
#
# root.title('TKinter sample app')
# root.geometry('800x600')
# root.iconbitmap('python_icon.ico')
#
# v_var = IntVar()
# h_var = IntVar()
#
# vertical = Scale(root, from_=0, to=5)
# vertical.pack()
# horizontal = Scale(root, from_=0, to=5, orient=HORIZONTAL)
# horizontal.pack()
#
# Label(root, textvariable=v_var).pack()
# Label(root, textvariable=h_var).pack()
#
# Button(root, text='click', command=lambda: print(horizontal.get(), vertical.get())).pack()
#
# root.mainloop()



y = {'name': 'Jack', 'surname': 'Smith'}
x = {**y,'age': 25}

print(x)
