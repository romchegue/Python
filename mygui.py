# file: mygui.py

from tkinter import *
import random

class MyGui:
    '''
    ГИП с кнопками, которые изменяют цвет и размер надписи
    '''
    colors = ['red', 'green', 'blue', 'yellow', 'orange', 'white', 'cyan', 'purple']
    def __init__(self, parent, title='popup'):
        parent.title(title)
        self.growing = False
        self.fontsize = 10
        self.lab = Label(parent, text='Gui1', fg='white', bg='navy')
        self.lab.pack(expand=YES, fill=BOTH)
        Button(parent, text='Spam', command=self.reply).pack(side=LEFT)
        Button(parent, text='Grow', command=self.grow).pack(side=LEFT)
        Button(parent, text='Stop', command=self.stop).pack(side=LEFT)

    def reply(self):
        ' при нажатии кнопки Spam изменяет цвет случайным образом '
        self.fontsize += 5
        color = random.choice(self.colors)
        self.lab.config(bg=color,
        font=('courier', self.fontsize, 'bold italic'))

    def grow(self):
        'при нажатии кнопки Grow начинает увеличивать размер надписи'
        self.growing = True
        self.grower()

    def grower(self):
        if self.growing:
            self.fontsize += 5
            self.lab.config(font=('courier', self.fontsize, 'bold'))
            self.lab.after(500, self.grower)

    def stop(self):
        'при нажатии кнопки Stop останавливает увеличение размера'
        self.growing = False

class MySubGui(MyGui):
    colors = ['black', 'purple'] # Настройка изменения цвета

MyGui(Tk(), 'main')
MyGui(Toplevel())
MySubGui(Toplevel())
mainloop()