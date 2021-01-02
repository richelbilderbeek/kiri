from board import *


class Game:
   # A game of Mastermind, that is
    def __init__(self):
        self.board = Board()

    # - a board
    board = None

    # - a code, by default 0000 for now, where '0' is the first color

    def print_me(self):
        # Show the board as text one day
        print("I am a game")
        self.board.print_me()

    def test_game():
   # Testing the game
    if True:
        g = Game()
    assert g.board.n_cols == 4, "A game has a board"

    if False:
        g = Game()
        assert len(g.code) > 0, "A game has a code"

    if False:
        # Issue 15
        g = Game()
        assert get_winner(g) == "none", "A new game has no winner"

    if False:
        # Issue 16
        g = Game()
        assert get_n_guesses_done(g) == 0, "A new game has zero guesses done"

    if False:
        # Issue 17
        g = Game()
        move = "red", "red", "red", "red"
        g.guess(move)
        assert get_n_guesses_done(g) == 1, "After a guess, one guess is done"
