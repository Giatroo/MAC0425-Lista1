"""This is the module for all of drawing engine of the game."""

import pygame

import global_vars as gvars
import colors


def draw_window():
    gvars.WIN.fill(colors.WHITE)
    gvars.WIN.blit(gvars.BACKGROUND_IMG, (0, 0))
    gvars.WIN.blit(gvars.O_IMG, (0, 0))


def draw_frame():
    draw_window()

    pygame.display.update()
