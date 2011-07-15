import pygame,resource_loader

class Bullet(pygame.sprite.Sprite):
    def __init__(self, player_pos = 0):
        pygame.sprite.Sprite.__init__(self)
        
        self.image = resource_loader.load_image('bullet1.png', -1)
        self.area = pygame.display.get_surface()
        self.area_rect = self.area.get_rect()

        self.velocity = 35

        #bullet positioning
        self.rect = self.image.get_rect().move(player_pos) #player pos is a tuple of x, y

        def update(self):
            self.rect.move_ip(self.velocity, 0)
