"""Module for the main functionality."""

import pygame

import drawing_engine as drawing
import game_engine as engine
import minimax as ai


def welcome():
    """The function with the welcome message."""
    print("Welcome to my tic-tac-toe game.\n")
    print("Use R to restart the game.")
    print("Use Q to quit the game.\n")


def init_ai():
    """The function to initiate the AI module."""
    ai_first = int(input("Do you want to be the first or second to play? (1/2) "))
    ai_first = ai_first == 2

    toss_turn = input("Do you want to flip a coin in each turn? (y/n) ")
    toss_turn = toss_turn == "y"

    verbose = input("Do you want the AI to print its thoughts? (y/n) ")
    verbose = verbose == "y"

    ai.init(engine.BOARD, ai_first=ai_first, toss_turn=toss_turn, verbose=verbose)
    return ai_first, toss_turn, verbose


def main():
    """The main function of the game.

    The game should start by this function
    """
    pygame.display.set_caption("Jogo da Velha")

    welcome()
    engine.init()
    ai_first, toss_turn, verbose = init_ai()

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
                    print()
                    ai_first, toss_turn, verbose = init_ai()

                if event.key == pygame.K_e:
                    engine.init()
                    ai.init(
                        engine.BOARD,
                        ai_first=ai_first,
                        toss_turn=toss_turn,
                        verbose=verbose,
                    )

                if event.key == pygame.K_q:
                    print("\nThanks for playing =)")
                    pygame.quit()
                    return

            if event.type == pygame.QUIT:
                print("\nThanks for playing =)")
                pygame.quit()
                return

        pygame.display.update()


if __name__ == "__main__":
    main()
