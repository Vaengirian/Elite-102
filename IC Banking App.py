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
        App.firstmenu()
    def firstmenu():
        for widgets in root2.winfo_children(): #deletes all widgets
            widgets.destroy()
        label1 = tk.Label(root2, text="Welcome to [Corporation Name]!")
        label1.pack()
        caccount = tk.Button(root2, text="Create account", command=lambda: App.createaccountmenu())
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
    def createaccountmenu(): #make account
        clist = []
        for widgets in root2.winfo_children(): #deletes all widgets
            widgets.destroy()
        clabel = tk.Label(root2, text="Enter Desired Username")
        clabel.pack()
        cinputtxt = tk.Text(root2,height = 1,width = 45)
        cinputtxt.pack()
        clabel = tk.Label(root2, text="Enter Desired Password")
        clabel.pack()
        cinputtxt2 = tk.Text(root2,height=1, width = 45)
        cinputtxt2.pack()
        cserButton = tk.Button(root2, text = "Confirm", command = lambda: [clist.extend([App.printInput(cinputtxt),App.printInput(cinputtxt2)]),App.createaccount(clist)])
        cserButton.pack()
        Backe = tk.Button(root2, text="Back", command=App.firstmenu)
        Backe.pack()
    def createaccount(clist):
        for widgets in root2.winfo_children(): #deletes all widgets
            widgets.destroy()
        idlist = []
        print(clist)
        adQuery = ("SELECT Userid FROM user_information ORDER BY Userid DESC LIMIT 1")
        cursor.execute(adQuery)
        for item in cursor:
            for it in item:
                idlist.append(it)
        newid = idlist[0] + 1
        cuple = (newid,clist[0],clist[1])
        addquery = ("INSERT INTO user_information (Userid, Username, Userpassword) VALUES (%s,%s,%s)")
        cursor.execute(addquery, cuple)
        cuple2 = (newid, 0)
        aidquery = ("INSERT INTO userbalance (accountid, accountbalance) VALUES (%s,%s)")
        cursor.execute(aidquery, cuple2)
        print("successful")
        Backe = tk.Button(root2, text="Back", command=App.firstmenu)
        Backe.pack()
    def printInput(text): #input getter for all text boxes
        #global inp #GLOBAL VARIABLE HERE
        inp = text.get(1.0, "end-1c")
        return inp
    def logininterface(): #login window code
        #root2.geometry('600x250') #geometry restructure
        inplist=[]
        for widgets in root2.winfo_children(): #deletes all widgets
            widgets.destroy()
        label2 = tk.Label(root2, text="Username")
        label2.pack()
        inputtxt = tk.Text(root2,height = 1,width = 45)
        inputtxt.pack()
        label3 = tk.Label(root2, text="Password")
        label3.pack()
        inputtxt2 = tk.Text(root2,height=1, width = 45)
        inputtxt2.pack()
        userButton = tk.Button(root2, text = "Login", command = lambda: [inplist.extend([App.printInput(inputtxt),App.printInput(inputtxt2)]),App.login(inplist)])
        userButton.pack()
        Backe = tk.Button(root2, text="Back", command=App.firstmenu)
        Backe.pack()
        quite = tk.Button(root2, text="Quit", command=App.connectionsever)
        quite.pack()
    def login(ilist): #actually logs in
        datalist=[]
        userQuery = ("SELECT Username, Userpassword FROM user_information WHERE Username = %s")
        ulist=[]
        ulist.append(ilist[0])
        cursor.execute(userQuery, ulist)
        for item in cursor:
            for it in item:
                datalist.append(it)
                print(it)
        if ilist == datalist:
            print('successful')
            App.userinterface(ilist)
        #print(datalist)
        #print(ilist[0])
    def userinterface(inlist): #brings up new interface with view, withdraw, deposit, quit, delete (quit but removes dataset)
        #print(inlist[0])
        for widgets in root2.winfo_children(): #deletes all widgets
            widgets.destroy()
        ulist2=[]
        idlist1 = []
        ulist2.append(inlist[0])
        accountQuery = ("SELECT Userid FROM user_information WHERE Username = %s")
        cursor.execute(accountQuery,ulist2)
        for item in cursor:
            for it in item:
                idlist1.append(it)
                print(it)
        ViewButton = tk.Button(root2, text="View", command=lambda: App.view(idlist1,inlist))
        ViewButton.pack()
        DepositButton = tk.Button(root2, text="Deposit", command=lambda: App.depositmenu(idlist1,inlist))
        DepositButton.pack()
        WithdrawButton = tk.Button(root2, text="Withdraw", command=lambda: App.withdrawmenu(idlist1,inlist))
        WithdrawButton.pack()
        DeleteButton = tk.Button(root2, text="Delete", command=lambda: App.deletemenu(idlist1,inlist))
        DeleteButton.pack()
        Backe = tk.Button(root2, text="Back", command=App.firstmenu)
        Backe.pack()
        quite = tk.Button(root2, text="Quit", command=App.connectionsever)
        quite.pack()
        
    def view(idlist1,inlist): #view balance
        balist = []
        for widgets in root2.winfo_children(): #deletes all widgets
            widgets.destroy()
        balanceQuery = ("SELECT accountbalance FROM userbalance WHERE accountid = %s")
        cursor.execute(balanceQuery,idlist1)
        for item in cursor:
            for it in item:
                balist.append(it)
        viewstr = 'Username =' + inlist[0] + '\nPassword =' + inlist[1] + '\nId = ' + str(idlist1[0]) + '\nBalance = $' + str(balist[0]) #tester terminal code
        label4 = tk.Label(root2, text=viewstr)
        label4.pack()
        Backe = tk.Button(root2, text="Back", command=lambda: App.userinterface(inlist))
        Backe.pack()
    def depositmenu(idlist1,inlist): #deposit money menu
        dlist = []
        for widgets in root2.winfo_children(): #deletes all widgets
            widgets.destroy()
        label = tk.Label(root2, text="Please enter amount to deposit")
        label.pack()
        inputtxt = tk.Text(root2,height = 1,width = 45)
        inputtxt.pack()
        dButton = tk.Button(root2, text = "Enter", command = lambda: [dlist.append(App.printInput(inputtxt)),App.deposit(idlist1, dlist,inlist)])
        dButton.pack()
        Backe = tk.Button(root2, text="Back", command=lambda: App.userinterface(inlist))
        Backe.pack()
    def deposit(idlist1, deplist,inlist): #actual deposit
        for widgets in root2.winfo_children(): #deletes all widgets
            widgets.destroy()
        balist = []
        balanceQuery = ("SELECT accountbalance FROM userbalance WHERE accountid = %s") #(defunct code may remove)
        cursor.execute(balanceQuery,idlist1)
        for item in cursor:
            for it in item:
                balist.append(it)
        f1 = float(deplist[0])
        total = balist[0] 
        total += f1
        tuple1 = (total,idlist1[0])
        epoupdate = ("UPDATE userbalance SET accountbalance = %s WHERE accountid = %s")
        cursor.execute(epoupdate, tuple1)
        #print(total)
        dstr = "Deposit Successful, your new balance is: $" + str(total)
        label5 = tk.Label(root2, text=dstr)
        label5.pack()
        Backe = tk.Button(root2, text="Back", command=lambda: App.userinterface(inlist))
        Backe.pack()
    def withdrawmenu(idlist1,inlist): #withdraw money menu
        dlist = []
        for widgets in root2.winfo_children(): #deletes all widgets
            widgets.destroy()
        label = tk.Label(root2, text="Please enter amount to withdraw")
        label.pack()
        inputtxt = tk.Text(root2,height = 1,width = 45)
        inputtxt.pack()
        dButton = tk.Button(root2, text = "Enter", command = lambda: [dlist.append(App.printInput(inputtxt)),App.withdraw(idlist1, dlist,inlist)])
        dButton.pack()
        Backe = tk.Button(root2, text="Back", command=lambda: App.userinterface(inlist))
        Backe.pack()
    def withdraw(idlist1, deplist,inlist): #actual withdraw
        for widgets in root2.winfo_children(): #deletes all widgets
            widgets.destroy()
        balist = []
        balanceQuery = ("SELECT accountbalance FROM userbalance WHERE accountid = %s") #(defunct code may remove)
        cursor.execute(balanceQuery,idlist1)
        for item in cursor:
            for it in item:
                balist.append(it)
        f1 = float(deplist[0])
        total = balist[0] 
        total -= f1
        tuple1 = (total,idlist1[0])
        epoupdate = ("UPDATE userbalance SET accountbalance = %s WHERE accountid = %s")
        cursor.execute(epoupdate, tuple1)
        #print(total)
        wstr = "Withdrawal Successful, your new balance is: $" + str(total)
        label5 = tk.Label(root2, text=wstr)
        label5.pack()
        Backe = tk.Button(root2, text="Back", command=lambda: App.userinterface(inlist))
        Backe.pack()
    def deletemenu(idlist1, inlist):
        for widgets in root2.winfo_children(): #deletes all widgets
            widgets.destroy()
        #idlist2 = [] measure1
        #idlist2 = idlist1
        #deletequery = "DELETE FROM user_information WHERE Userid = %s"
        #cursor.execute(deletequery, idlist1)
        #deletequery = "DELETE FROM userbalance WHERE accountid = %s"
        #cursor.execute(deletequery, idlist1)
        duple = (None, idlist1[0])
        deletequery = ("UPDATE user_information SET Username = %s WHERE Userid = %s")
        cursor.execute(deletequery, duple)
        deletequery2 = ("UPDATE user_information SET Userpassword = %s WHERE Userid = %s")
        cursor.execute(deletequery2, duple)
        deletequery3 = ("UPDATE userbalance SET accountbalance = %s WHERE accountid = %s")
        cursor.execute(deletequery3, duple)
        dstr = "Deletion Successful"
        dlabel5 = tk.Label(root2, text=dstr)
        dlabel5.pack()
        quite = tk.Button(root2, text="Quit", command=App.connectionsever)
        quite.pack()
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