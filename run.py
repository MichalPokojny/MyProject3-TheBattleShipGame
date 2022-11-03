from random import randint


class Game:
    """
    Main class game
    """

    def __init__(self, size, num_ships):
        """
        Set attribute for size and number of ships.
        Set board for the game
        """
        self.size = size
        self.num_ships = num_ships
        self.board = [["." for x in range(size)] for y in range(size)]

    def populate_board(self):
        """
        Define function to populate the board with random locations. 
        """
        for i in range(num_ships):
            self.x, self.y = randint(0, size), randint(0, size)

            return self.board[self.x][self.y] == "@"    