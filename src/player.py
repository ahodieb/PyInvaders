import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self, width, height, offset):

        pygame.sprite.Sprite.__init__(self)
        self.window_width = width
        self.window_height = height
        self.offset = offset
        
        self.image =  pygame.image.load('../gfx/player.png')
        self.image.set_colorkey ((255, 0, 255))

        # initial player position        
        self.rect = self.image.get_rect().move(width/2, height - offset)
        
    def update(self, keyType):
        keystate = pygame.key.get_pressed()
        
        if keyType is True:
        
            if keystate[pygame.K_LEFT]:
                self.rect.move_ip(-7, 0)
            
            if keystate[pygame.K_RIGHT]:
                self.rect.move_ip(7, 0)
        else:
            #move by mouse
            pos = x, y = pygame.mouse.get_pos()
            self.rect.midtop = (x, self.window_height - self.offset)

