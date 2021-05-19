"""This is the module for the game engine.

Here we keep the board, the functions for deciding if the game is over,
etc.
"""

BOARD = 0
""" BOARD is a trinary number with 9 trinary digits.
0 means no piece.
1 means an X.
2 means an O."""

PIECE_EMPTY = 0
""" Constant for an empty spot on the board """
PIECE_X = 1
""" Constant for an X on the board """
PIECE_O = 2
""" Constant for an O on the board """

PLAYER_TURN = 1
""" If 1, its X's turn, if -1, its O's turn """

MOVEMENTS_LEFT = 9
""" The number of empty squares on the board """


def put_piece(piece_type, loc):
    """Modify BOARD to put the piece_type in the position loc.

    Parameters
    ----------
    piece_type : const
        One option between PIECE_EMPTY, PIECE_X or PIECE_O
    loc : tuple
        Must contain two values, the row and the column, which are integers
        between 1 and 3 inclusive.

    Raises
    ------
    TypeError
        if loc is not a tuple
    """
    global BOARD

    if type(loc) != tuple:
        raise TypeError(f"loc should be a tuple, but was {loc}.")

    column = loc[0] - 1
    row = loc[1] - 1
    digit_loc = row + column * 3

    BOARD += piece_type * 3 ** digit_loc


def get_piece(loc):
    """This function gets a board location loc and returns the piece
    corresponding to that position.

    Parameters
    ----------
    loc : tuple
        Must contain two values, the row and the column, which are integers
        between 1 and 3 inclusive.

    Raises
    ------
    TypeError
        if loc is not a tuple

    Returns
    -------
    digit : const
        A digit indicating the type of the piece. It can be PIECE_EMPTY,
        PIECE_O, PIECE_X.
    """
    global BOARD

    if type(loc) != tuple:
        raise f"loc should be a tuple, but was {loc}."
    column = loc[0] - 1
    row = loc[1] - 1

    digit_loc = row + column * 3
    digit = BOARD // (3 ** digit_loc) % 3
    return digit


def get_board_matrix():
    """This function returns an 2D-list representation of the current board.

    Returns
    -------
    board_matrix : list
        A 2d integer list where each position indicates an empty space or a
        piece.
    """
    board_matrix = []

    for i in range(1, 4):
        line = []
        for j in range(1, 4):
            piece = get_piece((i, j))
            line.append(piece)
        board_matrix.append(line.copy())

    return board_matrix


def _array_game_over(array):
    return array[0] == array[1] == array[2]


def is_game_over():
    """This functions returns the winning piece constant if it was a game over
    or PIECE_EMPTY it's not game over."""

    # row game over
    for i in range(1, 4):
        row = []
        for j in range(1, 4):
            row.append(get_piece((i, j)))
        if _array_game_over(row):
            return row[0]

    # column game over
    for j in range(1, 4):
        column = []
        for i in range(1, 4):
            column.append(get_piece((i, j)))
        if _array_game_over(column):
            return column[0]

    # main diagonal game over
    main_diagonal = []
    for i in range(1, 4):
        main_diagonal.append(get_piece((i, i)))
    if _array_game_over(main_diagonal):
        return main_diagonal[0]

    # off diagonal game over
    off_diagonal = []
    for i in range(1, 4):
        off_diagonal.append(get_piece((i, 4 - i)))
    if _array_game_over(off_diagonal):
        return off_diagonal[0]

    return PIECE_EMPTY


def main():
    global BOARD

    put_piece(PIECE_X, (3, 1))
    put_piece(PIECE_X, (2, 2))
    put_piece(PIECE_X, (1, 3))
    print(get_board_matrix())
    print(is_game_over())


if __name__ == "__main__":
    main()