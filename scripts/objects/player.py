
import pygame
from pygame.locals import *

from scripts.objects.gameObject import GameObject
from scripts.utils.constants import *


class Player(GameObject):

    def __init__(self, x: float, y: float, game):
        super().__init__(x, y, 50, 50, game)

        self.xVel: float = 0
        self.yVel: float = 0
        self.speed: float = 0.4

        self.set_color((255, 255, 0))

    def update(self):
        self.xVel *= (1 - RESISTANCE)
        self.yVel *= (1 - RESISTANCE)

        self.solve_collisions(self.game.levelManager.walls)
        super().update()

    def solve_collisions(self, walls):
        self.x += self.xVel
        self.rect = Rect(self.x, self.y, self.width, self.height)
        for wall in walls:
            if self.rect.colliderect(wall.rect):
                if self.xVel > 0:
                    self.x = wall.x - self.width
                    self.xVel = 0
                if self.xVel < 0:
                    self.x = wall.x + wall.width
                    self.xVel = 0
            self.rect = Rect(self.x, self.y, self.width, self.height)

        self.y += self.yVel
        self.rect = Rect(self.x, self.y, self.width, self.height)

        for wall in walls:
            if self.rect.colliderect(wall.rect):
                if self.yVel > 0:
                    self.y = wall.y - self.height
                    self.yVel = 0
                if self.yVel < 0:
                    self.y = wall.y + wall.height
                    self.yVel = 0
            self.rect = Rect(self.x, self.y, self.width, self.height)


    def draw(self, offset=(0, 0)):
        super().draw(offset)