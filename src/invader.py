import pygame,random


class Invader(pygame.sprite.Sprite):
    def __init__(self, image):
        
        pygame.sprite.Sprite.__init__(self)

        self.image = image
        
        self.image.set_colorkey((255, 0, 255))
        self.rect = self.image.get_rect(topleft = (0, 0)) 
        
        self.active = False
        self.vectorX = 0
        self.vectorY = 0

        self.movement_type = 0
        self.time_delay = 0
        
        
    def update(self):
        random.seed()

        if (self.active):
            if self.movement_type == 0:
                # in this movement type the invader moves a long only one of x, y
                select_coordinate = random.randint(0, 1)
                if select_coordinate == 0:
                    # move a long x coordinate
                    self.rect.move_ip(self.vectorX, self.vectorY)
                    self.vectorX += random.randint(0, 5)

        if self.rect.centerx  == 600 or self.rect.centery == 468:
            self.active = False


