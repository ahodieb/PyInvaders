import pygame,sys,copy
import player
import invader

def main():
    FPS = 20
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
        invaders.append(invader.Invader(invader1))
        invaders.append(invader.Invader(invader2))
    
    p = player.Player(width, height, PLAYER_OFFSET)
    
    while game_loop :       
        
        #clear old position
        screen.blit(background, p.rect)
        for inv in invaders:
            screen.blit(background,inv.rect)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_loop = not game_loop            
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    game_loop = not game_loop
                
        p.update()
        # just for testing the invader
        invaders[1].active = True
        invaders[1].update()
        screen.blit(invaders[1].image,invaders[1].rect)
        
        
        # in the new position
        screen.blit(p.img,p.rect)
        
        #adding all invaders 
        for inv in invaders:
            inv.active = True
            inv.update()
            screen.blit(inv.image,inv.rect)
            #to slow things a bit
            pygame.time.wait(50)
        
        clock.tick(FPS)    
        pygame.display.update()
        pygame.display.flip()
    pygame.quit()
    
    

if __name__ == '__main__':
    main()
