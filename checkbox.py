import tkinter as tk
from tkinter import ttk

root = tk.Tk()

root.title('Checkbox')
root.geometry('300x200')
root.resizable(False, False)

check1 = ttk.Checkbutton(root, text= 'python')
check1.pack()

check2 = ttk.Checkbutton(root, text='Java')
check2.pack()

root.mainloop()