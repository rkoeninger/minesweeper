from minesweeper.minefield import Minefield
from minesweeper.window import Window


def main():
    Window(Minefield(16, 16, 0.1)).show()


if __name__ == '__main__':
    main()
