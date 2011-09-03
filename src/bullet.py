import pygame

class Bullet(pygame.sprite.Sprite):
    def __init__(self, properties,player_pos = 0):
        pygame.sprite.Sprite.__init__(self)
        
        self.properties = properties   
        self.image = properties.anim_images[0]
        self.area = pygame.display.get_surface()
        self.area_rect = self.area.get_rect()
        
        self.active = True
        
        self.vectorX = self.properties.vectorX
        self.vectorY = self.properties.vectorY
        
        self.anim_frame = 0
        self.anim_delay_count = 0
        self.destroyed = False
        self.exploding = False
        self.sound_playing = False
        
        self.rect = self.image.get_rect()
        self.rect.midtop = player_pos
        self.properties.sound.play()
        
    def update(self):
        
        if self.active: self._animate()
        if self.exploding:self._explode()
                 
            
#    def _animate(self):
#        if self.anim_delay_count > self.properties.ANIM_DELAY:
#            self.anim_delay_count = 0
#            self._move()
#        self.anim_delay_count += 1 

    def _animate(self):
        if self.anim_delay_count > self.properties.ANIM_DELAY:
            self.anim_delay_count = 0
            if self.anim_frame >= len(self.properties.anim_images):
                self.anim_frame = 0        
            self.image = self.properties.anim_images[self.anim_frame]
            self.anim_frame += 1
                
            self._move()
                
        self.anim_delay_count += 1
        
    def _explode(self):
        if self.anim_delay_count > self.properties.ANIM_DELAY:
            self.anim_delay_count = 0
            
            if not self.sound_playing:
                self.sound_playing = True
                self.properties.sound.play()
                
            if self.anim_frame >= len(self.properties.exp_images):
                self.destroyed = True   
                
                return
            self.image = self.properties.exp_images[self.anim_frame]
            self.anim_frame += 1     
             
    def _move(self):
        newpos = self.rect.move((self.vectorX,-self.vectorY))        
        if not self.area_rect.contains(newpos): self.destroyed = False
        self.rect = newpos

 
#    def __del__(self):
#        print 'bullet removed'