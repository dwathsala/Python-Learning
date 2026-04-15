import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Buttons")
root.geometry('300x200')

def button_func(num1, num2):
    sum = num1+num2
    answer.set(f'Answer is {sum}')

number1 = tk.IntVar()
number2 = tk.IntVar()
answer = tk.StringVar()

entry1 = ttk.Entry(root, textvariable=number1)
entry1.pack()

entry2 = ttk.Entry(root, textvariable=number2)
entry2.pack()

button = ttk.Button(root, text="Click Me", command=lambda: button_func(number1.get(), number2.get()))
button.pack()

label= ttk.Label(root, textvariable=answer)
label.pack()

root.mainloop()