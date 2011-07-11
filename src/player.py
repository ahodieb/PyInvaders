import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self,width,height,offset,Speed,Screen):

        pygame.sprite.Sprite.__init__(self)
        
        self.img =  pygame.image.load('../gfx/player.png')
        self.img.set_colorkey ((255,0,255))
        self.rect = self.img.get_rect(topleft = (width/2,height-offset))
        
        self.x_pos = width/2
        self.y_pos = height - offset
        self.speed = Speed
        
        self.window_width = width
        self.window_height = height
        self.screen = Screen
    def update(self,direction):
        #1 = right
        #0 = left
        if direction : 
            self.x_pos += self.speed
        else :
            self.x_pos -= self.speed
        
        if self.x_pos < 0 : self.x_pos = 0
        if self.x_pos >self.window_width : self.xpos = self.window_width
        
        self.rect.clamp_ip(self.screen.get_rect())