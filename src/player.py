import pygame

class Player():
    def __init__(self,width,height,offset,Speed,Screen):

        #pygame.sprite.Sprite.__init__(self)
                
        #self.x_pos = width/2
        #self.y_pos = height - offset
        self.speed = Speed
        
        self.window_width = width
        self.window_height = height
        
        self.img =  pygame.image.load('../gfx/player.png')
        self.img.set_colorkey ((255,0,255))
        
        self.rect = self.img.get_rect().move(width/2,height - offset)
        
        
    def move(self,direction):
        #1 = right
        #0 = left
        if direction : self.rect.move_ip(self.speed,0)
        else : self.rect.move_ip(-self.speed,0)
        
        if self.rect.left < 0 : self.rect.left = 0
        if self.rect.right >self.window_width : self.rect.right = self.window_width
        