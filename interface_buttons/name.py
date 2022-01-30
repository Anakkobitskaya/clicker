import pygame


class Name:
    def __init__(self):
        self.image = pygame.image.load('img/name.png')
        self.pos = (650, 0)

    def draw(self, sc):
        self.name.draw(sc)