import pygame,random


class Invader(pygame.sprite.Sprite):
    def __init__(self, images,health):
        
        pygame.sprite.Sprite.__init__(self)
        self.area = pygame.display.get_surface()
        self.area_rect = self.area.get_rect()   
        self.images = images
        self.image = images[0]
        
        startx = random.randint(10, self.area.get_width() - 20)
        starty = random.randint(35, self.area.get_height() - 100)
        
        self.rect = self.image.get_rect(topleft = (startx, starty)) 
        
        self.active = False
        self.vectorX = 10
        self.vectorY = 0

        self.movement_type = 0
        
        self.ANIM_DELAY = 2
        self.anim_frame = 0
        self.anim_delay_count = 0
        
        self.health = health
        
        
    def update(self):
        random.seed()
        
        if self.health <= 0 : 
            self.active = False
            
        
        if (self.active):
            if self.anim_delay_count > self.ANIM_DELAY:
                self.anim_delay_count = 0
                if self.anim_frame >= len(self.images):
                    self.anim_frame = 0        
                self.image = self.images[self.anim_frame]
                self.anim_frame += 1
                
                self._move()
                
            self.anim_delay_count += 1
    
    def _move(self):
        newpos = self.rect.move((self.vectorX,0))
        
        if not self.area_rect.contains(newpos):
            if self.rect.left < self.area_rect.left or self.rect.right > self.area_rect.right:
                self.vectorX = -self.vectorX
                newpos = self.rect.move((self.vectorX, 0))
                
        self.rect = newpos
                          
#            if self.movement_type == 0:
#                # in this movement type the invader moves a long only one of x, y
#                select_coordinate = random.randint(0, 1)
#                if select_coordinate == 0:
#                    # move a long x coordinate
#                    self.rect.move_ip(self.vectorX, self.vectorY)
#                    self.vectorX += random.randint(0, 5)
#
#        if self.rect.centerx  == 600 or self.rect.centery == 468:
#            self.active = False

