import pygame

class Invader(pygame.sprite.Sprite):
    def __init__(self, image, screen):
        self.image = image
        
        self.image.set_colorkey((255, 0, 255))
        self.rect = self.image.get_rect(topleft = (0, 0)) 
        
        self.active = False
        self.vectorX = 10
        self.vectorY = 10

        self.screen = screen
        
    def update(self):
        if (self.active):
            self.rect.move_ip(self.vectorX, self.vectorY)
            self.vectorX += 10
            self.vectorY += 3
            self.rect.clamp_ip(self.screen.get_rect())

