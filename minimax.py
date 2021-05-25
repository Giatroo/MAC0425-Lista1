"""This module implements the minimax algorithm."""

import numpy as np

import game_engine as engine

AI_PIECE = engine.PIECE_X
"""" The type of the piece of the AI """
PLAYER_PIECE = engine.PIECE_O
""" The type of the piece of the player """

AI_VERBOSE = True
""" Defines if the AI will print it's thoughts about the game """

INF = 2
""" A constant for a infinity amount """

NULL_MOVE = (-1, -1)
""" A constant for a null movement """


def init(board, ai_first=False, verbose=False):
    """Initializes the AI choosing if the AI is going to play first or second.

    If the AI will play first, it makes the first move.

    Parameters
    ----------
    board : numpy ndarray
        A 3x3 representation of the board (it will probably be empty)
    ai_first : bool, default=False
        If the AI is going to play first or second (be X or O).
    verbose : bool, default=True
        If the AI will print the evaluation of the board or not.
    """
    global AI_PIECE, PLAYER_PIECE, AI_VERBOSE

    AI_VERBOSE = verbose

    if ai_first:
        AI_PIECE = engine.PIECE_X
        PLAYER_PIECE = engine.PIECE_O
        move(board, AI_VERBOSE)
    else:
        AI_PIECE = engine.PIECE_O
        PLAYER_PIECE = engine.PIECE_X


def _array_game_over(array):
    if array[0] == engine.PIECE_EMPTY:
        return False
    return np.all(array == array[0])


def is_game_over(board):
    """A copy of the is_game_over of the engine, but capable of evaluating if
    the game is over for a specific board.

    Parameters
    ----------
    board : numpy ndarray
        A 3x3 representation of the board.
    Returns
    -------
    const
        The return will be one of `PIECE_X`, `PIECE_O`, `DRAW_ID` or
        `PIECE_EMPTY`. If it's the last one, than the game is not over yet. But
        it's one of the firsts, than or X won, or O won or it's a draw
        (respectively).
    """

    # row game over
    for i in range(3):
        row = board[i, :]
        if _array_game_over(row):
            return row[0]

    # column game over
    for j in range(3):
        column = board[:, j]
        if _array_game_over(column):
            return column[0]

    # main diagonal game over
    main_diagonal = np.diagonal(board)
    if _array_game_over(main_diagonal):
        return main_diagonal[0]

    # off diagonal game over
    off_diagonal = [board[0, 2], board[1, 1], board[2, 0]]
    if _array_game_over(off_diagonal):
        return off_diagonal[0]

    for i in range(3):
        if np.any(board[i] == engine.PIECE_EMPTY):
            return engine.PIECE_EMPTY

    return engine.DRAW_ID


def get_moves(board, player_to_move):
    """Returns all the possible moves for a certain player on a certain board.

    Parameters
    ----------
    board : numpy ndarray
        The current board position.
    player_to_move : const
        Must be ether AI_PIECE or PLAYER_PIECE, indicating who is the next to
        move.

    Yields
    ------
    new_board : numpy ndarray
        The board modified by the player's play.
    loc : tuple
        The tuple encoding the square played.
    """
    for i in range(3):
        for j in range(3):
            if board[i][j] == engine.PIECE_EMPTY:
                new_board = board.copy()
                new_board[i][j] = player_to_move
                yield (new_board, (i, j))


def minimax(board, maxi=True, alpha=-INF, beta=INF):
    """The minimax algorithm. It receives a board and player to evaluate.

    Parameters
    ----------
    board : numpy ndarray
        The current board
    maxi : bool, default=True
        If the AI is maximazim its gains or minimizing its loses.
    alpha : int, default=-INF
        The alpha value (referent to the alpha-beta pruning technic)
    beta :
        The beta value (referent to the alpha-beta pruning technic)

    Returns
    -------

    board_value : int
        If the AI thinks the position is a draw, than it returns 0. If it thinks
        it's a winning position, then it returns 1. If it thinks it's a losing
        game, then it returns -1.
    loc : tuple
        The best possible movement in the position.
    """
    game_over = is_game_over(board)
    # game over cases:
    if game_over == engine.DRAW_ID:  # draw
        return 0, NULL_MOVE
    if game_over == AI_PIECE:  # ai wins
        return 1, NULL_MOVE
    if game_over == PLAYER_PIECE:  # player wins
        return -1, NULL_MOVE

    if maxi:
        maxi_value = -INF
        best_move = NULL_MOVE
        for new_board, move in get_moves(board, AI_PIECE):
            minimax_ret = minimax(new_board, not maxi, alpha, beta)
            if minimax_ret[0] > maxi_value:
                maxi_value = minimax_ret[0]
                best_move = move

            alpha = max(alpha, maxi_value)
            if alpha >= beta:
                break
        return maxi_value, best_move
    else:
        mini_value = INF
        best_move = NULL_MOVE
        for new_board, move in get_moves(board, PLAYER_PIECE):
            minimax_ret = minimax(new_board, not maxi, alpha, beta)
            if minimax_ret[0] < mini_value:
                mini_value = minimax_ret[0]
                best_move = move

            beta = min(beta, mini_value)
            if alpha >= beta:
                break
        return mini_value, best_move


def move(board, verbose=False):
    """Function called when we want the AI to play. It puts a piece on the
    board and change the turn.

    Parameters
    ----------
    board : numpy ndarray
        The current board.
    verbose : bool, default=False
        If we want or not the AI to tell us its evaluation of the position.
    """
    value, movement = minimax(board)

    if verbose:
        value_to_str = {-1: "Losing game", 0: "Game tied", 1: "Winning game"}
        print(f'[AI]: {value_to_str[value]}')

    engine.put_piece(AI_PIECE, movement)
    engine.change_turn()


def main():
    """The test function."""
    board = np.full((3, 3), engine.PIECE_EMPTY, dtype=int)
    board[0][1] = engine.PIECE_X
    board[0][0] = engine.PIECE_O
    board[2][2] = engine.PIECE_X
    board[1][1] = engine.PIECE_O
    print(board)
    print(minimax(board, maxi=True))


if __name__ == "__main__":
    main()
