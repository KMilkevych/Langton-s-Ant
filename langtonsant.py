import pygame
from pygame.locals import *
import random

class Ant():

    def __init__(self, pos = [100, 100], dir = [0, 1], color = (255, 0, 0)):
        self.pos = pos
        self.dir = dir
        self.color = color
        if color == (255, 0, 0):
            self.anttype = "RED"
    
    def turn(self, dir = 1):
        if dir == 1:
            self.dir = [self.dir[1], -self.dir[0]]
        else:
            self.dir = [-self.dir[1], self.dir[0]]
    
    def move(self):
        self.pos = [self.pos[0] + self.dir[0], self.pos[1] + self.dir[1]]

def updateants(ants, cells):
    changes = []
    for ant in ants:
        antpos = ant.pos
        try:
            val = cells[antpos[1]][antpos[0]]
        except:
            val = 0
        if ant.anttype == "RED":
            if val == 1:
                ant.turn(1) #Turn right if green
            else:
                ant.turn(0) #Turn left if black
        if val == 0:
            val = 1
        else:
            val = 0
        try:
            cells[antpos[1]][antpos[0]] = val
        except:
            pass   
        changes.append((antpos[0], antpos[1], val))
        ant.move()
    return changes

        


grid = (200, 200)
cell_size = 5

pygame.init()
window = pygame.display.set_mode((grid[0]*cell_size, grid[1]*cell_size))
pygame.display.set_caption("The Ant")


cells = [[0 for x in range(grid[0])] for y in range(0, grid[1])]

window.fill((0, 0, 0))
for y in range(grid[1]):
    for x in range(grid[0]):
        window.fill((0, cells[y][x]*255, 0), ((x*cell_size, y*cell_size), (cell_size, cell_size)))

redAnt = Ant([50, 100])
blueAnt = Ant([150, 100])
ants = [redAnt, blueAnt]

clock = pygame.time.Clock()
running = True
updating = False
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            continue
        if event.type == pygame.KEYDOWN:
            updating = True
    
    if not updating:
        continue

    changes = updateants(ants, cells)
    for change in changes:
        window.fill((0, change[2]*255, 0), ((change[0]*cell_size, change[1]*cell_size), (cell_size, cell_size)))

    for ant in ants:
        window.fill(ant.color, ((ant.pos[0]*cell_size, ant.pos[1]*cell_size), (cell_size, cell_size)))

    pygame.display.update()
    clock.tick(120)