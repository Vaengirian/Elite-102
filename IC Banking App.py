import mysql.connector
import tkinter as tk
from tkinter import *
connection = mysql.connector.connect(user = 'modbankapp', database = 'bankapp', password = 'M3k5!tsr693^')
cursor = connection.cursor()
class App(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.pack(expand=1)
        label1 = tk.Label(root2, text="Welcome to [Corporation Name]!")
        label1.pack()
        caccount = tk.Button(root2, text="Create account", command=root2.destroy)
        caccount.pack()
        logine = tk.Button(root2, text="Log in",command=App.logininterface)
        logine.pack()
        #ttk.Button(frm, text="View", command=root.destroy).grid(column=0, row=2)
        #ttk.Button(frm, text="Deposit", command=root.destroy).grid(column=0, row=3)
        #ttk.Button(frm, text="Withdraw", command=root.destroy).grid(column=0, row=4)
        quite = tk.Button(root2, text="Quit", command=App.connectionsever)
        quite.pack()
        #a button
        #ttk.Button(frm, text="a", command=Appfunction.a).grid(column=0, row=4)
    def connectionsever():
        cursor.close()
        connection.close()
        root2.destroy()
    def createaccount():
        bankusername = input("Enter a username\n") #transfer to tkinter window somehow
        bankpassword = input("Enter a password\n") #transfer to tkinter window somehow (widgets)
    def printInput(text):
        inp = text.get(1.0, "end-1c")
        print(inp)
        print('d')
    def logininterface():
        #root2.geometry('600x250') #geometry restructure
        for widgets in root2.winfo_children(): #deletes all widgets
            widgets.destroy()
        inputtxt = tk.Text(root2,height = 5,width = 20)
        inputtxt.pack()
        printButton = tk.Button(root2, text = "Print", command = lambda: App.printInput(inputtxt))
        printButton.pack()
root2 = tk.Tk()
root2.geometry('1000x400')
myapp = App(root2)
#
# here are method calls to the window manager class
#
myapp.master.title("[Corporation Name]")
myapp.master.maxsize(1000, 400)

# start the program
myapp.mainloop()