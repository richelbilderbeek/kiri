class Board:
    # A Mastermind board

    def __init__(self):
        # Constructor
        self.peg_colors = [
            [""for i in range(self.n_rows)] for i in range(self.n_cols)
        ]

    n_cols = 4
    # Number of columns where a player can place a peg

    n_rows = 12
    # Number of rows where a player can place a peg

    peg_colors = None
    # A 2D array, y-x-ordered aka ordered-by-row, for example
    # self[1][2] = "orange"
    # will set the second column of the first row to orange

    def print_me(self):
        # Show the board as text one day
        print("Me: ", self.n_cols, self.n_rows)
        print(self.peg_colors)


def test_board():
    # Testing the board

    if True:
        b = Board()
        assert b.n_cols == 4, "A board has four columns"

    if True:
        b = Board()
        assert b.n_rows == 12, "A board has 12 rows"

    if True:
        b = Board()
        assert b.is_empty(), "A new board is empty"

    if True:
        # Issue 11
        b = Board()
        b.set_color(0, 0, "red")
        assert not b.is_empty(), "A board is not empty after a peg is placed"

    if False:
        # Issue 12
        b = Board()
        b.set_color(1, 2, "green")
        # assert b.get_color(1, 2) == "green", "set and get must be symmetric"
