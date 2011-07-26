import pygame,random


class Invader(pygame.sprite.Sprite):
    def __init__(self, anim_images,exp_images,health):
        
        pygame.sprite.Sprite.__init__(self)
        self.area = pygame.display.get_surface()
        self.area_rect = self.area.get_rect()   
        self.anim_images = anim_images
        
        self.image = anim_images[0]
        self.exp_images = exp_images
        
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
        self.dead = False
        self.exploding = False
        
        
        
    def update(self):
        random.seed()
        
#        if self.health <= 0 : 
#            self.active = False
#            
        
        if (self.active):
            if self.anim_delay_count > self.ANIM_DELAY:
                self.anim_delay_count = 0
                if self.anim_frame >= len(self.anim_images):
                    self.anim_frame = 0        
                self.image = self.anim_images[self.anim_frame]
                self.anim_frame += 1
                
                self._move()
                
            self.anim_delay_count += 1
            self.exploding = self.health <= 0
            
            
        if self.exploding:
            if self.anim_delay_count > self.ANIM_DELAY:
                self.anim_delay_count = 0
                if self.anim_frame >= len(self.exp_images):
                    self.dead = True   
                    return
                self.image = self.exp_images[self.anim_frame]
                self.anim_frame += 1            
            

    def _move(self):
        newpos = self.rect.move((self.vectorX,0))
        
        if not self.area_rect.contains(newpos):
            if self.rect.left < self.area_rect.left or self.rect.right > self.area_rect.right:
                self.vectorX = -self.vectorX
                newpos = self.rect.move((self.vectorX, 0))
                
        self.rect = newpos
   
     
    def __del__(self):
        print 'invader removed'
 
    def hit_test(self,objects):
        collisions = []
        for i in xrange(len(objects)):
            
            hit = self.rect.colliderect(objects[i].rect)
            if hit : 
                collisions.append(i)
                #objects[i].active = False
                self.health -= objects[i].damage
                self.vectorX*=2 # increas speed after hit 
                objects[i].active = False
                self.anim_frame = 0 # 3WZA NADAFA 
        return collisions    
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

