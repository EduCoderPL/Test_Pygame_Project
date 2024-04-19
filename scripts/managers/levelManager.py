import random

from scripts.objects.enemy import Enemy
from scripts.objects.wall import Wall


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

    def __init__(self, game, level=TEMPLATE_LEVEL, tileSize=TILE_SIZE):
        self.level = level
        self.tileSize = tileSize
        self.walls = []
        self.enemies = []
        self.game = game

        self.matrix = []

    def add_walls(self):
        for y in range(len(self.level)):
            for x in range(len(self.level[0])):
                if self.level[y][x] == 1:
                    self.walls.append(
                        Wall(
                            x * self.tileSize,
                            y * self.tileSize,
                            self.tileSize,
                            self.tileSize,
                            self.game)
                        )

    def save_level(self, filepath):
        file = open(filepath, "w")
        for y in range(len(self.level)):
            for x in range(len(self.level[0])):
                file.write(str(self.level[y][x]))
            file.write("\n")
        file.close()

    def read_level(self, filepath):
        self.level = []
        file = open(filepath, "r")
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

    def add_enemies(self):
        for i in range(100):

            while True:
                randTileX = random.randint(0, len(self.level[0]) - 1)
                randTileY = random.randint(0, len(self.level) - 1)

                if self.level[randTileY][randTileX] == 0:
                    break

            x = randTileX * self.tileSize
            y = randTileY * self.tileSize
            self.enemies.append(Enemy(x, y, self.game))