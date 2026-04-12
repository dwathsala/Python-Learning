import tkinter as tk

#create a window
root = tk.Tk()

width, height = 600, 600

display_width = root.winfo_screenwidth()
display_height = root.winfo_screenheight()

left = int(display_width/2 - width/2)
top = int(display_height/2 - height/2)

root.geometry(f'{width}x{height}+{left}+{top}') #width x height +let + top

root.title("Hello World")

# default we can resize the size of window -----> root.resizable(True, True)
#we can change it ----> root.resizable(True, False)
#we can change it ----> root.resizable(False, False)
root.resizable(False, False)

root.iconbitmap('')

#Run the window
root.mainloop() #Run this main loop contiuously and after close the window(gui), then after run the below things after mainloop.

print("Hello")

 