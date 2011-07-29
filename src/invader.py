import pygame,random

class Invader(pygame.sprite.Sprite):
    def __init__(self, properties):
        
        pygame.sprite.Sprite.__init__(self)
        self.area = pygame.display.get_surface()
        self.area_rect = self.area.get_rect()
        self.properties = properties   
        #self.anim_images = anim_images
        #self.exp_images = exp_images
        
        self.image = properties.anim_images[0]
        
        startx = random.randint(10, self.area.get_width() - 20)
        starty = random.randint(35, self.area.get_height() - 100)
        
        self.rect = self.image.get_rect(topleft = (startx, starty)) 
        
        self.vectorX = self.properties.vectorX
        self.vectorY = self.properties.vectorY

        #self.movement_type = 0
        
        #self.ANIM_DELAY = 2
        self.anim_frame = 0
        self.anim_delay_count = 0
        
        self.active = False
        self.dead = False
        self.exploding = False
        self.sound_playing = False
        self.health = self.properties.health
        
        
        
    def update(self):
        if self.active: self._animate()
        if self.exploding:self._explode()
            
    def _animate(self):
        if self.anim_delay_count > self.properties.ANIM_DELAY:
            self.anim_delay_count = 0
            if self.anim_frame >= len(self.properties.anim_images):
                self.anim_frame = 0        
            self.image = self.properties.anim_images[self.anim_frame]
            self.anim_frame += 1
                
            self._move()
                
        self.anim_delay_count += 1
        #self.exploding = self.health <= 0
        
    def _explode(self):
        if self.anim_delay_count > self.properties.ANIM_DELAY:
            self.anim_delay_count = 0
            
            if not self.sound_playing:
                self.sound_playing = True
                self.properties.sound.play()
                
            if self.anim_frame >= len(self.properties.exp_images):
                self.dead = True   
                
                return
            self.image = self.properties.exp_images[self.anim_frame]
            self.anim_frame += 1     
                       
        
    def _move(self):
        newpos = self.rect.move((self.vectorX,0))
        
        if not self.area_rect.contains(newpos):
            if self.rect.left < self.area_rect.left or self.rect.right > self.area_rect.right:
                self.vectorX = -self.vectorX
                newpos = self.rect.move((self.vectorX, 0))
                
        self.rect = newpos
   
     
  
    def hit_test(self,objects):
        if self.exploding or not self.active:
            return []
        
        collisions = []
        for i in xrange(len(objects)):
            
            hit = self.rect.colliderect(objects[i].rect)
            if hit : 
                collisions.append(i)
                self.health -= objects[i].properties.damage
                objects[i].exploding = True
                if self.health <= 0 :
                    self.anim_frame = 0
                    self.exploding  = True
                self.vectorX*=2 # increas speed after hit 
                #objects[i].active = False
        return collisions    
    