"""This is the module for all of drawing engine of the game."""

import pygame

import colors
import game_engine as engine
import global_vars as gvars


def piece_type_to_img(piece_type):
    piece_type_to_img_dict = {engine.PIECE_X: gvars.X_IMG, engine.PIECE_O: gvars.O_IMG}
    return piece_type_to_img_dict[piece_type]


def draw_piece(piece_type, loc):
    additional_pading = {
        0: 50,
        1: 25,
        2: 0,
    }

    column = loc[0] * gvars.WIDTH // 3 + additional_pading[loc[0]]
    row = loc[1] * gvars.HEIGHT // 3 + additional_pading[loc[1]]
    coordinates = (row, column)
    piece_img = piece_type_to_img(piece_type)
    gvars.WIN.blit(piece_img, coordinates)


def draw_pieces():
    for i in range(3):
        for j in range(3):
            piece_type = engine.get_piece((i, j))
            if piece_type != engine.PIECE_EMPTY:
                draw_piece(piece_type, (i, j))


def handle_mouse_pressed():
    mouse_pos = pygame.mouse.get_pos()

    row = 0
    column = 0

    for i in range(3):
        if gvars.WIDTH // 3 * i <= mouse_pos[0] <= gvars.WIDTH // 3 * (i + 1):
            row = i
            break

    for j in range(3):
        if gvars.HEIGHT // 3 * j <= mouse_pos[1] <= gvars.HEIGHT // 3 * (j + 1):
            column = j
            break

    loc = (column, row)
    if engine.get_piece(loc) == engine.PIECE_EMPTY:
        engine.put_piece(engine.PIECE_O, loc)


def draw_window():
    gvars.WIN.fill(colors.WHITE)
    gvars.WIN.blit(gvars.BACKGROUND_IMG, (0, 0))


def draw_frame():
    draw_window()
    draw_pieces()

    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            handle_mouse_pressed()

    pygame.display.update()


def main():
    engine.put_piece(engine.PIECE_O, (1, 2))
    engine.put_piece(engine.PIECE_X, (0, 1))
    print(engine.get_board_matrix())
    while True:
        draw_frame()


if __name__ == "__main__":
    main()
