import pygame
import random

class Fish:
    id = 0
    y = -500
    x = random.randint(0,40*3)
    def __init__(self, filename):
        self.id += 1
        self.image = pygame.image.load(filename)
        self.rect = pygame.Rect(self.x, self.y, 40, 20)

    def  getImage(self):
        return self.image

    def Move(self):
        self.rect.move_ip(0, 1)

    def newX(self):
#        self.x = random.randint(0, 40*3)
#        self.rect.move_ip(random.randint(0, 40*3))
        self.rect.x = random.randint(0, 40*3)
