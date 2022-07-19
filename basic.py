from tkinter import *
from tkinter import messagebox as m
root=Tk()
root.geometry("600x300")
root.title("cpp")
def out():

    print("hello")
    label = Label(text="HEllo").pack()
    m.askyesno("this is message box,  ", "what do you want?")




button=Button(text="cricket",command=out)
#button1=Button(text="this ")
button.pack()
root.mainloop()