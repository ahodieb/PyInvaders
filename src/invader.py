import pygame

class Invader(pygame.sprite.Sprite):
    def __init__(self, kind):
        if kind == 0:
            self.image = self.rect = pygame.image.load("../gfx/invader1.png")
        if kind == 1:
            self.image = self.rect = pygame.image.load("../gfx/invader2.png")
        self.image.set_colorkey((255, 0, 255))
        
        self.active = True
        
    def update(self):
        pass
