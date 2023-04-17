import tkinter as tk
from tkinter import *
from tkinter import ttk
class Demo1:
    def __init__(self, master):
        self.master = master
        self.frame = tk.Frame(self.master)
        self.HelloButton = tk.Button(self.frame, text = 'Hello', width = 25, command = self.new_window,)
        self.HelloButton.pack()
        self.frame.pack()
    def close_windows(self):
        self.master.destroy()
        self.new_window

    def new_window(self):
        self.master.destroy() # close the current window
        self.master = tk.Tk() # create another Tk instance
        self.app = Demo2(self.master) # create Demo2 window
        self.master.mainloop()
class Demo2:
    def __init__(self, master):
        self.master = master
        self.frame = tk.Frame(self.master)
        self.quitButton = tk.Button(self.frame, text = 'Quit', width = 25, command = self.close_windows)
        self.quitButton.pack()
        self.frame.pack()
    def close_windows(self):
        self.master.destroy()

def main(): 
    root = tk.Tk()
    app = Demo1(root)
    root.mainloop()

if __name__ == '__main__':
    main()
    