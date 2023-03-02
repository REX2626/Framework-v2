"""
This file loads all the images
1 pixel in a .png is equvilent to 1 game unit
All images have the same scale, i.e. they're pixels are all 1 game unit in size
"""

import pygame
import sys
import os

def resource_path(relative_path):
    """Get absolute path to asset, used because the .exe stores assets in a different place"""
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

def load_image(path):
    return pygame.image.load(resource_path(path)).convert_alpha()

# Example:
DEFAULT = pygame.transform.scale_by(load_image("assets/default_image.png"), 30) # 10 times larger
# SHIP = load_image("assets/ship_image.png")