"""This is the module for the global variables of the project."""

import os

import pygame

WIDTH, HEIGHT = 600, 600

TICKS_WIDTH = 15
TICKS_PADDING = 10

O_IMG = pygame.transform.scale(
    pygame.image.load(os.path.join("Assets", "o.png")),
    ((WIDTH - 4 * TICKS_WIDTH) // 3 - 5, (HEIGHT - 4 * TICKS_WIDTH) // 3 - 5),
)
X_IMG = pygame.transform.scale(
    pygame.image.load(os.path.join("Assets", "x.png")),
    ((WIDTH - 4 * TICKS_WIDTH) // 3, (HEIGHT - 4 * TICKS_WIDTH) // 3),
)
BACKGROUND_IMG = pygame.transform.scale(
    pygame.image.load(os.path.join("Assets", "background.png")), (WIDTH, HEIGHT)
)

WIN = pygame.display.set_mode((WIDTH, HEIGHT))

pygame.font.init()
PIECES_FONT = pygame.font.SysFont("Comic Sans MS", WIDTH // 2)
END_FONT = pygame.font.SysFont("Comic Sans MS", 120)
