from tkinter import *


class Window:

    def __init__(self):
        self.window = Tk()
        self.window.title("Minesweeper")

    def show(self):
        self.window.mainloop()
