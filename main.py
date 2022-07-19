import tkinter
from tkinter import messagebox
from tkinter.filedialog import askopenfile

import cv2 # used to display video
import win32com.client as wincl #used for voice
import PIL.Image, PIL.ImageTk #Used to display image
from functools import partial #speed control
import threading #images display
import imutils
import time #time stamp

from tkVideoPlayer import TkinterVideo #browse and copy video

root = tkinter.Tk()
SET_WIDTH = 830
SET_HEIGHT = 600
root.geometry("830x600")

root.title("Home page of project")

var = tkinter.IntVar()
var.set(11)
stream = cv2.VideoCapture("lowCatch.mp4")
stream1 = cv2.VideoCapture("runout.mp4")
stream2 = cv2.VideoCapture("stum.mp4")
stream4 = cv2.VideoCapture("lbw1.mp4")
def open_file():#browse video from file
    file = askopenfile(mode='r', filetypes=[
        ('Video Files', ["*.mp4"])])
    if file is not None:
        global filename
        filename = file.name
        global videoplayer
        global flag
        videoplayer = TkinterVideo(master=root,width=650, height=368,scaled=True, pre_load=False)
        videoplayer.load(r"{}".format(filename))
        videoplayer.pack( side="right",fill="x",pady=23,padx=56)
        videoplayer.play()
def thank():
    speak = wincl.Dispatch("SAPI.SpVoice")
    speak.Speak("thank you for using this software This project is made by ABDUL sushant rohit samarth nikhil")
    root.destroy()


def help():
    speak = wincl.Dispatch("SAPI.SpVoice")
    speak.Speak("please select any button and then click on Check now button ")

    messagebox.showinfo("How to use this application", "First click on any of the options you want to check ")


with open("facts.txt", "a") as f:
    f.write(
        "1. Sanath Jayasuriya has more ODI wickets than Shane Warne.\n\n2. The highest number of runs scored in an over is not 36. It’s 77\n\n3. On 12 th January 1964, Indian spinner Bapu Nadkarni bowled 21 consecutive maiden overs vs England at Chennai.\n\n4. In a World Cup Match, chasing 335, Sunil Gavaskar scored an unbeaten 36 off 174 balls.\n\n5.  Mahela Jayawardene is the only batsman to have scored centuries in both the Semi-Final and Final of a World Cup.\n\n 6. Inzamam Ul Haq took a wicket off the very first ball he bowled in International Cricket.\n\n7. Sachin Tendulkar got out for a duck only once in his Ranji career. Bhuvaneshwar Kumar got him.\n\n8. Saeed Ajmal has never won a Man of the Match award in One Day International Cricket.")


def submit():
    speak = wincl.Dispatch("SAPI.SpVoice")
    speak.Speak("welcome to decision review  system  ")

    def facts():
        speak = wincl.Dispatch("SAPI.SpVoice")
        speak.Speak("these are the some intersting facts ")
        messagebox.showinfo("Some of the intresting facts",
                            "1. Sanath Jayasuriya has more ODI wickets than Shane Warne.\n\n2. The highest number of runs scored in an over is not 36. It’s 77\n\n3. On 12 th January 1964, Indian spinner Bapu Nadkarni bowled 21 consecutive maiden overs vs England at Chennai.\n\n4. In a World Cup Match, chasing 335, Sunil Gavaskar scored an unbeaten 36 off 174 balls.\n\n5.  Mahela Jayawardene is the only batsman to have scored centuries in both the Semi-Final and Final of a World Cup.\n\n 6. Inzamam Ul Haq took a wicket off the very first ball he bowled in International Cricket.\n\n7. Sachin Tendulkar got out for a duck only once in his Ranji career. Bhuvaneshwar Kumar got him.\n\n8. Saeed Ajmal has never won a Man of the Match award in One Day International Cricket.")

    def play(speed):
        if var.get() == 1:

            print(f"you clicked on out.speed is{speed}")
            frame = stream.get(cv2.CAP_PROP_POS_FRAMES)
            stream.set(cv2.CAP_PROP_POS_FRAMES, frame + speed)
            grabbed, frame = stream.read()
            frame = imutils.resize(frame, width=900, height=SET_HEIGHT)
            frame = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(frame))
            cv.image = frame
            cv.create_image(0, 0, image=frame, anchor=tkinter.NW)
        elif var.get() == 2:
            print(f"you clicked on out.speed is{speed}")
            frame1 = stream1.get(cv2.CAP_PROP_POS_FRAMES)
            stream1.set(cv2.CAP_PROP_POS_FRAMES, frame1 + speed)
            grabbed, frame = stream1.read()
            frame = imutils.resize(frame, width=900, height=SET_HEIGHT)
            frame = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(frame))
            cv.image = frame
            cv.create_image(0, 0, image=frame, anchor=tkinter.NW)
        elif var.get() == 3:
            print(f"you clicked on out.speed is{speed}")
            frame1 = stream2.get(cv2.CAP_PROP_POS_FRAMES)
            stream2.set(cv2.CAP_PROP_POS_FRAMES, frame1 + speed)
            grabbed, frame = stream2.read()
            frame = imutils.resize(frame, width=900, height=SET_HEIGHT)
            frame = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(frame))
            cv.image = frame
            cv.create_image(0, 0, image=frame, anchor=tkinter.NW)
        elif var.get() == 4:
            print(f"you clicked on out.speed is{speed}")
            frame1 = stream4.get(cv2.CAP_PROP_POS_FRAMES)
            stream4.set(cv2.CAP_PROP_POS_FRAMES, frame1 + speed)
            grabbed, frame = stream4.read()
            frame = imutils.resize(frame, width=900, height=SET_HEIGHT)
            frame = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(frame))
            cv.image = frame
            cv.create_image(0, 0, image=frame, anchor=tkinter.NW)

    def pending(decision):
        frame = cv2.cvtColor(cv2.imread("pending.png"), cv2.COLOR_BGR2RGB)
        frame = imutils.resize(frame, width=900, height=SET_HEIGHT)
        frame = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(frame))
        cv.image = frame
        cv.create_image(0, 0, image=frame, anchor=tkinter.NW)
        # waiting for 1 seccond
        time.sleep(1)

        frame = cv2.cvtColor(cv2.imread("sponsor.png"), cv2.COLOR_BGR2RGB)
        frame = imutils.resize(frame, width=900, height=SET_HEIGHT)
        frame = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(frame))
        cv.image = frame
        cv.create_image(0, 0, image=frame, anchor=tkinter.NW)
        time.sleep(1)
        speak = wincl.Dispatch("SAPI.SpVoice")
        speak.Speak("this project is sponsored from Bhandari Sports club ")
        # display out or not out image
        if decision == "out":

            decisionImg = "out.png"
            speak = wincl.Dispatch("SAPI.SpVoice")
            speak.Speak("the   batsman is out")
        else:
            decisionImg = "not_out.png"
            speak = wincl.Dispatch("SAPI.SpVoice")
            speak.Speak("the  batsman is not out")

        frame = cv2.cvtColor(cv2.imread(decisionImg), cv2.COLOR_BGR2RGB)
        frame = imutils.resize(frame, width=900, height=SET_HEIGHT)
        frame = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(frame))
        cv.image = frame
        cv.create_image(0, 0, image=frame, anchor=tkinter.NW)

    def out():
        thread = threading.Thread(target=pending, args=("out",))
        thread.daemon = 1
        thread.start()
        print("Player is out")

    def not_out():
        thread = threading.Thread(target=pending, args=("not out",))
        thread.daemon = 1
        thread.start()
        print("player is not out")

    # Tkinter gui starts here
    window = tkinter.Toplevel()
    window.geometry("830x830")
    window.title("Decision Review System ")

    window.configure(bg="light blue")#background light
    cv = tkinter.Canvas(window, height=500, width=830, bg="black", bd=0)
    img = PIL.ImageTk.PhotoImage(file="wel.png")

    cv.create_image(0, 0, anchor=tkinter.NW, image=img)
    cv.place(x=0, y=0)


    if var.get() == 1:
        print("Low catch dekhna hai")
        btn = tkinter.Button(window, text="<< Previous (fast)", bg="DarkOliveGreen2", command=partial(play, -15),
                             font="verdana 13 bold", width=35)
        btn.place(x=200, y=470)

        btn = tkinter.Button(window, text="<< Previous (slow)", bg="DarkOliveGreen2", command=partial(play, -2),
                             font="verdana 13 bold", width=35)
        btn.place(x=200, y=500)

        btn = tkinter.Button(window, text="Next (slow) >>", bg="DarkOliveGreen2", command=partial(play, 2),
                             font="verdana 13 bold", width=35)
        btn.place(x=200, y=530)

        btn = tkinter.Button(window, text="Next (fast) >>", bg="DarkOliveGreen2", command=partial(play, 25),
                             font="verdana 13 bold", width=35)
        btn.place(x=200, y=560)

        btn = tkinter.Button(window, text="Give Out", command=out, bg="DarkOliveGreen2", font="verdana 13 bold",
                             width=35)
        btn.place(x=200, y=590)

        btn = tkinter.Button(window, text="Give Not Out", bg="DarkOliveGreen2", command=not_out, font="verdana 13 bold",
                             width=35)
        btn.place(x=200, y=620)
        btn = tkinter.Button(window, text="Facts", bg="chocolate1", command=facts, padx=11, pady=12)
        btn.place(x=770, y=600)

        window.mainloop()
    elif var.get() == 2:
        print("run out dekhna hai")
        btn = tkinter.Button(window, text="<< Previous (fast)", bg="DarkOliveGreen2", command=partial(play, -15),
                             font="verdana 13 bold", width=35)
        btn.place(x=200, y=470)

        btn = tkinter.Button(window, text="<< Previous (slow)", bg="DarkOliveGreen2", command=partial(play, -2),
                             font="verdana 13 bold", width=35)
        btn.place(x=200, y=500)

        btn = tkinter.Button(window, text="Next (slow) >>", bg="DarkOliveGreen2", command=partial(play, 2),
                             font="verdana 13 bold", width=35)
        btn.place(x=200, y=530)

        btn = tkinter.Button(window, text="Next (fast) >>", bg="DarkOliveGreen2", command=partial(play, 25),
                             font="verdana 13 bold", width=35)
        btn.place(x=200, y=560)

        btn = tkinter.Button(window, text="Give Out", command=out, bg="DarkOliveGreen2", font="verdana 13 bold",
                             width=35)
        btn.place(x=200, y=590)

        btn = tkinter.Button(window, text="Give Not Out", bg="DarkOliveGreen2", command=not_out, font="verdana 13 bold",
                             width=35)
        btn.place(x=200, y=620)
        btn = tkinter.Button(window, text="Facts", bg="chocolate1", command=facts, padx=11, pady=12)
        btn.place(x=770, y=600)

        window.mainloop()
    elif var.get() == 3:
        print("Stump out dekhna hai")
        btn = tkinter.Button(window, text="<< Previous (fast)", bg="DarkOliveGreen2", command=partial(play, -15),
                             font="verdana 13 bold", width=35)
        btn.place(x=200, y=470)

        btn = tkinter.Button(window, text="<< Previous (slow)", bg="DarkOliveGreen2", command=partial(play, -2),
                             font="verdana 13 bold", width=35)
        btn.place(x=200, y=500)

        btn = tkinter.Button(window, text="Next (slow) >>", bg="DarkOliveGreen2", command=partial(play, 2),
                             font="verdana 13 bold", width=35)
        btn.place(x=200, y=530)

        btn = tkinter.Button(window, text="Next (fast) >>", bg="DarkOliveGreen2", command=partial(play, 25),
                             font="verdana 13 bold", width=35)
        btn.place(x=200, y=560)

        btn = tkinter.Button(window, text="Give Out", command=out, bg="DarkOliveGreen2", font="verdana 13 bold",
                             width=35)
        btn.place(x=200, y=590)

        btn = tkinter.Button(window, text="Give Not Out", bg="DarkOliveGreen2", command=not_out, font="verdana 13 bold",
                             width=35)
        btn.place(x=200, y=620)
        btn = tkinter.Button(window, text="Facts", bg="chocolate1", command=facts, padx=11, pady=12)
        btn.place(x=770, y=600)

        window.mainloop()
    elif var.get() == 4:
        print("LBW dekhna hai")
        btn = tkinter.Button(window, text="<< Previous (fast)", bg="DarkOliveGreen2", command=partial(play, -25),
                             font="verdana 13 bold", width=35)
        btn.place(x=200, y=470)

        btn = tkinter.Button(window, text="<< Previous (slow)", bg="DarkOliveGreen2", command=partial(play, -2),
                             font="verdana 13 bold", width=35)
        btn.place(x=200, y=500)

        btn = tkinter.Button(window, text="Next (slow) >>", bg="DarkOliveGreen2", command=partial(play, 2),
                             font="verdana 13 bold", width=35)
        btn.place(x=200, y=530)

        btn = tkinter.Button(window, text="Next (fast) >>", bg="DarkOliveGreen2", command=partial(play, 25),
                             font="verdana 13 bold", width=35)
        btn.place(x=200, y=560)

        btn = tkinter.Button(window, text="Give Out", command=out, bg="DarkOliveGreen2", font="verdana 13 bold",
                             width=35)
        btn.place(x=200, y=590)

        btn = tkinter.Button(window, text="Give Not Out", bg="DarkOliveGreen2", command=not_out, font="verdana 13 bold",
                             width=35)
        btn.place(x=200, y=620)
        btn = tkinter.Button(window, text="Facts", command=facts, bg="chocolate1", padx=11, pady=12)
        btn.place(x=770, y=600)
        window.mainloop()


# var = IntVar()
var.set(11)
c = tkinter.Canvas(root, height=600, width=830, bg="black", bd=0)
img = PIL.ImageTk.PhotoImage(file="mama.png")


c.create_image(0, 0, anchor=tkinter.NW, image=img)

c.place(x=0, y=0)

tkinter.Label(root, text="What do you want to check?", bg="yellow", font="corba 19 bold", padx=14).place(x=250, y=80)
tkinter.Radiobutton(root, text="Low catch", padx=14, variable=var, value=1, font="sanserif 13 bold").place(x=350, y=130)
tkinter.Radiobutton(root, text="Run out", padx=14, variable=var, value=2, font="sanserif 13 bold").place(x=350, y=180)
tkinter.Radiobutton(root, text="Stump out", padx=14, variable=var, value=3, font="sanserif 13 bold").place(x=350, y=230)
tkinter.Radiobutton(root, text="LBW", padx=14, variable=var, value=4, font="sanserif 13 bold").place(x=350, y=280)
tkinter.Button(text="Check Now", command=submit, activebackground='green', highlightcolor='yellow', bd=3, bg='black',
               fg='white', font=('Megrim', 20, 'bold'), relief='raised', height=1, width=15).place(x=300, y=370)
tkinter.Button(text="Exit", command=thank, borderwidth=5, padx=15, pady=10, bg="yellow", fg="black").place(x=13,
                                                                                                                  y=500)
tkinter.Button(text="Help", borderwidth=5, padx=15, pady=10, bg="pink", fg="black", command=help).place(x=750, y=489)
file= tkinter.Menu(root)
m1=tkinter.Menu(file,tearoff=0)
#m1.add_command(label="Delete",command=delete)
#m1.add_command(label="Save",command=save)
m1.add_command(label="browse",command=open_file)
m1.add_command(label="delete ",command=open_file)
#m1.add_command(label="check",command=broswevideo)
file.add_cascade(menu=m1,label="File")
root.config(menu=file)
root.mainloop()


