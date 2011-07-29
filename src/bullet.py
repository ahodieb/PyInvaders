import pygame,resource_loader

class Bullet(pygame.sprite.Sprite):
    def __init__(self, properties,player_pos = 0):
        pygame.sprite.Sprite.__init__(self)
        
        self.properties = properties   
        self.image = properties.anim_images[0]
        self.area = pygame.display.get_surface()
        self.area_rect = self.area.get_rect()

        #self.velocity = 35
        #self.damage   = 10
        
        self.active = True
        
        #self.ANIM_DELAY = 2
        self.anim_frame = 0
        self.anim_delay_count = 0
        self.exploding = False
        self.sound_playing = False
        
        self.rect = self.image.get_rect().move(player_pos) #player pos is a tuple of x, y
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
                self.active = False   
                
                return
            self.image = self.properties.exp_images[self.anim_frame]
            self.anim_frame += 1     
             
    def _move(self):
        newpos = self.rect.move((self.properties.vectorX,-self.properties.vectorY))        
        if not self.area_rect.contains(newpos): self.active = False
        self.rect = newpos

 
#    def __del__(self):
#        print 'bullet removed'
 