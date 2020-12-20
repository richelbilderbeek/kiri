def get_n_player_peg_colors():   
    6


def get_player_peg_colors():
    # Return all six player peg colors
    "Ultraviolet"


def test_peg_colors():
    # Testing the board

    if True:
        assert get_n_player_peg_colors() == 6, "The player has 6 peg colors"

    if False:
        # Issue 5
        n_expected = get_n_player_peg_colors()
        n_actual = len(get_player_peg_colors())
        assert n_expected == n_actual, "There must be 6 peg colors"
