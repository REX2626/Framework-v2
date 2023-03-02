"""
This file has all constants for other files to use
It also has functions that can be used in any file e.g. game.quit()
"""

import pygame

WIN = pygame.display.set_mode(flags=pygame.FULLSCREEN+pygame.RESIZABLE)

import images
pygame.display.set_icon(images.DEFAULT)

pygame.init()

import sys
from objects import Vector


WIDTH, HEIGHT = pygame.display.get_window_size()
FULLSCREEN = True
FULLSCREEN_SIZE = WIDTH, HEIGHT
WINDOW_SIZE = WIDTH * 0.8, HEIGHT * 0.8
SIZE_LINK = True

# CENTRE_POINT is the position of player on screen
CENTRE_POINT = Vector(WIDTH/2, HEIGHT/2)

PLAYER_POSITION = Vector(0, 0)

WHITE = (255, 255, 255)
LIGHT_GREY = (120, 120, 120)
MEDIUM_GREY = (60, 60, 60)
DARK_GREY = (30, 30, 30)
BLACK = (0, 0, 0)

objects = [] # list of all game objects


def quit():
    """Stops the program"""
    pygame.quit()
    sys.exit(0)


def update_screen_size():
    """Updates objects size and position with new screen size"""
    "Adjust any constants"

    global WIDTH, HEIGHT, CENTRE_POINT
    WIDTH, HEIGHT = pygame.display.get_window_size()
    CENTRE_POINT = Vector(WIDTH/2, HEIGHT/2)

    if SIZE_LINK:
        "Adjust objects size"