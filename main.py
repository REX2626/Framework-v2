import pygame

import game
from entities import Ship # Example
import menu
from time import perf_counter

pygame.display.set_caption("Framework")



def update_playing_screen_size():
    """Updates live objects positions"""

    "Get objects position on screen by ratio e.g. 20% of the screen"

    game.update_screen_size()

    "Set the x and y of objects based on new width and height, with ratios"

    "Clip the coords of any object out of bounds"


def draw_window():
    """Draw window"""
    game.WIN.fill(game.BLACK)

    for object in game.objects:
        object.draw(game.WIN, game.PLAYER_POSITION)

    pygame.display.update()


def handle_player_input(keys_pressed, delta_time):

    """Adjust player velocity depnding on input. NOTE: Not for changing position"""
    # Example:
    """if keys_pressed[pygame.K_w]:
        player.move_forward(delta_time)

    if keys_pressed[pygame.K_s]:
        player.move_backward(delta_time)

    if keys_pressed[pygame.K_a]:
        player.move_left(delta_time)

    if keys_pressed[pygame.K_d]:
        player.move_right(delta_time)
    
    if keys_pressed[pygame.K_SPACE]:
        player.boost(delta_time)

    if pygame.mouse.get_pressed()[0]: # left click
        player.shoot()"""


def update_objects(delta_time):
    """Updates all objects, e.g. adjusts positions based on velocity"""

    # Loop until every object has been updated e.g. moved
    # Entity set has to be copied as entity might be deleted from the actual set
    for object in game.objects:
        
        # Update object e.g. move it
        object.update(delta_time)


def main():
    """Main game loop"""

    delta_time = 1

    menu.Menu.running = False

    running = True
    while running:
        time1 = perf_counter()

        keys_pressed = pygame.key.get_pressed()

        handle_player_input(keys_pressed, delta_time)
        update_objects(delta_time)

        draw_window()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()

            elif event.type == pygame.VIDEORESIZE:
                update_playing_screen_size()

            elif event.type == pygame.KEYDOWN and event.__dict__["key"] == pygame.K_ESCAPE:

                # Fix delta_time so that time paused is not included
                start = perf_counter()

                menu.Menu.pause()

                # Correct time1
                time1 = perf_counter() - start + time1
                
        time2 = perf_counter()
        delta_time = time2 - time1


def main_menu():
    """Initializes Menu"""
    menu.Menu()


if __name__ == "__main__":
    main_menu()