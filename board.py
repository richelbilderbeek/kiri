class Board:
    # A Mastermind board

    n_cols = 4
    # Number of columns where a player can place a peg

    n_rows = 12

    c = Rectangle(Point(1, -10), Point(10, -5))
    c.setFill("lightbrown")
    c.setOutline("darkbrown")
    c.draw(win)

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
