from tkinter import *
import tkinter as tk
import tkinter.font as tkFont

app = Tk()
app.title("Cps counter")
app.geometry('400x400')
app.resizable(False,False)
app.config(bg='#696969')

time_allowed = 5

raw = 0
cps = 0
timer = 5
i = "once"

def click():
    global i
    if i == "once":
        update()
        i = "runned once"

    global raw
    if timer != 0: 
        raw += 1

def update():
    global timer
    global cps
    timer -= 1
    timerLabel.config(text=f"Time left: {timer} Sec")
    cps = raw / (time_allowed - timer)
    cps = round(cps,2)
    cpsLabel.config(text=(f"Current cps: {cps} "))
    reset.config(state='disabled')

    if timer == 0:
        cpsLabel.config(text=(f"Final cps: {cps} "))
        button.config(state='disabled')
        reset.config(state='normal')
        return timer


    timerLabel.after(1000, update)

def reset():
    global timer
    global i 
    global raw
    timer = 5
    i = "once"
    raw = 0
    cps = 0
    cpsLabel.config(text=(f"Cps: {cps}"))
    timerLabel.config(text=(f"Timer: {time_allowed} Sec"))
    button.config(state='normal')

thefont = tkFont.Font(family="Helvetica",size=16,weight="bold")    

cpsLabel = Label(app,text=(f"Cps: {cps}"),font = thefont)
cpsLabel.place(x=100,y=20,width=200,height=40)

timerLabel = Label(app, text=f"Time left: {timer} Sec",font = thefont)
timerLabel.place(x=100,y=75,width=200,height=40)

button = Button(app, text = "Click me", command=click,font = thefont )
button.place(x=60,y=130,width=280,height=200)

reset = Button(app, text = "Reset",command=reset ,font = thefont)
reset.place(x=140,y=345,width=120,height=30)

app.mainloop()
