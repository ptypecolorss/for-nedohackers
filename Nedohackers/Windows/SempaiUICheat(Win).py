import tkinter as tk
from tkinter import Tk, Entry, Label, Button, NW
import pyautogui, sys
import os
from PIL import ImageTk, Image
import random
from tkinter import messagebox as mb


def show_image(path):

  def passwd():
    global code
    code = random.randint(100000, 999999)
    print(code)

  def check():
    s = entry.get()
    if not s.isdigit():
      mb.showerror("Код", code)
    else:
      entry.delete(0, END)
      label['text'] = s

  def website():
    os.system('start https://ptypecolorss.github.io/samurai/samurai')

  def instrukt():
    os.system('start https://ptypecolorss.github.io/samurai/instruktion')

  root = tk.Tk()
  a = random.random()
  x = (root.winfo_screenwidth() - root.winfo_reqwidth()) / 2
  y = (root.winfo_screenheight() - root.winfo_reqheight()) / 2
  root.wm_geometry("+%d+%d" % (x, y))
  root.title("SempaiUICheat")
  root.resizable(width=False, height=False)
  root.geometry('500x350')
  img = Image.open(path)
  width = 500
  ratio = (width / float(img.size[0]))
  height = 350
  imag = img.resize((width, height), Image.ANTIALIAS)
  image = ImageTk.PhotoImage(imag)
  panel = tk.Label(root, image=image)
  panel.pack(side="top", fill="both", expand="no")
  lbl = Label(root, text="Привет!")
  lbl.place(relx=.5, rely=.1, anchor="center")
  lbl = Label(root, text="Чтобы воспользоваться: ")
  lbl.place(relx=.5, rely=.2, anchor="center")
  lbl = Label(
    root, text="1) Нажми кнопку левом нижнем углу окна, она выдаст тебе код")
  lbl.place(relx=.5, rely=.3, anchor="center")
  lbl = Label(root, text="2) введи его в поле ввода ниже!")
  lbl.place(relx=.5, rely=.4, anchor="center")
  entry = Entry(root, font='Courier 14')
  entry.place(relx=.5, rely=.6, anchor="center", width=100, height=20)
  entry.focus()

  b1 = Button(text="Код", width=8, height=2)
  b1.config(command=lambda: [passwd(), check()])
  b1.pack(anchor="nw", padx=6, pady=6)
  b1.place(relx=.1, rely=.8, anchor="nw")

  b2 = Button(text="Вебсайт", width=10, height=2)
  b2.config(command=website)
  b2.pack()
  b2.place(relx=.5, rely=.8, anchor="center")

  b3 = Button(text="Инструкция", width=15, height=2)
  b3.config(command=instrukt)
  b3.pack()
  b3.place(relx=.7, rely=.8, anchor="nw")
  root.protocol('WM_DELETE_WINDOW', lambda: None)
  pyautogui.FAILSAFE = False

  while True:

    root.update()
    if entry.get() == "яхзкакойпароль":
      print("worked!")
      #os.system('taskkill /IM explorer.exe /F')
      #os.system('taskkill /IM SempaiUI.exe /F')
      #else:
      a = 'неправильно!'
      print(a)


show_image('fon.jpg')
