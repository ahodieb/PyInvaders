import pygame,sys,copy
import player

def main():
    FPS = 60
    MAX_BULLETS = 10
    MAX_INVADERS = 4
    PLAYER_OFFSET = 25
    PLAYER_SPEED = 10
    game_loop = True
    
    pygame.init()
    
    clock = pygame.time.Clock()
    size = width , height = 800 , 600
    screen = pygame.display.set_mode(size)
    
    icon = pygame.image.load('../gfx/icon.png')
    invader1 = pygame.image.load('../gfx/invader1.png')
    invader2 = pygame.image.load('../gfx/invader2.png')
    bullet = pygame.image.load('../gfx/bullet1.png')
    
    pygame.display.set_icon(icon)
    pygame.display.set_caption('pyInvaders')
    
    
    bullets = []
    for i in range(MAX_BULLETS):
        bullets.append(copy.deepcopy(bullet))
        
    invaders = []
    for i in range(MAX_BULLETS):
        invaders.append(copy.deepcopy(invader1))
        invaders.append(copy.deepcopy(invader2))
        
    #p = player.Player(0,0)
    p = player.Player(width,height,PLAYER_OFFSET,PLAYER_SPEED,screen)
    
    while game_loop :
       
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT : game_loop = not game_loop
            
            if event.type == pygame.KEYDOWN :
                if event.key == pygame.K_ESCAPE:game_loop = not game_loop
                
                if event.key == pygame.K_LEFT: 
                    screen.fill((0,0,0))
                    p.rect.move_ip(-PLAYER_SPEED,0)
                    
                if event.key == pygame.K_RIGHT: 
                    screen.fill((0,0,0))
                    p.rect.move_ip(PLAYER_SPEED,0)
                
                
        clock.tick(FPS)    
        screen.blit(p.img,p.rect)
        pygame.display.flip()
    pygame.quit()
    
    

if __name__ == '__main__':
    main()