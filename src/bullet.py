import pygame,resource_loader

class Bullet(pygame.sprite.Sprite):
    def __init__(self, player_pos = 0):
        pygame.sprite.Sprite.__init__(self)
        
        self.image = resource_loader.load_image('bullet1.png')
        self.area = pygame.display.get_surface()
        self.area_rect = self.area.get_rect()

        self.velocity = 35
        self.damage   = 10
        
        self.active = True
        
        self.ANIM_DELAY = 2
        self.anim_frame = 0
        self.anim_delay_count = 0
        
        self.rect = self.image.get_rect().move(player_pos) #player pos is a tuple of x, y
    
    def update(self):
        
        if (self.active):
            if self.anim_delay_count > self.ANIM_DELAY:
                self.anim_delay_count = 0

                self._move()
                
            self.anim_delay_count += 1 
                
    def _move(self):
        newpos = self.rect.move((0,-self.velocity))        
        if not self.area_rect.contains(newpos): self.active = False
        self.rect = newpos

 
    def __del__(self):
        print 'bullet removed'
 
#    def hit_test(self,objects):
#        collisions = []
#        for i in xrange(len(objects)):
#            
#            hit = self.rect.colliderect(objects[i].rect)
#            if hit : 
#                collisions.append(i)
#                #objects[i].active = False
#                objects[i].health -= self.damage
#                objects[i].vectorX*=2
#        self.active = not len(collisions)
#        return collisions
        