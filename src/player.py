import pygame,resource_loader

class Player(pygame.sprite.Sprite):
    def __init__(self):
        self.PLAYER_OFFSET = 25
        self.PLAYER_SPEED =  10 
        pygame.sprite.Sprite.__init__(self)
        
        self.area = pygame.display.get_surface()
        self.area_rect = self.area.get_rect()    
        self.image = resource_loader.load_image('player.png', -1)
        
        #initial player position        
        self.rect = self.image.get_rect().move(self.area.get_width()/2, self.area.get_height() - self.PLAYER_OFFSET)
        
    def update(self, keyType):
        keystate = pygame.key.get_pressed()
        
        if keyType is True:
        
            d = 1 #direction
            if keystate[pygame.K_LEFT]:
                d = -1    
            if keystate[pygame.K_RIGHT]:
                d = 1    

            if keystate[pygame.K_LEFT] or keystate[pygame.K_RIGHT]:
                        
                self.rect.move_ip(d * self.PLAYER_SPEED, 0)
                area_rect = self.area.get_rect()

                if self.rect.left < area_rect.left:
                    self.rect.left = area_rect.left
                
                if self.rect.right > area_rect.right:
                    self.rect.right = area_rect.right
                
        else:
            #move by mouse
            x, y = pygame.mouse.get_pos()
            self.rect.midtop = (x, self.area.get_height() - self.PLAYER_OFFSET)

