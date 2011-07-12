import pygame,sys,copy
import player
import invader

def main():
    FPS = 60
    MAX_BULLETS = 10
    MAX_INVADERS = 4
    PLAYER_OFFSET = 25
    game_loop = True
    
    pygame.init()
    
    clock = pygame.time.Clock()
    size = width , height = 600 , 468
    screen = pygame.display.set_mode(size)
    
    icon = pygame.image.load('../gfx/icon.png')
    invader1 = pygame.image.load('../gfx/invader1.png').convert()
    invader2 = pygame.image.load('../gfx/invader2.png').convert()
    bullet = pygame.image.load('../gfx/bullet1.png').convert()
    
    #this background should be replaced by the background image
    background = pygame.surface.Surface((size),0,None)
    background.fill((130,21,138))
    
    screen.blit(background,background.get_rect())
    
    pygame.display.set_icon(icon)
    pygame.display.set_caption('PyInvaders')
    
    bullets = []
    for i in range(MAX_BULLETS):
        bullets.append(copy.deepcopy(bullet))
        
    invaders = []
    for i in range(MAX_INVADERS):
        invaders.append(invader.Invader(invader1, screen))
        invaders.append(invader.Invader(invader2, screen))
    
    p = player.Player(width, height, PLAYER_OFFSET, screen)
    
    while game_loop :       
        
        #clear old position
        screen.blit(background, p.rect)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_loop = not game_loop            
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    game_loop = not game_loop
                
        p.update()
        invaders[1].active = True
        invaders[1].update()
        # in the new position
        screen.blit(p.img,p.rect)
        
        clock.tick(FPS)    
        pygame.display.update()
        pygame.display.flip()
    pygame.quit()
    
    

if __name__ == '__main__':
    main()
