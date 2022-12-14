from tkinter import *
from playsound import playsound
import time

# create window
window = Tk()
window.title('Productivier')
window.geometry('500x600')
window.config(bg='#D6E4E5')  # configuring window

# create header text
header_text = 'PRODUCTIVE TIME'
header = Label(window, text=header_text, bg='#D6E4E5',
               fg='#497174', pady=10, font='arial 25 bold')  # creating text
header.pack()


def timer():  # local time function
    clock_timer = time.strftime('%H:%M:%S %p')  # create time format
    current_time.config(text=clock_timer)
    current_time.after(1000, timer)  # iterate time every 1s


current_time = Label(window, font="arial 15 bold",
                     text="", bg="#D6E4E5", fg='#497174')  # create text from label
current_time.place(x=190, y=70)  # placing widget pos

timer()

# time_digit
hours = StringVar()  # init stringvar for set and get values from set and get
Entry(window, textvariable=hours, width=2,
      font="arial 50", bg="#D6E4E5", fg='#497174', bd=1).place(x=80, y=150)
hours.set("00")

minutes = StringVar()
Entry(window, textvariable=minutes, width=2,
      font="arial 50", bg="#D6E4E5", fg='#497174', bd=1).place(x=200, y=150)
minutes.set("00")

seconds = StringVar()
Entry(window, textvariable=seconds, width=2,
      font="arial 50", bg="#D6E4E5", fg='#497174', bd=1).place(x=320, y=150)
seconds.set("00")

Label(window, text="hrs", font="arial 12",
      bg="#D6E4E5", fg='#497174').place(x=105, y=200)
Label(window, text="min", font="arial 12",
      bg="#D6E4E5", fg='#497174').place(x=225, y=200)
Label(window, text="sec", font="arial 12",
      bg="#D6E4E5", fg='#497174').place(x=345, y=200)


def count():  # counter function very important!!
    times = int(hours.get())*3600 + int(minutes.get())*60 + int(seconds.get())

    while times > -1:
        # condition for minute count
        # return minute and modulo (as seconds)
        min, sec = (times//60, times % 60)
        hrs = 0
        if min > 60:  # condition for hour count
            # return hour and modulo (as minute)
            hrs, min = (min//60, min % 60)

        seconds.set(sec)
        minutes.set(min)
        hours.set(hrs)

        window.update()  # looping until entire event have been processed
        time.sleep(1)  # delay execution 1s

        if(times == 0):
            playsound('assets/alarm.wav')
            seconds.set("00")
            minutes.set("00")
            hours.set("00")
        times -= 1


def pomodoroBtn():  # create btn function
    hours.set("00")
    minutes.set("45")
    seconds.set("00")


def breakBtn():
    hours.set("00")
    minutes.set("10")
    seconds.set("00")


def workoutBtn():
    hours.set("00")
    minutes.set("20")
    seconds.set("00")


button = Button(window, text="Start", bg="#497174", fg='#D6E4E5',
                width=20, height=2, font="arial 15 bold", command=count)
button.pack(padx=5, pady=30, side='bottom')

img1 = PhotoImage(file="assets/pomodoro-btn.png")
btn1 = Button(window, image=img1, bg="#D6E4E5", bd=0, command=pomodoroBtn)
btn1.place(x=47, y=300)

img2 = PhotoImage(file="assets/break-btn.png")
btn2 = Button(window, image=img2, bg="#D6E4E5", bd=0, command=breakBtn)
btn2.place(x=177, y=300)

img3 = PhotoImage(file="assets/workout-btn.png")
btn3 = Button(window, image=img3, bg="#D6E4E5", bd=0, command=workoutBtn)
btn3.place(x=307, y=300)

window.mainloop()
