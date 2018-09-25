import random


class Minefield:

    def __init__(self, width, height, prob):
        self.width = width
        self.height = height
        self.grid = list(map(lambda x: list(map(lambda y: random.random() < prob, range(0, height))), range(0, width)))

    def is_mine_at(self, x, y):
        return self.grid[x][y]
