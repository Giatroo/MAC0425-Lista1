"""This is the module for the global variables of the project."""

import os

import pygame

WIDTH, HEIGHT = 600, 600

TICKS_WIDTH = 150

O_IMG = pygame.transform.scale(
    pygame.image.load(os.path.join("Assets", "o.png")),
    ((WIDTH - TICKS_WIDTH) // 3, (HEIGHT - TICKS_WIDTH) // 3),
)
X_IMG = pygame.transform.scale(
    pygame.image.load(os.path.join("Assets", "x.png")),
    ((WIDTH - TICKS_WIDTH) // 3, (HEIGHT - TICKS_WIDTH) // 3),
)
BACKGROUND_IMG = pygame.transform.scale(
    pygame.image.load(os.path.join("Assets", "background.png")), (WIDTH, HEIGHT)
)

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
