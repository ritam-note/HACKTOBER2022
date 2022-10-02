import pygame
import time
import random

cellSize = 40
notFinished = True

width = 800
heigth = 800
cols = int(width / cellSize)
rows = int(heigth / cellSize)

w = int(width / cellSize)
h = int(heigth / cellSize)

grid = [[0 for x in range(w)] for y in range(h)]
visited = []
stack = []
cell = 0


class Cell:
    def __init__(self, cellSize, x, y):
        self.cellSize = cellSize
        self.x = x
        self.y = y


def move_up(window, x, y):
    pygame.draw.rect(
        window,
        (0, 0, 255),
        (x * cellSize + 1, (y - 1) * cellSize + 1, cellSize - 1, (cellSize * 2 - 1)),
        0,
    )
    pygame.display.update()


def move_right(window, x, y):
    pygame.draw.rect(
        window,
        (0, 0, 255),
        (x * cellSize + 1, y * cellSize + 1, (cellSize * 2) - 2, cellSize - 2),
        0,
    )
    pygame.display.update()


def move_down(window, x, y):
    pygame.draw.rect(
        window,
        (0, 0, 255),
        (x * cellSize + 1, y * cellSize + 1, cellSize - 1, (cellSize * 2 - 1)),
        0,
    )
    pygame.display.update()


def move_left(window, x, y):
    pygame.draw.rect(
        window,
        (0, 0, 255),
        ((x - 1) * cellSize + 1, y * cellSize + 1, cellSize * 2 - 2, cellSize - 1),
        0,
    )
    pygame.display.update()
