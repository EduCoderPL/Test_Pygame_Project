import pygame
from pygame.locals import *

from scripts.objects.gameObject import GameObject
from scripts.utils.constants import *


class Enemy(GameObject):
    def __init__(self, x, y, game):
        super().__init__(x, y, 50, 50, game)

        self.xVel: float = 0
        self.yVel: float = 0
        self.speed: float = 0.4
        self.accCoefficient = 0.4
        self.set_color((255, 0, 0))

    def update(self):

        self.moveToTarget(self.game.player)

        self.xVel *= (1 - RESISTANCE)
        self.yVel *= (1 - RESISTANCE)

        self.solve_collisions(self.game.levelManager.walls)
        self.solve_collisions_moving(self.game.levelManager.enemies)
        super().update()

    def moveToTarget(self, target):
        targetX, targetY = target.x, target.y

        vectorToTargetX = targetX - self.x
        vectorToTargetY = targetY - self.y

        vectorToTargetLength = (vectorToTargetX ** 2 + vectorToTargetY ** 2) ** 0.5

        vectorToTargetNormalizedX = vectorToTargetX / vectorToTargetLength
        vectorToTargetNormalizedY = vectorToTargetY / vectorToTargetLength

        xAcc = vectorToTargetNormalizedX * self.accCoefficient
        yAcc = vectorToTargetNormalizedY * self.accCoefficient

        self.xVel += xAcc
        self.yVel += yAcc

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

    def solve_collisions_moving(self, objects):
        pass
        # for obj in objects:
        #     if obj != self:  # Avoiding self-collision check
        #         if self.rect.colliderect(obj.rect):
        #             # Calculate direction to move away from the collided object
        #             if self.x + self.width > obj.x:
        #                 diff = abs(self.x + self.width - obj.x)
        #                 self.x -= diff
        #                 obj.x += diff
        #                 self.rect = Rect(self.x, self.y, self.width, self.height)
        #                 obj.rect = Rect(obj.x, obj.y, obj.width, obj.height)
        #                 self.xVel = 0
        #             if self.x < obj.x + obj.width:
        #                 diff = abs(obj.x + obj.width - self.x)
        #                 self.x += diff
        #                 obj.x -= diff
        #                 self.rect = Rect(self.x, self.y, self.width, self.height)
        #                 obj.rect = Rect(obj.x, obj.y, obj.width, obj.height)
        #                 obj.xVel = 0
        #             if self.y + self.width > obj.y:
        #                 diff = abs(self.y + self.height - obj.y)
        #                 self.y -= diff
        #                 obj.y += diff
        #                 self.rect = Rect(self.x, self.y, self.width, self.height)
        #                 obj.rect = Rect(obj.x, obj.y, obj.width, obj.height)
        #                 self.yVel = 0
        #             if self.y < obj.y + obj.height:
        #                 diff = abs(obj.y + obj.height - self.y)
        #                 self.y += diff
        #                 obj.y -= diff
        #                 self.rect = Rect(self.x, self.y, self.width, self.height)
        #                 obj.rect = Rect(obj.x, obj.y, obj.width, obj.height)
        #                 obj.yVel = 0


    def draw(self, offset=(0, 0)):
        super().draw(offset)