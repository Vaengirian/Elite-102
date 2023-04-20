from tkinter import *
from tkinter import ttk
root = Tk()
frm = ttk.Frame(root, padding=10)
frm.grid()
ttk.Label(frm, text="Welcome to [Corporation Name]!").grid(column=0, row=0)
ttk.Button(frm, text="Quit", command=root.destroy).grid(column=0, row=1)
root.mainloop()

callables = []
for i in (1, 2, 3):
    callables.append(lambda a=i: a)

for f in callables:
    print(f())