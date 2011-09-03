import pygame
import player
import invader
import resource_loader
import bullet
from properties import *

FPS = 60
MAX_INVADERS = 5
SIZE =  900, 560

#Game Loop Control Variables
main_loop    = True
title_screen = True
game_loop    = False
menu_choice  = 0


input_type   = True
player_score = 0

#Font Constants
if pygame.font:        
    pygame.font.init()
    FONT_NORMAL = pygame.font.Font('../gfx/04b_25__.ttf', 12)
    FONT_BIG = pygame.font.Font('../gfx/04b_25__.ttf', 25)
    FONT_TITLE = pygame.font.Font('../gfx/04b_25__.ttf', 50)
else :
    print 'pyGame Fonts not supported'
    

#Color constants
RED    = (255, 0, 0)
BLUE   = (120, 190, 231)
YELLOW = (247,250,0)

clock  = pygame.time.Clock()
screen = pygame.display.set_mode(SIZE)

invader1_images = []
invader2_images = []
exp_images      = []
bullet1         = None

#Sounds
laser_sound     = None
explosion_sound = None

#Backgrounds
bg_Menu         = None
bg_Game         = None

#Objects Lists
invaders = []
p        = None
bullets = []

#objects Properties
bullet1_properties = None
invader1_properties = None
invader2_properties = None

def Init_Env():
    global icon
    global bg_Menu
    global bg_Game
    global screen
    
    pygame.init()
    icon = pygame.image.load('../gfx/icon.png') 
    
    pygame.display.set_icon(icon)
    pygame.display.set_caption('PyInvaders')
    pygame.mouse.set_visible(0)

    bg_Menu = resource_loader.load_image('bg_menu.jpg')
    bg_Game= resource_loader.load_image('bg_game.jpg')
    screen.blit(bg_Menu, bg_Menu.get_rect())

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
    
    global invader1_properties
    global invader2_properties
    
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

    #creating title invaders
    #title_invader1_image = resource_loader.load_image('wallpaper2.jpg')
    #title_invader1 = screen.blit(title_invader1_image, title_invader1_image.get_rect())
    
    p = player.Player()
    pygame.mixer.music.load('../sounds/game_music.mp3')
    pygame.mixer.music.set_volume(0.1)
    pygame.mixer.music.play(-1,0.0)
    
    clock.tick(FPS)
    screen.blit(bg_Game, bg_Game.get_rect())


def title_menu():
    global main_loop  
    global title_screen
    global game_loop
    global menu_choice 
    
    screen.blit(bg_Menu, bg_Menu.get_rect())
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
                #Init_Game()
                        
                    #close the game  
            if event.key == pygame.K_RETURN and menu_choice == 1:
                title_screen = False
                main_loop = False
                    
                        
            #handling menu choice switching

    if menu_choice == 0:
        start_color = YELLOW
        exit_color = BLUE
    else:
        start_color = BLUE
        exit_color = YELLOW
 
    start_txt = FONT_BIG.render('Start',1, start_color)
    start_txt_pos = start_txt.get_rect(centerx=669,centery=475)
    screen.blit(start_txt,start_txt_pos)
                
    start_txt = FONT_BIG.render('Exit',1, exit_color)
    start_txt_pos = start_txt.get_rect(centerx=669,centery=510)
    screen.blit(start_txt,start_txt_pos)
    if title_screen == False and game_loop == True : Init_Game()
    
    
def game():
    global main_loop  
    global title_screen
    global game_loop
    global input_type
    global player_score
    #clearing screen
    screen.blit(bg_Game, p.rect,p.rect)
            
    #clearing in active bullets
    bullets_to_remove = filter(lambda b : b.destroyed,bullets)
    #clear bullets for redraw
    for b in bullets:
        screen.blit(bg_Game,b.rect,b.rect)
                          
    for b in bullets_to_remove:                
        bullets.remove(b)
                
    #Clear invaders for redraw
    for i in invaders :
        screen.blit(bg_Game, i.rect,i.rect)
    invaders_to_remove = filter(lambda i : i.dead, invaders)                
    for i in invaders_to_remove:                
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
                      
                b =  bullet.Bullet(bullet1_properties,(x+15,y))
                b.vectorX = 3
                bullets.append(b) 
                        
                b =  bullet.Bullet(bullet1_properties,(x-15,y))
                b.vectorX = -3
                bullets.append(b) 
                
                b =  bullet.Bullet(bullet1_properties,(x,y))
                bullets.append(b) 
                        
            #laser_sound.play()
            if event.key == pygame.K_n:
                invaders.append(invader.Invader(invader1_properties))
                invaders.append(invader.Invader(invader2_properties))
                        
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    bullets.append(bullet.Bullet(bullet1_properties,p.rect.midtop))
                    #laser_sound.play()
                        
    #hints and shortcuts to be printed
    switch_input_txt = FONT_NORMAL.render('Press k to switch input',1,YELLOW)
    switch_input_txt_pos = switch_input_txt.get_rect(topright = (screen.get_width()-10,10))
    screen.blit(switch_input_txt,switch_input_txt_pos)
                        
    if input_type:
        current_input_txt = FONT_NORMAL.render('current input: keyboard',1,RED)
        current_input_txt_pos = current_input_txt.get_rect(centerx=switch_input_txt_pos.centerx,top = 25)
        screen.blit(current_input_txt,current_input_txt_pos)

                
    else:
    #screen.blit(font.render("current input: " + "mouse", 1, Red), (465, 20))
        current_input_txt = FONT_NORMAL.render('current input: mouse',1,RED)
        current_input_txt_pos = current_input_txt.get_rect(centerx=switch_input_txt_pos.centerx,top = 25)
        screen.blit(current_input_txt,current_input_txt_pos)
             
    #error in blitting the score to be fixed  
    score_input_txt = FONT_BIG.render('Score : '+ str(player_score),1,YELLOW)
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
    
def main():
    Init_Env()
    while main_loop:

        if title_screen:
            title_menu()            
            
        clock.tick(FPS)
        pygame.display.flip()
        
        if game_loop:    
            game()   
        
    pygame.quit()
    

if __name__ == '__main__':
    main()

