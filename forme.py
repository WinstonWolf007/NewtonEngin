import pygame
import random


class Forme(pygame.sprite.Sprite):
    def __init__(self, name):
        super().__init__()
        self.color = [(42, 157, 143), (233, 196, 106), (244, 162, 97), (231, 111, 81)][random.randint(0, 3)]
        self.position = [random.randint(0, 1080), 0]
        if name in ['1', '2']:
            if name == '1':
                cote = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100][random.randint(0, 9)]
                self.size = [cote, cote]
            elif name == '2':
                self.size = [[100, 110, 120, 130, 140, 150][random.randint(0, 5)], [10, 20, 30, 40, 50, 60, 70, 80, 90, 100][random.randint(0, 9)]]
        self.rect = pygame.Rect(self.position[0], self.position[1], self.size[0], self.size[1])

    def updateGravity(self, f, direct):
        N = f/10 * (self.size[0]*self.size[1])
        if direct:
            if self.rect.y+self.size[1] < 920:
                self.rect.y += N + 1
            else:
                self.rect.y = 920-self.size[1]
        else:
            if self.rect.y > 0:
                self.rect.y -= N + 1
            else:
                self.rect.y = 0
