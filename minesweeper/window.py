from itertools import product
from tkinter import Button, Tk


class Window:

    def __init__(self, field):
        self.minefield = field
        self.window = Tk()
        self.window.title("Minesweeper")

        for (x, y) in product(range(field.width), range(field.height)):
            button = Button(
                self.window,
                text="_",
                command=self.clicked(x, y))
            button.grid(column=x, row=y)

    def clicked(self, x, y):
        return lambda: print(str(self.minefield.is_mine_at(x, y)))

    def show(self):
        self.window.mainloop()
