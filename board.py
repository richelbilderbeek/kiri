class Board:
    # A Mastermind board

    n_cols = 4
    # Number of columns where a player can place a peg

    n_rows = 12

    def print_me(self):
        # Show the board as text one day
        print("Me: ", self.n_cols, self.n_rows)


def test_board():
    # Testing the board

    if True:
        b = Board()
        assert b.n_cols == 4, "A board has four columns"

    if True:
        b = Board()
        assert b.n_rows == 12, "A board has 12 rows"

    if False:
        # Issue 10
        b = Board()
        assert b.is_empty(), "A new board is empty"

    if False:
        # Issue 11
        b = Board()
        b.set_color(0, 0, "red")
        assert !b.is_empty(), "A board is not empty after a peg is placed"
