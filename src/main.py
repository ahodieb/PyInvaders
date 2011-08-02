import pygame
import player
import invader
import resource_loader
import bullet
from properties import *



FPS = 60
MAX_INVADERS = 5
SIZE =  900, 560

main_loop    = True
title_screen = True
game_loop    = False
menu_choice  = 0
input_type   = True
player_score = 0

#Color constants
Red    = (255, 0, 0)
Blue   = (0, 0, 255)
Yellow = (225,255,0)

clock  = pygame.time.Clock()
screen = pygame.display.set_mode(SIZE)

invader1_images = []
invader2_images = []
exp_images      = []
bullet1         = None
laser_sound     = None
explosion_sound = None
background      = None

invaders = []
p        = None
bullets = []
bullet1_properties = None

def Init_Env():
    global icon
    global background
    global screen
    
    pygame.init()
    icon = pygame.image.load('../gfx/icon.png') 
    
    pygame.display.set_icon(icon)
    pygame.display.set_caption('PyInvaders')
    pygame.mouse.set_visible(0)
    
    #this background should be replaced by the background image
    #background = pygame.surface.Surface(screen.get_size()).convert()
    #background.fill((0, 0, 0))
    background = resource_loader.load_image('wallpaper2.jpg')
    screen.blit(background, background.get_rect())

def Init_Game():
    global invader1_images
    global invader2_images
    global exp_images
    global bullet1
    global laser_sound
    global explosion_sound
    global background
    
    global bullets 
    global invaders
    global bullet1_properties
    global p
    
    bullets = []
    invaders = []
    
    invader1_images = resource_loader.load_sprite_images('invader1.png',32)
    invader2_images = resource_loader.load_sprite_images('invader2.png',32)
    exp_images = resource_loader.load_sprite_images('exp.png',32)
    bullet1 = pygame.image.load('../gfx/bullet2.png')  
    
    laser_sound = resource_loader.load_sound('lazer1.wav')
    laser_sound.set_volume(0.1)
    explosion_sound = resource_loader.load_sound('explode1.wav')
    explosion_sound.set_volume(0.1)
    #loading function would be implemented to load those settings from xmlfiles
    invader1_properties = Invader_Properties(invader1_images,exp_images,explosion_sound,5,0,0,2,10,1)
    invader2_properties = Invader_Properties(invader2_images,exp_images,explosion_sound,5,0,0,2,20,2)
    #put room for images for the weopon to explode 
    bullet1_properties  = Wepon__Properties([bullet1],[],laser_sound,0,10,0,2,10)
    

    
    for i in xrange(MAX_INVADERS):
        invaders.append(invader.Invader(invader1_properties))
        invaders.append(invader.Invader(invader2_properties))
    
    p = player.Player()
    pygame.mixer.music.load('../sounds/game_music.mp3')
    pygame.mixer.music.set_volume(0.1)
    pygame.mixer.music.play(-1,0.0)
    
def main():
    global main_loop  
    global title_screen
    global game_loop
    global menu_choice 
    global input_type
    global player_score 
    
    global invader1_images
    global invader2_images
    global exp_images
    global bullet1
    global laser_sound
    global explosion_sound
    global background
    
    
    global invaders
    global p
    global bullets
    
    Init_Env()
    #Init_Game()
     
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
            title = font_title.render('PyInvaders',1,Red)
            title_pos = title.get_rect(centerx=screen.get_width()/2,centery=100)
            screen.blit(title,title_pos)
            #screen.blit(font_title.render("PyInvaders", 0, Red), (height/2 - 100, 50))
            
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
                        Init_Game()
                        
                    #close the game  
                    if event.key == pygame.K_RETURN and menu_choice == 1:
                        title_screen = False
                        main_loop = False
                    
                        
            #handling menu choice switching

            if menu_choice == 0:
                start_color = Red
                exit_color = Blue
            else:
                start_color = Blue
                exit_color = Red
 
            start_txt = font_big.render('Start',1,start_color)
            start_txt_pos = start_txt.get_rect(centerx=screen.get_width()/2,centery=screen.get_height()/2)
            screen.blit(start_txt,start_txt_pos)
                
            start_txt = font_big.render('Exit',1,exit_color)
            start_txt_pos = start_txt.get_rect(centerx=screen.get_width()/2,centery=screen.get_height()/2 +30 )
            screen.blit(start_txt,start_txt_pos)
            
        clock.tick(FPS)
        pygame.display.flip()
        screen.blit(background, background.get_rect())
        
        #################
        #   GAME LOOP   #
        #################
        
        if game_loop:       
            
            #clearing screen
            screen.blit(background, p.rect,p.rect)
            
            #clearing in active bullets
            bullets_to_remove = filter(lambda b : b.destroyed,bullets)            
            for b in bullets_to_remove:
                #screen.blit(background,b.rect,b.rect)
                bullets.remove(b)

            invaders_to_remove = filter(lambda i : i.dead, invaders)                
            for i in invaders_to_remove:
                screen.blit(background, i.rect,i.rect)
                player_score += i.properties.score
                invaders.remove(i)
            
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
                            
                        for b in bullets :
                            b.active = not b.active

                    #switching between keyboard and mouse
                    if event.key == pygame.K_k:
                        input_type = not input_type

                    #Fire bullets
                    if event.key == pygame.K_z:
                        x,y = p.rect.midtop
#                        bullets.append(bullet.Bullet(bullet1_properties,(x+15,y)))
#                        bullets.append(bullet.Bullet(bullet1_properties,(x-15,y)))
#                        bullets.append(bullet.Bullet(bullet1_properties,(x,y)))
#                       
                        b =  bullet.Bullet(bullet1_properties,(x+15,y))
                        b.vectorX = 3
                        bullets.append(b) 
                        
                        b =  bullet.Bullet(bullet1_properties,(x-15,y))
                        b.vectorX = -3
                        bullets.append(b) 
#                        
                        b =  bullet.Bullet(bullet1_properties,(x,y))
                        bullets.append(b) 
                        
                        #laser_sound.play()
                        
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        bullets.append(bullet.Bullet(bullet1_properties,p.rect.midtop))
                        #laser_sound.play()
                        
            #hints and shortcuts to be printed
            switch_input_txt = font.render('Press k to switch input',1,Yellow)
            switch_input_txt_pos = switch_input_txt.get_rect(topright = (screen.get_width()-10,10))
            screen.blit(switch_input_txt,switch_input_txt_pos)
                        
            if input_type:
                current_input_txt = font.render('current input: keyboard',1,Red)
                current_input_txt_pos = current_input_txt.get_rect(centerx=switch_input_txt_pos.centerx,top = 25)
                screen.blit(current_input_txt,current_input_txt_pos)

                
            else:
                #screen.blit(font.render("current input: " + "mouse", 1, Red), (465, 20))
                current_input_txt = font.render('current input: mouse',1,Red)
                current_input_txt_pos = current_input_txt.get_rect(centerx=switch_input_txt_pos.centerx,top = 25)
                screen.blit(current_input_txt,current_input_txt_pos)
               
            score_input_txt = font_big.render('Score : '+ str(player_score),1,Yellow)
            score_input_txt_pos = score_input_txt.get_rect(topleft = (10,10))
            screen.blit(score_input_txt,score_input_txt_pos)

            
            p.update(input_type)            
            screen.blit(p.image, p.rect)

            for i in invaders:               
                #l = len(i.hit_test(bullets))
                #player_score += l
                #if l > 0 : 
                    #explosion_sound.play()
                #    pass
                i.hit_test(bullets)
                i.update()
                screen.blit(i.image,i.rect)
                    
            for b in bullets:
                b.update()
                screen.blit(b.image,b.rect)


            clock.tick(FPS)
            pygame.display.flip()
        
    pygame.quit()
    

if __name__ == '__main__':
    main()

