import random


class Spot:

    @staticmethod
    def random(x, y, probability):
        """Create an unrevealed minefield spot that randomly has a mine.

        probability -- should be 0 <= p <= 1.
        """
        return Spot(x, y, random.random() < probability, False)

    def __init__(self, x, y, mine, revealed):
        self.x = x
        self.y = y
        self.mine = mine
        self.revealed = revealed

    def __str__(self):
        values = (self.x, self.y, self.mine, self.revealed)
        return '(%s, %s, %s, %s)' % values


class Minefield:

    def __init__(self, width, height, probability):
        self.width = width
        self.height = height

        def xs(x):

            def ys(y):
                return Spot.random(x, y, probability)

            return list(map(ys, range(0, height)))

        self.grid = list(map(xs, range(0, width)))

    def is_mine_at(self, x, y):
        return self.grid[x][y].mine

    def is_revealed_at(self, x, y):
        return self.grid[x][y].revealed
