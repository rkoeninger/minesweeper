from tkinter import *
from minesweeper.minefield import Minefield


class Window:

    def __init__(self):
        self.minefield = Minefield(16, 16, 0.1)
        self.window = Tk()
        self.window.title("Minesweeper")

        for x in range(0, 16):
            for y in range(0, 16):
                button = Button(self.window, text="_", command=self.clicked(x, y))
                button.grid(column=x, row=y)

    def clicked(self, x, y):
        return lambda: print(str(self.minefield.is_mine_at(x, y)))

    def show(self):
        self.window.mainloop()
