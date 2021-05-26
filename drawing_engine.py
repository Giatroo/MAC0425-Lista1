"""This is the module for all of drawing engine of the game."""

import pygame

import colors
import game_engine as engine
import global_vars as gvars
import minimax as ai

def _piece_type_to_txt(piece_type):
    piece_type_to_txt_dict = {
        engine.PIECE_X: "X",
        engine.PIECE_O: "O",
        engine.PIECE_EMPTY: " ",
    }
    return piece_type_to_txt_dict[piece_type]


def _piece_type_to_color(piece_type):
    piece_type_to_color_dict = {
        engine.PIECE_X: colors.BLUE,
        engine.PIECE_O: colors.RED,
    }
    return piece_type_to_color_dict[piece_type]


def _loc_to_coordinates(loc):
    column = (
        loc[0] * gvars.WIDTH // 3 - gvars.TICKS_WIDTH // 2 + 2 * gvars.TICKS_PADDING
    )
    row = loc[1] * gvars.HEIGHT // 3 - gvars.TICKS_WIDTH // 2 + 3 * gvars.TICKS_PADDING

    return (row, column)


def _coordinates_to_loc(coordinates):
    row = column = 0

    for i in range(3):
        if gvars.WIDTH // 3 * i <= coordinates[0] <= gvars.WIDTH // 3 * (i + 1):
            row = i
            break

    for j in range(3):
        if gvars.HEIGHT // 3 * j <= coordinates[1] <= gvars.HEIGHT // 3 * (j + 1):
            column = j
            break

    return (column, row)


def draw_piece(piece_type, loc):
    """Draws a piece onto the screen.

    Params
    ------
    piece_type : const
        One option between PIECE_EMPTY, PIECE_X or PIECE_O
    loc : tuple
        A location tuple with the square to draw the piece
    """

    coordinates = _loc_to_coordinates(loc)
    piece_txt = gvars.PIECES_FONT.render(
        _piece_type_to_txt(piece_type), False, _piece_type_to_color(piece_type)
    )
    gvars.WIN.blit(piece_txt, coordinates)


def draw_pieces():
    """Draws all the pieces onto the screen."""
    for i in range(3):
        for j in range(3):
            piece_type = engine.get_piece((i, j))
            if piece_type != engine.PIECE_EMPTY:
                draw_piece(piece_type, (i, j))


def draw_game_over(winner_type):
    """Draws the game over message onto the screen.

    Params
    ------
    winner_type : const
        One of PIECE_X, PIECE_O or DRAW_ID
    """
    winner_player_dict = {
        engine.PIECE_X: "X",
        engine.PIECE_O: "O",
    }
    color_dict = {
        engine.PIECE_X: colors.BLUE,
        engine.PIECE_O: colors.RED,
    }

    if winner_type == engine.DRAW_ID:
        color = colors.GREEN
        text = "DRAW"
    else:
        winner_player = winner_player_dict[winner_type]
        color = color_dict[winner_type]
        text = f"PLAYER {winner_player}"

    text_rend = gvars.END_FONT.render(text, False, color)
    width = (gvars.WIDTH - text_rend.get_width()) // 2
    height = gvars.HEIGHT // 2 - text_rend.get_height() // 2

    pygame.draw.rect(
        gvars.WIN,
        colors.SHADOW,
        (width, height, text_rend.get_width(), text_rend.get_height()),
    )
    gvars.WIN.blit(text_rend, (width, height))


def handle_mouse_pressed():
    """Function to handle the mouse pressed event.

    It puts a piece on the location where the mouse is at.
    """
    mouse_pos = pygame.mouse.get_pos()

    loc = _coordinates_to_loc(mouse_pos)

    if engine.get_piece(loc) == engine.PIECE_EMPTY:
        engine.put_piece(engine.get_current_player_type(), loc)
        changed = engine.change_turn(engine.FLIPPING_COIN)

        if changed and engine.is_game_over() == engine.PIECE_EMPTY:
            # Then, the AI must play
            ai.move(engine.BOARD, engine.FLIPPING_COIN, ai.AI_VERBOSE)


def draw_background():
    """Draws the background cross."""
    gvars.WIN.fill(colors.WHITE)

    for i in range(1, 3):
        x = gvars.WIDTH // 3 * i - gvars.TICKS_WIDTH // 2
        y = gvars.TICKS_PADDING
        width = gvars.TICKS_WIDTH
        height = gvars.HEIGHT - 2 * gvars.TICKS_PADDING

        tick = pygame.Rect(x, y, width, height)
        pygame.draw.rect(gvars.WIN, colors.BLACK, tick)

    for i in range(1, 3):
        x = gvars.TICKS_PADDING
        y = gvars.HEIGHT // 3 * i - gvars.TICKS_WIDTH // 2

        height = gvars.TICKS_WIDTH
        width = gvars.WIDTH - 2 * gvars.TICKS_PADDING

        tick = pygame.Rect(x, y, width, height)
        pygame.draw.rect(gvars.WIN, colors.BLACK, tick)


def draw_frame():
    """Draws a frame of the game.

    Must be called at each iteration of our game loop.
    """
    draw_background()
    draw_pieces()

    if engine.WINNER_TYPE != engine.PIECE_EMPTY:
        draw_game_over(engine.WINNER_TYPE)


def main():
    """Tests function."""
    pass


if __name__ == "__main__":
    main()
