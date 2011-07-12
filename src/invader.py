import pygame,random


class Invader(pygame.sprite.Sprite):
    def __init__(self, image):
        self.image = image
        
        self.image.set_colorkey((255, 0, 255))
        self.rect = self.image.get_rect(topleft = (0, 0)) 
        
        self.active = False
        self.vectorX = 1
        self.vectorY = 3
        
        
        
    def update(self):
        
        if (self.active):
            random.seed()
            self.rect.move_ip(self.vectorX, self.vectorY)
            self.vectorX += random.randint(0,10)
            self.vectorY += random.randint(0,10)

