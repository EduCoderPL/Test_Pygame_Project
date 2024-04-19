import pygame
from pygame.locals import *

from scripts.utils.constants import *
from scripts.managers.offsetManager import OffsetManager
from scripts.objects.player import Player

from scripts.managers.levelManager import LevelManager

class Game:

    def __init__(self):

        pygame.init()
        self.screenWidth = SCREEN_WIDTH
        self.screenHeight = SCREEN_HEIGHT
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.font = pygame.font.SysFont(None, 24)
        self.player = Player(150, 150, self)

        self.fileWithLevel = "level.txt"
        self.levelManager = LevelManager(self)
        self.levelManager.read_level(self.fileWithLevel)

        self.levelManager.add_walls()
        self.levelManager.add_enemies()
        self.offsetManager = OffsetManager()
        self.offset = (0, 0)
        self.targetOffset = (0, 0)

        self.game_loop()

    def game_loop(self):
        self.running = True
        while self.running:

            self.check_if_exit_clicked()
            mouseX, mouseY = self.manage_input()
            self.manage_offset(mouseX, mouseY)

            self.update()
            self.draw()

        self.levelManager.save_level(self.fileWithLevel)
        pygame.quit()


    def check_if_exit_clicked(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
                break

    def manage_input(self):
        keys = pygame.key.get_pressed()
        if keys[K_w]:
            self.player.yVel -= self.player.speed
        if keys[K_s]:
            self.player.yVel += self.player.speed
        if keys[K_a]:
            self.player.xVel -= self.player.speed
        if keys[K_d]:
            self.player.xVel += self.player.speed
        mouseX, mouseY = pygame.mouse.get_pos()
        return mouseX, mouseY

    def manage_offset(self, mouseX, mouseY):

        targetOffset = (
            self.player.rect.centerx - SCREEN_WIDTH // 2 + (mouseX - SCREEN_WIDTH // 2) * 0.5,
            self.player.rect.centery - SCREEN_HEIGHT // 2 + (mouseY - SCREEN_HEIGHT // 2) * 0.5
        )
        self.offsetManager.update_offset(targetOffset)
    def update(self):
        self.player.update()
        for enemy in self.levelManager.enemies:
            enemy.update()

    def draw(self):
        offset = self.offsetManager.get_offset()
        self.screen.fill((0, 0, 0))

        for wall in self.levelManager.walls:
            wall.draw(offset)

        for enemy in self.levelManager.enemies:
            enemy.draw(offset)

        self.player.draw(offset)
        self.clock.tick(60)
        pygame.display.flip()
