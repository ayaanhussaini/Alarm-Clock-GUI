from tkinter import *
import datetime
import time
import playsound
import os
from threading import *


root = Tk()
root.title('Alarm Clock')
root.geometry('600x400')


def threading1():
    t1 = Thread(target=setAlarm)
    t1.start()


def threading2():
    t2 = Thread(target=stopAlarm)
    t2.start()


hours_label = Label(root, text='Enter hours in 24 hour format (eg.05, 17)')
hours_label.grid(row=0, column=0, pady=20, padx=60)
hours_widget = Entry(root)

hours_widget.grid(row=1, column=0)

minutes_label = Label(root, text='Enter minutes')
minutes_label.grid(row=0, column=1)

minutes_widget = Entry(root)
minutes_widget.grid(row=1, column=1)

alarmTime = ''


def stopAlarm():
    os._exit(os.X_OK)


def setAlarm():
    global alarmTime
    hours = StringVar()
    minutes = StringVar()
    hours = hours_widget.get()
    minutes = minutes_widget.get()
    alarmTime = f'{hours}:{minutes}'
    print(alarmTime)
    triggerAlarm()


def triggerAlarm():
    while True:
        time.sleep(1)
        current_time = datetime.datetime.now()
        now = current_time.strftime('%H:%M')
        print(current_time, now, alarmTime)

        if now == alarmTime:
            while True:
                print('Alarm!')
                playsound.playsound('alarm_sound.wav')


SetAlarmButton = Button(root, text='Set Alarm', command=threading1)
SetAlarmButton.grid(row=3, pady=20)

stopRingingSound = Button(root, text='Quit Alarm', bd='5', command=threading2)
stopRingingSound.grid(column=1, row=3, pady=30)


root.mainloop()
