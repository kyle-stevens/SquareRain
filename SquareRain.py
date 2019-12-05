#!/usr/bin/python
# -*- coding: utf-8 -*-

import pygame
from pygame.locals import *
from array import *
import random

pygame.init()
pygame.font.init()


class Entity:

    x = 0
    y = 0

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def moveBlock(self):
        self.y = self.y + 1


def cleanupMarkers(player, x, markers):
    player = [Entity(x, 18)]
    markers = []


def gameloop():
    #change this to change size of window
    gameXY = 600
    blockWidth = gameXY / 20
    gamewindow = pygame.display.set_mode((gameXY, gameXY))

    def spriteObs(
        color,
        x,
        y,
        width,
        ):

        pygame.draw.rect(gamewindow, color, (x + 1, y + 1, width - 2,
                         width - 2))

    def spritePla(x, y, width):
        pygame.draw.rect(gamewindow, (255, 255, 255), (x + 1, y + 1,
                         width - 2, width - 2))

    pygame.display.set_caption('sirtet')
    black = (0, 0, 0)
    white = (255, 255, 255)
    enemyColor = (255, 255, 255)

    isDead = False
    Position = [
        [
            (),
            (),
            (),
            (),
            (),
            (),
            (),
            (),
            (),
            (),
            (),
            (),
            (),
            (),
            (),
            (),
            (),
            (),
            (),
            (),
            ],
        [
            (),
            (),
            (),
            (),
            (),
            (),
            (),
            (),
            (),
            (),
            (),
            (),
            (),
            (),
            (),
            (),
            (),
            (),
            (),
            (),
            ],
        [
            (),
            (),
            (),
            (),
            (),
            (),
            (),
            (),
            (),
            (),
            (),
            (),
            (),
            (),
            (),
            (),
            (),
            (),
            (),
            (),
            ],
        [
            (),
            (),
            (),
            (),
            (),
            (),
            (),
            (),
            (),
            (),
            (),
            (),
            (),
            (),
            (),
            (),
            (),
            (),
            (),
            (),
            ],
        [
            (),
            (),
            (),
            (),
            (),
            (),
            (),
            (),
            (),
            (),
            (),
            (),
            (),
            (),
            (),
            (),
            (),
            (),
            (),
            (),
            ],
        [
            (),
            (),
            (),
            (),
            (),
            (),
            (),
            (),
            (),
            (),
            (),
            (),
            (),
            (),
            (),
            (),
            (),
            (),
            (),
            (),
            ],
        [
            (),
            (),
            (),
            (),
            (),
            (),
            (),
            (),
            (),
            (),
            (),
            (),
            (),
            (),
            (),
            (),
            (),
            (),
            (),
            (),
            ],
        [
            (),
            (),
            (),
            (),
            (),
            (),
            (),
            (),
            (),
            (),
            (),
            (),
            (),
            (),
            (),
            (),
            (),
            (),
            (),
            (),
            ],
        [
            (),
            (),
            (),
            (),
            (),
            (),
            (),
            (),
            (),
            (),
            (),
            (),
            (),
            (),
            (),
            (),
            (),
            (),
            (),
            (),
            ],
        [
            (),
            (),
            (),
            (),
            (),
            (),
            (),
            (),
            (),
            (),
            (),
            (),
            (),
            (),
            (),
            (),
            (),
            (),
            (),
            (),
            ],
        [
            (),
            (),
            (),
            (),
            (),
            (),
            (),
            (),
            (),
            (),
            (),
            (),
            (),
            (),
            (),
            (),
            (),
            (),
            (),
            (),
            ],
        [
            (),
            (),
            (),
            (),
            (),
            (),
            (),
            (),
            (),
            (),
            (),
            (),
            (),
            (),
            (),
            (),
            (),
            (),
            (),
            (),
            ],
        [
            (),
            (),
            (),
            (),
            (),
            (),
            (),
            (),
            (),
            (),
            (),
            (),
            (),
            (),
            (),
            (),
            (),
            (),
            (),
            (),
            ],
        [
            (),
            (),
            (),
            (),
            (),
            (),
            (),
            (),
            (),
            (),
            (),
            (),
            (),
            (),
            (),
            (),
            (),
            (),
            (),
            (),
            ],
        [
            (),
            (),
            (),
            (),
            (),
            (),
            (),
            (),
            (),
            (),
            (),
            (),
            (),
            (),
            (),
            (),
            (),
            (),
            (),
            (),
            ],
        [
            (),
            (),
            (),
            (),
            (),
            (),
            (),
            (),
            (),
            (),
            (),
            (),
            (),
            (),
            (),
            (),
            (),
            (),
            (),
            (),
            ],
        [
            (),
            (),
            (),
            (),
            (),
            (),
            (),
            (),
            (),
            (),
            (),
            (),
            (),
            (),
            (),
            (),
            (),
            (),
            (),
            (),
            ],
        [
            (),
            (),
            (),
            (),
            (),
            (),
            (),
            (),
            (),
            (),
            (),
            (),
            (),
            (),
            (),
            (),
            (),
            (),
            (),
            (),
            ],
        [
            (),
            (),
            (),
            (),
            (),
            (),
            (),
            (),
            (),
            (),
            (),
            (),
            (),
            (),
            (),
            (),
            (),
            (),
            (),
            (),
            ],
        [
            (),
            (),
            (),
            (),
            (),
            (),
            (),
            (),
            (),
            (),
            (),
            (),
            (),
            (),
            (),
            (),
            (),
            (),
            (),
            (),
            ],
        ]

    for i in range(0, 20):
        for j in range(0, 20):
            Position[i][j] = (blockWidth * i, blockWidth * j)
        print (Position[i])
    x = 10
    running = True
    notDead = True
    timer = 0

    player = [Entity(x, 18)]
    markers = []

    while running:

        font = pygame.font.Font('freesansbold.ttf', 32)

        if timer < 250:
            if timer % 4 == 0:
                markers.append(Entity(random.randint(0, 19), 0))
        elif timer < 500 and timer > 250:

            if timer % 3 == 0:
                markers.append(Entity(random.randint(0, 19), 0))
        else:

            if timer % 2 == 0:
                markers.append(Entity(random.randint(0, 19), 0))

        for event in pygame.event.get():
            if event.type == QUIT:
                running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                print ('menu')
                running = False
            elif event.key == pygame.K_RIGHT:
                x = x + 1
            elif event.key == pygame.K_LEFT:
                x = x - 1
            elif event.key == pygame.K_SPACE:
                if not notDead:
                    player = [Entity(x, 18)]
                    markers = []
                    x = 10
                    timer = 1
                    notDead = True


        if x > 19:
            x = 19
        elif x < 0:
            x = 0
        gamewindow.fill((0, 0, 0))
        for i in range(0, 20):
            for j in range(0, 20):
                if j == x and i == 18 and notDead:
                    spriteObs((0, 255, 0), Position[i][j][1],
                              Position[i][j][0], blockWidth)
                else:
                    spriteObs((0, 0, 0), Position[i][j][1],
                              Position[i][j][0], blockWidth)

                for O in markers:
                    if j == O.x and i == O.y:
                        spriteObs(enemyColor, Position[i][j][1],
                                  Position[i][j][0], blockWidth)

        for O in markers:
            if O.y > 19:
                markers.remove(O)
            elif O.x == x and O.y == 18:

                O.moveBlock()
                pygame.display.update()
                notDead = False
                cleanupMarkers(player, x, markers)

            O.moveBlock()

        text = font.render(str(timer), True, (255, 255, 255))
        textRect = text.get_rect()
        textRect.center = (200, 100)
        if notDead:
            text0 = font.render('', True, (255, 255, 255))
            text = font.render(str(timer), True, (255, 255, 255))
            text2 = font.render('', True, (255, 255, 255))
            timer = timer + 1
        else:
            text0 = font.render(str(timer), True, (255, 255, 255))
            text = font.render('GAME OVER', True, (255, 255, 255))
            text2 = font.render('Press Space to Restart', True, (255,
                                255, 255))

        text0Rect = text0.get_rect()
        text0Rect.center = (gameXY // 2, gameXY // 2 - 140)
        textRect = text.get_rect()
        textRect.center = (gameXY // 2, gameXY // 2 - 100)
        text2Rect = text2.get_rect()
        text2Rect.center = (gameXY // 2, gameXY // 2 + 40 - 100)
        gamewindow.blit(text, textRect)
        gamewindow.blit(text2, text2Rect)
        gamewindow.blit(text0, text0Rect)

        pygame.display.update()

        if timer < 500:
            pygame.time.delay(50)
        elif timer > 500 and timer < 1000:
            pygame.time.delay(45)
        elif timer > 1000 and timer < 1500:

            pygame.time.delay(40)
        elif timer > 1500 and timer < 2000:

            pygame.time.delay(30)
        else:

            pygame.time.delay(25)


gameloop()
