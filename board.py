class Board:
    # A Mastermind board

    n_cols = 4
    # Number of columns where a player can place a peg

    n_rows = 10 # Let Kirsten check
    # Equals the number of turns a player has

    def print_me(self):
    # Show the board as text one day
        print("Me: ", self.n_cols, self.n_rows)


def test_board():
    #
    print("Testing the board here")

