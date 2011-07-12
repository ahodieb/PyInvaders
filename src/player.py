import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self, width, height, offset, Screen):

        #pygame.sprite.Sprite.__init__(self)
        self.window_width = width
        self.window_height = height
        self.screen = Screen

        self.img =  pygame.image.load('../gfx/player.png')
        self.img.set_colorkey ((255, 0, 255))

        # initial player position        
        self.rect = self.img.get_rect().move(width/2, height - offset)
        
    def update(self):
        keystate = pygame.key.get_pressed()
        
        if keystate[pygame.K_LEFT]:
            self.rect.move_ip(-7, 0)
            
        if keystate[pygame.K_RIGHT]:
            self.rect.move_ip(7, 0)

        self.rect.clamp_ip(self.screen.get_rect())

