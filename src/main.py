import pygame, os, random
import player
import invader
import resource_loader
import bullet

def main():
    FPS = 60
    MAX_BULLETS = 10
    MAX_INVADERS = 5

    #Game controlling variables
    main_loop = True
    title_screen = True
    game_loop = False
    menu_choice = 0
    input_type = True
    player_score = 0
    
    pygame.init()
    
    clock = pygame.time.Clock()
    size = width , height = 600 , 468
    screen = pygame.display.set_mode(size)
    
    icon = pygame.image.load('../gfx/icon.png')
    
    invader1_images = resource_loader.load_sprite_images('invader1.png',32)
    invader2_images = resource_loader.load_sprite_images('invader2.png',32)
    
    laser_sound = resource_loader.load_sound('lazer1.wav')
    explosion_sound = resource_loader.load_sound('explode1.wav')
    
    #bullet = pygame.image.load('../gfx/bullet1.png').convert()
    
    #this background should be replaced by the background image
    background = pygame.surface.Surface(screen.get_size()).convert()
    background.fill((212, 203, 67))
    
    screen.blit(background, background.get_rect())
    
    pygame.display.set_icon(icon)
    pygame.display.set_caption('PyInvaders')
    pygame.mouse.set_visible(0)
        
    invaders = []
    for i in range(MAX_INVADERS):
        invaders.append(invader.Invader(invader1_images,10))
        invaders.append(invader.Invader(invader2_images,20))
    
    p = player.Player()

    bullets = []    
    objects = []
    objects.extend(invaders)
    all_sprites = pygame.sprite.RenderPlain(objects)

    #init the font module and load the font
    if pygame.font:        
        pygame.font.init()
        font = pygame.font.Font('../gfx/04b_25__.ttf', 12)
        font_big = pygame.font.Font('../gfx/04b_25__.ttf', 18)
        font_title = pygame.font.Font('../gfx/04b_25__.ttf', 50)

    while main_loop:

        #################
        # TITLE SCREEN  #
        #################
        
        if title_screen:
            screen.blit(background, background.get_rect())

            screen.blit(font_title.render("PyInvaders", 0, ((197, 63, 60))), (205, 50))
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    main_loop = not main_loop
                
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        title_screen = not title_screen
                        main_loop = not main_loop

                    #menu_navigation
                    if event.key == pygame.K_DOWN:
                        menu_choice = 1
                    if event.key == pygame.K_UP:
                        menu_choice = 0

                    #start the game  
                    if event.key == pygame.K_RETURN and menu_choice == 0:
                        title_screen = False
                        game_loop = True
                        
                    #close the game  
                    if event.key == pygame.K_RETURN and menu_choice == 1:
                        title_screen = False
                        main_loop = False
                    
                        
            #handling menu choice switching
            if menu_choice == 0:
                screen.blit(font_big.render("Start", 0, ((197, 63, 60))), (290, 150))
                screen.blit(font_big.render("Exit", 0, ((82, 135, 175))), (295, 180))
            else:
                screen.blit(font_big.render("Start", 0, ((82, 135, 175))), (290, 150))
                screen.blit(font_big.render("Exit", 0, ((197, 63, 60))), (295, 180))

        clock.tick(FPS)
        pygame.display.flip()
        screen.blit(background, background.get_rect())
        
        #################
        #   GAME LOOP   #
        #################
        
        if game_loop:       
            
            #clearing screen
            screen.blit(background, p.rect)
            
            #clearing in active bullets
            bullets_to_remove =[]
            for b in bullets:
                if not b.active:
                    bullets_to_remove.append(b)
                    
            for b in bullets_to_remove:
                screen.blit(background,b.rect)
                bullets.remove(b)
                    
            
            
                
            for s in objects:
                screen.blit(background, s.rect)
            
            #watching for key events   
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_loop = not game_loop
                    main_loop = not main_loop
                
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        game_loop = not game_loop
                        title_screen = not title_screen
                        
                    #start activating invaders  
                    if event.key == pygame.K_p:
                        for i in invaders:
                            i.active = not i.active
                            #i.rect.top = random.randint(0, (height - 64) / 32) * 32
                            #i.rect.left = -32

                    #switching betweent keyboard and mouse
                    if event.key == pygame.K_k:
                        input_type = not input_type

                    if event.key == pygame.K_z:
                        bullets.append(bullet.Bullet(p.rect.midtop))
                        laser_sound.play()
            #hints and shortcuts to be printed
            screen.blit(font.render("Press k to switch input", 0, ((197, 63, 60))), (460, 5))

            if input_type is True:
                screen.blit(font.render("current input: " + "keyboard", 0, ((32, 135, 175))), (465, 20))
            
            else:
                screen.blit(font.render("current input: " + "mouse", 0, ((32, 135, 175))), (465, 20))

            screen.blit(font_big.render("Score: " + str(player_score), 0, ((197, 63, 60))), (5, 5))         


            p.update(input_type)            
            screen.blit(p.image, p.rect)

            for b in bullets:
                b.update()
                l = len(b.hit_test(objects))
                player_score += l
                if l > 0 : 
                    explosion_sound.play()
                screen.blit(b.image,b.rect)
                
            all_sprites.update()
            all_sprites.draw(screen)
                    
            clock.tick(FPS)
            pygame.display.flip()
        
    pygame.quit()
    

if __name__ == '__main__':
    main()
