import mysql.connector
import tkinter as tk
from tkinter import *
from tkinter import ttk
class App(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.pack(expand=1)
        
        frm = ttk.Frame(self, padding=10)
        frm.grid()
        ttk.Label(frm, text="Welcome to [Corporation Name]!").grid(column=0, row=0)
        ttk.Button(frm, text="Create account", command=root.destroy).grid(column=0, row=1)
        ttk.Button(frm, text="Log in",command=root.destroy).grid(column=0, row=2)
        #ttk.Button(frm, text="View", command=root.destroy).grid(column=0, row=2)
        #ttk.Button(frm, text="Deposit", command=root.destroy).grid(column=0, row=3)
        #ttk.Button(frm, text="Withdraw", command=root.destroy).grid(column=0, row=4)
        ttk.Button(frm, text="Quit", command=root.destroy).grid(column=0, row=3)

root = tk.Tk()
myapp = App(root)

#
# here are method calls to the window manager class
#
myapp.master.title("[Corporation Name]")
myapp.master.maxsize(1000, 400)

# start the program
myapp.mainloop()