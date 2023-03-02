from objects import Vector, Entity
import images
import game
import pygame



# Example:
class Ship(Entity):
    def __init__(self, position, velocity, rotation=0, health=10, damage=2, image=images.DEFAULT) -> None:
        super().__init__(position, velocity, rotation, image)
        self.health = health
        self.damage = damage

    def shoot(self):
        """Fire bullet at an enemy"""