import pygame, os, copy, random
import player
import invader

def main():
    FPS = 60
    MAX_BULLETS = 10
    MAX_INVADERS = 1
    PLAYER_OFFSET = 25
    game_loop = True
    input_type = False
    
    pygame.init()
    
    clock = pygame.time.Clock()
    size = width , height = 600 , 468
    screen = pygame.display.set_mode(size)
    
    icon = pygame.image.load('../gfx/icon.png')
    invader1 = pygame.image.load('../gfx/invader1.png').convert()
    invader2 = pygame.image.load('../gfx/invader2.png').convert()
    bullet = pygame.image.load('../gfx/bullet1.png').convert()
    
    #this background should be replaced by the background image
    background = pygame.surface.Surface(screen.get_size()).convert()
    background.fill((0,0,0))
    
    screen.blit(background,background.get_rect())
    
    pygame.display.set_icon(icon)
    pygame.display.set_caption('PyInvaders')
    pygame.mouse.set_visible(0)
    
    bullets = []
    for i in range(MAX_BULLETS):
        bullets.append(copy.deepcopy(bullet))
        
    invaders = []
    for i in range(MAX_INVADERS):
        invaders.append(invader.Invader(invader1))
        invaders.append(invader.Invader(invader2))
    
    p = player.Player(width, height, PLAYER_OFFSET)
    
    
    objects = []
    #objects.append(p)
    objects.extend(invaders)
    all_sprites = pygame.sprite.RenderPlain(objects)

    #init the font module and load the font
    pygame.font.init()
    font = pygame.font.Font('../gfx/04b_25__.ttf', 12)
    
    while game_loop:       
        
        #clearing screen
        for s in objects:
            screen.blit(background, s.rect)
        
        #watching for key events   
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_loop = not game_loop            
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    game_loop = not game_loop
                    
                #start activating invaders  
                if event.key == pygame.K_p:
                    for i in invaders:
                        i.active = not i.active
                        i.rect.top = random.randint(0, (height - 64) / 32) * 32
                        i.rect.left = -32

                #switching betweent keyboard and mouse
                if event.key == pygame.K_k:
                    input_type = not input_type
                    
                    
        # hints and shortcuts to be printed
        screen.blit(font.render("Press k to switch input", 0, ((255, 206, 0))), (460, 5))

        if input_type is True:
            screen.blit(font.render("current input: " + "keyboard", 0, ((255, 0, 0))), (465, 20))
        
        else:
            screen.blit(font.render("current input: " + "mouse", 0, ((255, 0, 0))), (465, 20))
            

        p.update(input_type)
        screen.blit(p.image,p.rect)

        all_sprites.update()
        all_sprites.draw(screen)
                
        clock.tick(FPS)
        pygame.display.flip()
        
    pygame.quit()
    
    

if __name__ == '__main__':
    main()
