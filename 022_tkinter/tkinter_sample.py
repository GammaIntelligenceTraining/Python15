# TKinter samples

from tkinter import *

def click():
    entered_text = textentry.get()
    output.delete(0.0, END)
    try:
        definition = my_dictionary[entered_text]
    except:
        definition = "Sorry, can't find " + entered_text + "\nTry again!"
    output.insert(END, definition)

def close_window():
    window.destroy()
    exit()

# Main window
window = Tk()

# Main window attributes
window.title('Tkinter samples')
window.configure(background='black')
# Adding pictures
photo1 = PhotoImage(file='python.png')
Label(window, image=photo1, bg='black').grid(row=0, column=0)

Label(window, text='Hello. This is a sample graphical interface made with Python and Tkinter library.', bg='black',
      fg='white', font='none 12 bold').grid(row=1, column=0, sticky=W)

textentry = Entry(window, width=20, bg='white')
textentry.grid(row=2, column=0, sticky=W)

Button(window, text='Submit', width=6, command=click).grid(row=3, column=0, sticky=W)

Label(window, text='\nDefinition:', bg='black', fg='white', font='none 12 bold').grid(row=4, column=0, sticky=W)

output = Text(window, width=75, height=6, wrap=WORD, background='white')
output.grid(row=5, column=0, sticky=W)

my_dictionary = {
    "one": "First line of a string", "two": "Second line of a string", "three": "Third line of a string"
}

Label(window, text='Click to exit', bg='black', fg='white', font='none 12 bold').grid(row=6, column=0, sticky=W)


Button(window, text='EXIT', width=14, command=close_window).grid(row=7, column=0, sticky=W)



# Main window loop
window.mainloop()