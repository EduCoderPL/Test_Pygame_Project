import pygame
from pygame.locals import *

from scripts.objects.gameObject import GameObject


class Wall(GameObject):
    def __init__(self, x, y, width, height, game):
        super().__init__(x, y, width, height, game)
        self.set_color((128, 128, 128))

    def draw(self, offset=(0, 0)):
        super().draw(offset)
