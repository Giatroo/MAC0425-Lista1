"""This is the module for the game engine.

Here we keep the board, the functions for deciding if the game is over,
etc.
"""

import numpy as np

BOARD = np.zeros((3, 3), dtype=int)
""" BOARD is a 3x3 matrix where each position must be one of PIECE_EMPTY,
PIECE_X or PIECE_O """

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

DRAW_ID = -1
""" The constant that indicates a draw """

WINNER_TYPE = PIECE_EMPTY
""" If the game is over, WINNER_TYPE will be PIECE_X, PIECE_O or DRAW_ID """


def put_piece(piece_type, loc):
    """Modify BOARD to put the piece_type in the position loc.

    Parameters
    ----------
    piece_type : const
        One option between PIECE_EMPTY, PIECE_X or PIECE_O
    loc : tuple
        Must contain two values, the row and the column, which are integers
        between 0 and 2 inclusive.

    Raises
    ------
    TypeError
        if loc is not a tuple
    """
    global BOARD

    if type(loc) != tuple:
        raise TypeError(f"loc should be a tuple, but was {loc}.")

    BOARD[loc[0], loc[1]] = piece_type


def get_piece(loc):
    """This function gets a board location loc and returns the piece
    corresponding to that position.

    Parameters
    ----------
    loc : tuple
        Must contain two values, the row and the column, which are integers
        between 0 and 2 inclusive.

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

    return BOARD[loc[0], loc[1]]


def change_turn():
    global PLAYER_TURN, MOVEMENTS_LEFT
    PLAYER_TURN *= -1
    MOVEMENTS_LEFT -= 1


def get_current_player_type():
    global PLAYER_TURN
    return PIECE_X if PLAYER_TURN == 1 else PIECE_O


def _array_game_over(array):
    if array[0] == PIECE_EMPTY:
        return False
    return np.all(array == array[0])


def is_game_over():
    """This functions returns the winning piece constant if it was a game over
    or PIECE_EMPTY it's not game over."""
    global WINNER_TYPE

    # row game over
    for i in range(3):
        row = BOARD[i, :]
        if _array_game_over(row):
            WINNER_TYPE = row[0]
            return row[0]

    # column game over
    for j in range(3):
        column = BOARD[:, j]
        if _array_game_over(column):
            WINNER_TYPE = column[0]
            return column[0]

    # main diagonal game over
    main_diagonal = np.diagonal(BOARD)
    if _array_game_over(main_diagonal):
        WINNER_TYPE = main_diagonal[0]
        return main_diagonal[0]

    # off diagonal game over
    off_diagonal = np.array([], dtype=int)
    for i in range(3):
        off_diagonal = np.append(off_diagonal, [get_piece((i, 2 - i))])
    if _array_game_over(off_diagonal):
        WINNER_TYPE = off_diagonal[0]
        return off_diagonal[0]

    if MOVEMENTS_LEFT == 0:
        WINNER_TYPE = DRAW_ID

    return PIECE_EMPTY


def init():
    global BOARD, MOVEMENTS_LEFT, WINNER_TYPE, PLAYER_TURN
    BOARD = np.zeros((3, 3), dtype=int)
    MOVEMENTS_LEFT = 9
    WINNER_TYPE = PIECE_EMPTY
    PLAYER_TURN = 1


def main():
    global BOARD

    put_piece(PIECE_X, (2, 0))
    put_piece(PIECE_X, (1, 1))
    put_piece(PIECE_X, (0, 2))
    print(is_game_over())


if __name__ == "__main__":
    main()
