def get_n_player_peg_colors():
    return 6


def get_player_peg_colors():
    return "red", "yellow", "green", "cyan", "blue", "magenta"


def test_peg_colors():
    # Testing the board

    if True:
        assert get_n_player_peg_colors() == 6, "The player has 6 peg colors"

    if True:
        n_expected = get_n_player_peg_colors()
        n_actual = len(get_player_peg_colors())
        assert n_expected == n_actual, "There must be 6 peg colors"

    if False:
        # Issue 6
        assert "red" in get_player_peg_colors(), "Red is a peg color"
        assert "yellow" in get_player_peg_colors(), "Yellow is a peg color"
        assert "green" in get_player_peg_colors(), "Green is a peg color"
        assert "cyan" in get_player_peg_colors(), "Cyan is a peg color"
        assert "blue" in get_player_peg_colors(), "Blue is a peg color"
        assert "magenta" in get_player_peg_colors(), "Magenta is a peg color"
