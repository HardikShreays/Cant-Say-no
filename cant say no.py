from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox
import random



def yes():
    global win
    messagebox.showinfo("yay!", "yay!! Thank you !love you <3")
X,Y = 400,400
def no():
    global X,Y,cb
    X = random.randint(0,600)
    Y = random.randint(0,600)
    cb.place(x = X,y = Y)

win = Tk()
win.title("PLEASE SAY YES!!!!")
win.geometry("600x600")
win.configure(background="Pink")

pilImage = Image.open("download.jpg")
pilImage = pilImage.resize((400, 200))
canvas = Canvas(win)
canvas.place(x = 150, y = 150)
image = ImageTk.PhotoImage(pilImage)
canvas.create_image(0, 0, anchor=NW, image=image)

Button(win, text= "YES", command=yes).place(x = 150, y = 400)
cb = Button(win, text= "NO", command=no)
cb.place(x = 400, y = 400)

win.image = image

win.mainloop()

