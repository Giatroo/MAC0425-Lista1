"""This is the module for all of drawing engine of the game."""

import pygame

import colors
import game_engine as engine
import global_vars as gvars


def _piece_type_to_img(piece_type):
    piece_type_to_img_dict = {engine.PIECE_X: gvars.X_IMG, engine.PIECE_O: gvars.O_IMG}
    return piece_type_to_img_dict[piece_type]


def _loc_to_coordinates(loc):
    column = (
        loc[0] * gvars.WIDTH // 3 - gvars.TICKS_WIDTH // 2 + 2 * gvars.TICKS_PADDING
    )
    row = loc[1] * gvars.HEIGHT // 3 - gvars.TICKS_WIDTH // 2 + 2 * gvars.TICKS_PADDING

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
    coordinates = _loc_to_coordinates(loc)
    piece_img = _piece_type_to_img(piece_type)
    gvars.WIN.blit(piece_img, coordinates)


def draw_pieces():
    for i in range(3):
        for j in range(3):
            piece_type = engine.get_piece((i, j))
            if piece_type != engine.PIECE_EMPTY:
                draw_piece(piece_type, (i, j))


def draw_game_over(winner_type):
    winner_player_dict = {
        engine.PIECE_X: "X",
        engine.PIECE_O: "O",
    }
    color_dict = {
        engine.PIECE_X: colors.BLUE,
        engine.PIECE_O: colors.RED,
    }

    if winner_type == -1: # draw
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
        gvars.WIN, colors.SHADOW, (width, height, text_rend.get_width(),
                                   text_rend.get_height())
    )
    gvars.WIN.blit(text_rend, (width, height))


def handle_mouse_pressed():
    mouse_pos = pygame.mouse.get_pos()

    loc = _coordinates_to_loc(mouse_pos)
    print(loc)

    if engine.get_piece(loc) == engine.PIECE_EMPTY:
        engine.put_piece(engine.get_current_player_type(), loc)
        engine.change_turn()


def draw_window():
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
    draw_window()
    draw_pieces()

    for event in pygame.event.get():
        if (
            event.type == pygame.MOUSEBUTTONDOWN
            and engine.WINNER_TYPE == engine.PIECE_EMPTY
        ):
            handle_mouse_pressed()
            engine.is_game_over()
            if engine.MOVEMENTS_LEFT == 0:
                engine.WINNER_TYPE = -1

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                engine.init()

    if engine.WINNER_TYPE != engine.PIECE_EMPTY:
        draw_game_over(engine.WINNER_TYPE)
    pygame.display.update()


def main():
    pygame.display.set_caption("Jogo da Velha")
    while True:
        draw_frame()


if __name__ == "__main__":
    main()
