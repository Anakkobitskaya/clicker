import pygame

class Seed:
    def __init__(self):
        self.count = 0
        self.image = pygame.image.load(r'img/seen.png')
        self.pos = (750, 0)
