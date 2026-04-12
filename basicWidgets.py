import tkinter as tk
from tkinter import ttk

#ttk is better for widgets than tk

root = tk.Tk()

root.title('Basic Widgets')
root.geometry('300x200')
root.resizable(False,False)

'''old_button = tk.Button(root, text = 'Click Me')   #initialize the button
old_button.pack()  #Use to pack the button in window, That means display button in window '''

def button_click_func():
    entry_field_value = entry.get()
    label.configure(text = entry_field_value)
    button.configure(state='disabled')  #disable button after once click the button.
    print(entry_field_value)

entry = ttk.Entry(root)
entry.pack()

button = ttk.Button(root, text = 'Click Me', command=button_click_func)
button.pack()

label = ttk.Label(root)
label.pack()
#label.configure(text='Hello')

root.mainloop()