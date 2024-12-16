from tkinter import *
import time
import math
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 0.1
SHORT_BREAK_MIN = 0.1
LONG_BREAK_MIN = 20
reps=0
timer_status=None

def reset():
    window.after_cancel(timer_status)
    canvas.itemconfig(timer_text,text="00:00")
    global reps
    reps=0
    timer.config(text="Timer",fg=GREEN)
    check_marks.config(text="")


def timer_start():
    global reps
    reps+=1
    work_sec=WORK_MIN*60
    short_sec=SHORT_BREAK_MIN*60
    long_sec=LONG_BREAK_MIN*60

    if reps %8==0:
        count_down(long_sec)
        timer.config(text="Break",fg=RED)
    elif reps%2==0:
        count_down(short_sec)
        timer.config(text="Break",fg=PINK)
    else:
        count_down(work_sec)
        timer.config(text="Work",fg=GREEN)


def count_down(count):
    count_min= math.floor(count/60)
    count_sec=count%60
    if count_sec==0 and count_sec>10:
       count_sec="00"
    if int(count_sec)<10 and int(count_sec)>=0:
        count_sec=f"0{count_sec}"
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count>0:
        global timer_status
        timer_status=window.after(1000,count_down,count-1)
    else:
        timer_start()
        mark=''
        for _ in range(math.floor(reps/2)):
            mark+="✓"
        check_marks.config(text=mark)


window=Tk()
window.title("Pomodoro")
window.config(padx=50,pady=50, bg=YELLOW)

canvas=Canvas(width=200,height=224,bg=YELLOW, highlightthickness=0)
tomato_img=PhotoImage(file="tomato.png")
canvas.create_image(100,112,image=tomato_img)
timer_text=canvas.create_text(100,130, text="00:00",fill="white",font=(FONT_NAME, 35 , "bold"))
timer=Label(text="Timer",fg=GREEN,font=(FONT_NAME, 50),bg=YELLOW,highlightthickness=0)
timer.grid(row=0,column=1)
canvas.grid(row=1,column=1)

start_button=Button(text="Start",command=timer_start,highlightthickness=0,relief="flat",bd=0,highlightbackground=YELLOW,bg=YELLOW,fg="black")
start_button.grid(row=2,column=0)
reset_button=Button(text="Reset",command=reset,highlightthickness=0,relief="flat",bd=0,highlightbackground=YELLOW,bg=YELLOW,fg="black")
reset_button.grid(row=2,column=2)
check_marks=Label(fg=GREEN,bg=YELLOW, highlightthickness=0,font=(FONT_NAME, 35 , "bold"))
check_marks.grid(row=3,column=1)
window.mainloop()