from random import randint


class Game_board:
    """
    Main class game
    Class contain size and num of the ships.
    Function for populating board with random locations.
    Function for printing the board with selected locations.
    Function for asking the location from user.
    """

    def __init__(self, size, num_ships):
        """
        Set attribute for size and number of ships.
        Set board for the game.
        """
        self.size = size
        self.num_ships = num_ships
        self.board = [["." for x in range(size)] for y in range(size)]

    def populate_board(self, size, num_ships):
        # Function to populate the board with random locations.
        for i in range(num_ships):
            self.x, self.y = randint(0, size - 1), randint(0, size - 1)
            self.board[self.x][self.y] = "@"

            return self.board[self.x][self.y]

    def print_board(self):
        # Function to print the board with location of the ship

        print("     0 1 2 3 4")
        row_number = 0
        for row in self.board:
            print("  ", row_number, " ".join(row))
            row_number += 1

    def make_guess(self):
        """
        Function for asking the location from the user
        then run the try, exept methods to catch error for invalid
        inputs.
        """
        try:
            x = input("Enter row number which you want to target.")
            while x not in "01234" or x == "":
                print("Not valid number for a row, please choose again.\n")
                x = input("Enter row number which you want to target.")

            y = input("Enter column number which you want to target.")
            while y not in "01234" or y == "":
                print("Not a valid number for a column, please choose again.")
                y = input("Enter column number which you want to target.")

            return int(x), int(y)
        except ValueError:
            print("Not a valid input.Try again.\n")
            return self.make_guess()


def New_game():
    # Main function to play the game
    name = input("Hi! What's your name?\n")

    print("------------------------------------------------------------")
    print("------------------------------------------------------------")
    print(f"\n   Welcome {name} to the Ultimate Battleship game!")
    print("\n   You have 3 guesses to try to find and destroy enemy ship!")
    print("   You need to select row and column from 0 to 4 only.")
    print("   Good luck!\n")
    print("------------------------------------------------------------")
    print("------------------------------------------------------------")

    size = 5
    num_ships = 1
    tries = 3
    game_board = Game_board(size, num_ships)
    game_board.populate_board(size, num_ships)
    while True:

        x, y = Game_board.make_guess(object)

        if game_board.board[x][y] == "@":
            print(f"\nHit! Well done {name}. You won!")
            game_board.print_board()
            break

        else:
            if game_board.board[x][y] == "X":
                print("Guessed that one already, try different one!")
                print(
                    "--------------------------------------------------------\
-----"
                )
                continue
            tries -= 1
            game_board.board[x][y] = "X"
            if tries == 0:
                print(f"\nSorry you lost {name}.")
                print("Hopefully you can get it next time!")
                print("Have a look where the ship was located!")
                game_board.print_board()
                print(
                    "--------------------------------------------------------\
-----"
                )
                New_game()
            print("Miss! Try again!")
            print(f"You have {tries} tries left.")
            ask_to_continue = input(
                "Continue? If yes, press any key.If not, \
type n: "
            ).lower()
            if ask_to_continue == "n":
                New_game()
        print("-------------------------------------------------------------")


New_game()
