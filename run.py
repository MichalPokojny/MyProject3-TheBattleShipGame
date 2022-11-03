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

    def make_guess(self):
        """
        Function for asking the location from the user
        Function also include try, exept methods to catch error for invalid inputs
        """
        try:
            x = input("Enter row number which you want to target.")
            while x not in '01' or x =="":
                print("Not valid number for a row, please choose again.")
                x = input("Enter row number which you want to target.")

            y = input("Enter column number which you want to target.")
            while y not in '01' or y == "":
                print("Not a valid number for a column, please choose again.")
                y = input("Enter column number which you want to target.")

            return int(x), int(y)
        except ValueError:
            print("Not a valid input")
            return self.make_guess()        

    
size = 2
num_ships = 1

game_board = Game(size, num_ships)
game_board.populate_board()
game_board.print_board()
game_board.make_guess()