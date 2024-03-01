# Potrzebne importy
import os
import random

import pygame
from pygame.locals import *

def lerp(x, y, a):
    return x + (y - x) * a



SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720


# Inicjalizacja wszystkich mechanizmów pythona (po prostu to jest ważne);
pygame.init()

# Parametry Screena
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Zegar kontrolujący FPS-y
clock = pygame.time.Clock()

font = pygame.font.SysFont(None, 24)

x = 100
y = 100

xVel = 0
yVel = 0
length = 5
width = 50
height = 50

GRAVITY = 0.1
RESISTANCE = 0.02

speed = 0.4

path = []



xBall = random.randint(50, SCREEN_WIDTH - 50)
yBall = random.randint(50, SCREEN_HEIGHT - 50)

# Pętla gry
running = True
while running:

    # Te cztery linijki pozwalają nam normalnie zamknąć program.
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            break

    keys = pygame.key.get_pressed()

    yVel += GRAVITY


    if keys[K_w]:
        yVel -= speed
    if keys[K_s]:
        yVel += speed
    if keys[K_a]:
        xVel -= speed
    if keys[K_d]:
        xVel += speed

    xVel *= (1 - RESISTANCE)
    yVel *= (1 - RESISTANCE)

    x += xVel
    y += yVel

    if x < 0:
        x = 0
        xVel *= -1

    if x > SCREEN_WIDTH - height:
        x = SCREEN_WIDTH - height
        xVel *= -1

    if y < 0:
        y = 0
        yVel = 0

    if y > SCREEN_HEIGHT - height:
        y = SCREEN_HEIGHT - height
        yVel = 0



    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)

    path.append((Rect(x, y, width, height), (r, g, b)))
    if len(path) > length:
        path.pop(0)

    # Rysowanie grafiki:

    if pygame.Rect(x, y, width, height).colliderect(pygame.Rect(xBall, yBall, 50, 50)):
        xBall = random.randint(50, SCREEN_WIDTH - 50)
        yBall = random.randint(50, SCREEN_HEIGHT - 50)
        length += 5

    # Wypełnienie okienka kolorem
    screen.fill((0, 0, 0))


    # Rysowanie kształtu
    for i, (rect, color) in enumerate(path):
        pygame.draw.rect(screen, (color[0] * (1 * i) / length, color[1] * (1 * i) / length, color[2] * (1 * i) / length), rect.scale_by((i + 1)/length))

    pygame.draw.rect(screen, (255, 255, 255), Rect(x - 3, y - 3, 56, 56))
    pygame.draw.rect(screen, (255, 255, 0), Rect(x, y, 50, 50))

    pygame.draw.ellipse(screen, (255, 255, 255), Rect(xBall, yBall, 50, 50))
    pygame.draw.ellipse(screen, (255, 0, 0), Rect(xBall + 5, yBall + 5, 40, 40))

    # Wyświetlanie współrzędnych x i y
    pygame.draw.circle(screen, (255, 0, 0), (x, y), 4)

    text = font.render(f'x: {int(x)}, y: {int(y)}', True, (255, 0, 0))
    screen.blit(text, (x, y - 30))


    # Czekanie na kolejną klatkę
    clock.tick(60)
    # Aktualizacja gry
    pygame.display.flip()

pygame.quit()