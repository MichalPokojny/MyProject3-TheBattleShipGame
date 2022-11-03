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
        # Function to populate the board with random locations. 
        
        for i in range(num_ships):
            self.x, self.y = randint(0, size - 1), randint(0, size - 1)
            self.board[self.x][self.y] = "@"

            return self.board[self.x][self.y]

    def print_board(self):
        # Function to print the board with location of the ship

        print(" 0 1")
        row_number = 0
        for row in self.board:
            print(row_number, " ".join(row))
            row_number += 1

    
size = 2
num_ships = 1

game_board = Game(size, num_ships)
game_board.populate_board()
game_board.print_board()


  