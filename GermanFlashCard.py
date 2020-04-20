from tkinter import *
from tkinter import ttk

from PIL import Image, ImageTk
import random
import time


def germandict():
    print("Process >>> germandict")
    Voc = Toplevel()
    DE_EN = {'Test':'test.jpg',
             'MSIG':'msig.jpg'}
    print(DE_EN)

    voc,pic = random.choice(list(DE_EN.items()))
    print(voc)
    print(pic)

    image = Image.open(pic)
    photo = ImageTk.PhotoImage(image)

    label = Label(Voc,image=photo)
    label.image = photo
    label.pack()

    translate = Label(Voc,text =voc)
    translate.config(font=("Courier",44))
    translate.pack(ipady=20)
    Voc.mainloop()

if __name__ == '__main__':
    print("Process >>> IF")
    GUI = Tk()
    GUI.title('German Flash Card')
    GUI.geometry("400x200+30+30")

    German = Label(GUI, text ="German Flash Card \n By MySelf")
    German.config(font=("tohama",25))
    German.pack(padx=20,pady=20)

    B = ttk.Button(GUI, text="Vacob", command = germandict)
    B.pack()

    GUI.mainloop()

print(__name__)
#input("EnyPress to exit")
