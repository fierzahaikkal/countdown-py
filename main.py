from tkinter import *
import time

# create window
window = Tk()
window.title('Countdown App')
window.geometry('500x600')
window.config(bg='#D6E4E5')

# create header text
header_text = 'Time'
header = Label(window, text=header_text, bg='#D6E4E5',
               fg='#497174', pady=10, font='arial 25 bold')
header.pack()


def timer():
    clock_timer = time.strftime('%H:%M:%S %p')
    current_time.config(text=clock_timer)
    current_time.after(1000, timer)


current_time = Label(window, font="arial 15 bold",
                     text="", bg="#D6E4E5", fg='#497174')
current_time.place(x=190, y=70)

timer()

# time_digit
hours = StringVar()
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


def count():
    times = int(hours.get())*3600 + int(minutes.get())*60 + int(seconds.get())

    while times > -1:
        min, sec = (times//60, times % 60)
        hrs = 0
        if min > 60:
            hrs, min = (min//60, min % 60)

        seconds.set(sec)
        minutes.set(min)
        hours.set(hrs)

        window.update()
        time.sleep(1)

        if(times == 0):
            seconds.set("00")
            minutes.set("00")
            hours.set("00")
        times -= 1


button = Button(window, text="Start", bg="#497174", fg='#D6E4E5',
                width=20, height=2, font="arial 15 bold", command=count)
button.pack(padx=5, pady=30, side='bottom')

window.mainloop()
