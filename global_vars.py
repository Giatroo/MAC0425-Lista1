"""This is the module for the global variables of the project."""

import os

import pygame

WIDTH, HEIGHT = 600, 600

TICKS_WIDTH = 15
TICKS_PADDING = 10

WIN = pygame.display.set_mode((WIDTH, HEIGHT))

pygame.font.init()
PIECES_FONT = pygame.font.SysFont("Comic Sans MS", WIDTH // 2)
END_FONT = pygame.font.SysFont("Comic Sans MS", 120)
