import pygame
from pygame.locals import *

class GameObject:
    def __init__(self, x: float, y: float, width: float, height: float, game):

        self.x: float = x
        self.y: float = y

        self.width: float = width
        self.height: float = height

        self.rect: Rect = Rect(self.x, self.y, self.width, self.height)

        self.xDraw = 0
        self.yDraw = 0

        self.game = game
        self.color = (255, 0, 0)

    def set_color(self, color):
        self.color = color

    def update(self):
        self.rect = Rect(self.x, self.y, self.width, self.height)

    def draw(self, offset=(0, 0)):
        self.xDraw = self.x - offset[0]
        self.yDraw = self.y - offset[1]
        drawRect = Rect(self.xDraw, self.yDraw, self.width, self.height)
        pygame.draw.rect(self.game.screen, self.color, drawRect)
