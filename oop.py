import os
import random
import pygame
from pygame.locals import *

class Player:

    def __init__(self, x: float, y: float):
        self.x: float = x
        self.y: float = y

        self.xVel: float = 0
        self.yVel: float = 0

        self.width: float = 50
        self.height: float = 50

        self.speed: float = 0.4

        self.rect: Rect = Rect(self.x, self.y, self.width, self.height)
        self.blobOffset = 13

        self.xDraw = 0
        self.yDraw = 0


    def update(self):

        self.yVel += GRAVITY

        self.xVel *= (1 - RESISTANCE)
        self.yVel *= (1 - RESISTANCE)

        self.solve_collisions(levelManager.walls)
        self.rect = Rect(self.x, self.y, self.width, self.height)

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


    def draw(self, offset):
        self.xDraw = self.x - offset[0]
        self.yDraw = self.y - offset[1]
        drawRect = Rect(self.xDraw, self.yDraw, self.width, self.height)

        pygame.draw.rect(screen, (255, 255, 255), drawRect.scale_by(1.1))
        pygame.draw.rect(screen, (255, 255, 0), drawRect)

        # # Wyświetlanie współrzędnych x i y
        # pygame.draw.circle(screen, (255, 0, 0), (self.x, self.y), 4)
        #
        # text = font.render(f'x: {int(self.x)}, y: {int(self.y)}', True, (255, 0, 0))
        # screen.blit(text, (self.x, self.y - 30))


class Coin:
    def __init__(self, x, y):
        self.x = x
        self.y = y

        self.rect = Rect(self.x, self.y, 30, 30)


    def set_random_position(self):
        randX = random.randint(50, SCREEN_WIDTH - 50)
        randY = random.randint(50, SCREEN_HEIGHT- 50)
        self.x, self.y = randX, randY
        self.rect = Rect(self.x, self.y, 30, 30)
    def draw(self):
        pygame.draw.rect(screen, (255, 255, 255), self.rect.scale_by(1.1))
        pygame.draw.rect(screen, (255, 0, 0), self.rect)

class Wall:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

        self.rect = Rect(self.x, self.y, self.width, self.height)
        self.xDraw = 0
        self.yDraw = 0

    def draw(self, offset=(0, 0)):
        self.xDraw = self.x - offset[0]
        self.yDraw = self.y - offset[1]

        drawRect = Rect(self.xDraw, self.yDraw, self.width, self.height)
        pygame.draw.rect(screen, (100, 100, 100), drawRect)

class LevelManager:

    TEMPLATE_LEVEL = [
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 1, 1, 1, 1, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 1, 0, 1, 0, 0, 1],
        [1, 0, 1, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 1, 1, 1, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    ]
    TILE_SIZE = 100

    def __init__(self, level=TEMPLATE_LEVEL, tileSize=TILE_SIZE):
        self.level = level
        self.tileSize = tileSize
        self.walls = []

    def add_walls(self):
        for y in range(len(self.level)):
            for x in range(len(self.level[0])):
                if self.level[y][x] == 1:
                    self.walls.append(
                        Wall(
                            x * self.tileSize,
                            y * self.tileSize,
                            self.tileSize,
                            self.tileSize)
                        )

    def save_level(self):
        file = open("level.txt", "w")
        for y in range(len(self.level)):
            for x in range(len(self.level[0])):
                file.write(str(self.level[y][x]))
            file.write("\n")
        file.close()

    def read_level(self):
        self.level = []
        file = open("level.txt", "r")
        for line in file.readlines():
            listFromFile = [*line[:-1]]
            listWithNumbers = [int(x) for x in listFromFile]
            self.level.append(listWithNumbers)

        file.close()
        return self.level

    def generate_random_level(self):
        for y in range(1, len(self.level) - 1):
            for x in range(1, len(self.level[0]) - 1):
                self.level[y][x] = random.choice([0, 0, 0, 1])


def lerp(a, b, x):
    return a + (b - a) * x

SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 24)
player = Player(150, 150)
walls = []
levelManager = LevelManager()


levelManager.add_walls()

GRAVITY = 0.1
RESISTANCE = 0.02

offset = (0, 0)
targetOffset = (0, 0)

running = True
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            break

    keys = pygame.key.get_pressed()

    if keys[K_w]:
        player.yVel -= player.speed
    if keys[K_s]:
        player.yVel += player.speed
    if keys[K_a]:
        player.xVel -= player.speed
    if keys[K_d]:
        player.xVel += player.speed

    player.update()

    mouseX, mouseY = pygame.mouse.get_pos()

    targetOffset = (
        player.rect.centerx - SCREEN_WIDTH // 2 + (mouseX - SCREEN_WIDTH // 2) * 0.5,
        player.rect.centery - SCREEN_HEIGHT // 2 + (mouseY - SCREEN_HEIGHT // 2) * 0.5
    )

    offset = (
        lerp(offset[0], targetOffset[0], 0.1),
        lerp(offset[1], targetOffset[1], 0.1)
    )

    screen.fill((0, 0, 0))

    for wall in levelManager.walls:
        wall.draw(offset)

    player.draw(offset)

    clock.tick(60)
    pygame.display.flip()

levelManager.save_level()
pygame.quit()
