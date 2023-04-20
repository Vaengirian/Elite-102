import mysql.connector
import tkinter as tk
from tkinter import *
connection = mysql.connector.connect(user = 'modbankapp', database = 'bankapp', password = 'M3k5!tsr693^')
cursor = connection.cursor()
connection.autocommit = True
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
    def connectionsever(): #quit program
        cursor.close()
        connection.close()
        root2.destroy()
    def createaccount(): #make account
        bankusername = input("Enter a username\n") #transfer to tkinter window somehow
        bankpassword = input("Enter a password\n") #transfer to tkinter window somehow (widgets)
    def printInput(text): #input getter for all text boxes
        #global inp #GLOBAL VARIABLE HERE
        inp = text.get(1.0, "end-1c")
        return inp
    def logininterface(): #login window code
        #root2.geometry('600x250') #geometry restructure
        inplist=[]
        for widgets in root2.winfo_children(): #deletes all widgets
            widgets.destroy()
        inputtxt = tk.Text(root2,height = 1,width = 45)
        inputtxt.pack()
        inputtxt2 = tk.Text(root2,height=1, width = 45)
        inputtxt2.pack()
        userButton = tk.Button(root2, text = "Login", command = lambda: [inplist.extend([(App.printInput(inputtxt),App.printInput(inputtxt2))]),App.login(inplist)])
        userButton.pack()
    def login(ilist):
        datalist=[]
        userQuery = ("SELECT Username, Userpassword FROM user_information")
        cursor.execute(userQuery)
        for item in cursor:
            datalist.append(item)
        if ilist == datalist:
            print('successful')
        print(datalist)
        print(ilist)

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