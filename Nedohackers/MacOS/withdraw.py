import tkinter as tk
from PIL import ImageTk, Image
from tkinter import Tk, Entry, Label, Button, NW
from tkinter import ttk
import os, pyautogui, sys
import random
from random import randint

def show_image(path):
  #окошко
    root = tk.Tk()
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

  #Текст
    lbl = Label(root , text="Привет!")
    lbl.place(relx=.5, rely=.1, anchor="center")
    lbl = Label(root , text="Чтобы воспользоваться: ")
    lbl.place(relx=.5, rely=.2, anchor="center")
    lbl = Label(root , text="1) Нажми кнопку левом нижнем углу окна, она выдаст тебе код")
    lbl.place(relx=.5, rely=.3, anchor="center")
    lbl = Label(root, text="2) введи его в поле ввода ниже!")
    lbl.place(relx=.5, rely=.4, anchor="center")
    
  #ранломный код
    def code():
        global a
        a = random.randint(100000, 999999)
        print (a)

    def check():
        print (a)

    def website():
        os.system('start https://ptypecolorss.github.io/samurai/samurai')
    def instrukt():
        os.system('start https://ptypecolorss.github.io/samurai/instruktion')
   #кнопочки

    b1 = Button(text="Код", width=8, height=2)
    b1.config(command=code)
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
    #поле ввода
    entry = Entry(root, font='Courier 12')
    entry.place(relx=.5, rely=.6, anchor="center", width=100, height=20)
    entry.focus()
    def valid():
        while True:
            root.update()
	
        if entry.get() =="яхзкакойпароль":
            sys.exit()
    root.mainloop()
show_image('C:\\Users\\arsenkubrin\\Desktop\\Nedohackers\\fon.jpg')
