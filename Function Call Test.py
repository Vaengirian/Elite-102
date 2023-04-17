import tkinter
 
window_main = tkinter.Tk(className='Tkinter - TutorialKart')
window_main.geometry("400x200")
 
def submitFunction():
    print('Submit button is clicked.')

def sndfunction():
    print('2nd function successful')
 
button_submit = tkinter.Button(window_main, text ="Submit", command=lambda: [submitFunction(),sndfunction()])
button_submit.config(width=20, height=2)
 
button_submit.pack()
window_main.mainloop()