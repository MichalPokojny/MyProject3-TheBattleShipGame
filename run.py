from random import randint


class Game:
    """
    Main class game
    """

    def __init__(self, size, num_ships):
        self.size = size
        self.num_ships = num_ships
        self.board = [["." for x in range(size)] for y in range(size)
        ]