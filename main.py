"""Module for the main functionality."""

import pygame

import drawing_engine as drawing
import game_engine as engine


def main():
    pygame.display.set_caption("Jogo da Velha")
    while True:
        drawing.draw_frame()

        for event in pygame.event.get():
            if (
                event.type == pygame.MOUSEBUTTONDOWN
                and engine.WINNER_TYPE == engine.PIECE_EMPTY
            ):
                drawing.handle_mouse_pressed()
                engine.is_game_over()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    engine.init()

            if event.type == pygame.QUIT:
                pygame.quit()
                return

        pygame.display.update()


if __name__ == "__main__":
    main()
