from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps=0
timer=None

# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text,text="00:00")
    title.config(text="TIMER")
    check.config(text="")
    global reps
    reps = 0

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps+=1

    work_sec=WORK_MIN*60
    short_break = SHORT_BREAK_MIN*60
    long_break=LONG_BREAK_MIN*60

    if reps % 8==0:
        countdown(long_break)
        title.config(text="LONG BREAK!",fg=RED)
    elif reps % 2==0:
        countdown(short_break)
        title.config(text="SHORT BREAK :D",fg=PINK)
    else:
        countdown(work_sec)
        title.config(text="WORK!",fg=GREEN)





# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
import time

def countdown(count):
    count_min=math.floor(count/60)
    count_sec=count % 60
    # Dynamic Typing
    if count_sec<10:
        count_sec=f"0{count_sec}"
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count>0:
        global timer
        timer = window.after(1000, countdown, count-1)
    else:
        start_timer()
        mark=""
        work_sessions=math.floor(reps/2)
        for _ in range(work_sessions):
            mark+="✔"
        check.config(text=mark)









# ---------------------------- UI SETUP ------------------------------- #

window=Tk()
window.title("POMODORO!")
window.config(padx=100,pady=50,bg=YELLOW)



title=Label(text="TIMER",fg=GREEN,font=(FONT_NAME,50),bg=YELLOW)
title.grid(column=1, row=0)

canvas=Canvas(width=200, height=224,bg=YELLOW, highlightthickness=0)
pic=PhotoImage(file="tomato.png")
canvas.create_image(100,112,image=pic)
timer_text = canvas.create_text(100,130,text="00:00",fill="white",font=(FONT_NAME,35,"bold"))
canvas.grid(column=1,row=1)


s_button=Button(text="START",highlightthickness=0,command=start_timer)
s_button.grid(column=0,row=2)

r_button=Button(text="RESET",highlightthickness=0,command=reset_timer)
r_button.grid(column=2,row=2)

check=Label(fg=GREEN,bg=YELLOW,font=(40))
check.grid(column=1,row=3)


window.mainloop()