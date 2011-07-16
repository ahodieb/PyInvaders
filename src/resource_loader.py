import pygame,os

def load_image(filename, colorkey=None):
    filename = os.path.join('../gfx', filename)
    try:
        image = pygame.image.load(filename)
    except pygame.error, message:
        print 'Cannot load the image: ', filename
        raise SystemExit, message

    image = image.convert()

    if colorkey is not None:
        if colorkey is -1:
            colorkey = image.get_at((0,0))
        image.set_colorkey(colorkey, pygame.RLEACCEL)
        
    return image

def load_sprite_images(filename,w):
    master_image = load_image(filename, -1)
    master_width,master_height = master_image.get_size()
    
    images = []
    for i in xrange(master_width / w):
        images.append(master_image.subsurface((i*w,0,w,master_height)))
    
    return images

def load_sound(filename):
    class No_Sound:
        def play(self) : pass

    if not pygame.mixer or not pygame.mixer.get_init():
        print 'sound not enabled'
        return No_Sound()

    fullname = os.path.join('../sounds', filename)
    print fullname
    if os.path.exists(fullname):
        sound = pygame.mixer.Sound(fullname)
    else:
        print 'File does not exist!', filename
        return No_Sound()

    return sound