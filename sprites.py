import pygame as pg
import random


class Captain(pg.sprite.Sprite):
    def __init__(self):
        pg.sprite.Sprite.__init__(self)

        self.image = pg.image.load("images/captain.png")
        self.image = pg.transform.scale(self.image,(400,400))

        self.rect = self.image.get_rect()
        self.rect.topleft = (-30,600)

        self.mode = "up"

    def update(self):
        if self.mode == "up":
            self.rect.y -= 2
            if self.rect.y <= 300:
                self.mode = "stay"

class Alien(pg.sprite.Sprite):
    def __init__(self):
        pg.sprite.Sprite.__init__(self)

        self.image = pg.image.load("images/alien_cat.png")
        self.image = pg.transform.scale(self.image,(400,400))

        self.rect = self.image.get_rect()
        self.rect.topleft = (-30,600)

        self.mode = "up"

    def update(self):
        if self.mode == "up":
            self.rect.y -= 2
            if self.rect.y <= 300:
                self.mode = "stay"

class Meteorite(pg.sprite.Sprite):
    def __init__(self,end_animation=False):
        pg.sprite.Sprite.__init__(self)
        self.end_animation = end_animation

        
        self.image = pg.image.load("images/meteorite.png")
        size = random.randint(70,150)

        self.image = pg.transform.scale(self.image,(size,size))
        
        self.rect = self.image.get_rect()
        self.rect.topleft = (800,random.randint(0,600-size))

        self.speedx = random.randint(1,2)
        self.speedy = random.randint(-2,2)

    def update(self):
        if not self.end_animation:
            self.rect.x -= self.speedx  
            self.rect.y += self.speedy
        else:
            self.rect.x -= 2
            self.rect.y += random.randint(-1,1)
class Cat_Starship(pg.sprite.Sprite):
    def __init__(self,mode="meteorites"):
        pg.sprite.Sprite.__init__(self)
        self.mode = mode
        self.image = pg.image.load("images/cat_starship_horizontal.png")
        self.image = pg.transform.scale(self.image,(150,150))
        
        self.rect = self.image.get_rect()
        self.rect.midleft = (0,300)

    def update(self,speed,allow_vertical_motion=True,allow_horizontal_motion=False):
        keys = pg.key.get_pressed() 
        if allow_vertical_motion:
            if keys[pg.K_w] or keys[pg.K_UP] and self.rect.top >= 0:
                self.rect.y -= speed
            elif keys[pg.K_s] or keys[pg.K_DOWN] and self.rect.bottom <= 600:
                self.rect.y += speed
        if allow_horizontal_motion:
            if keys[pg.K_a] or keys[pg.K_LEFT] and self.rect.left >= 0:
                self.rect.x -= speed
            elif keys[pg.K_d] or keys[pg.K_RIGHT] and self.rect.right <= 800:
                self.rect.x += speed
        
    def switch_textures(self,mode_to_switch):
        self.image = pg.image.load(f"images/{mode_to_switch}.png")
        self.image = pg.transform.scale(self.image,(150,150))

class Mouse_Starship(pg.sprite.Sprite):
    def __init__(self):
        pg.sprite.Sprite.__init__(self)


        
        self.image = pg.image.load("images/mouse_starship.png")
        size = random.randint(70,120)
        self.image = pg.transform.flip(self.image,False,True)

        self.image = pg.transform.scale(self.image,(size,size))
        
        self.rect = self.image.get_rect()
        self.rect.topleft = (random.randint(0,800-size),0)

        self.speedx = random.randint(1,2)
        self.speedy = random.randint(1,2)

    def update(self):
        # self.rect.x -= self.speedx  
        self.rect.y += self.speedy

class Lasers(pg.sprite.Sprite):
    def __init__(self,pos):
        pg.sprite.Sprite.__init__(self)

        
        
        self.image = pg.image.load("images/laser.png")

        self.image = pg.transform.scale(self.image,(50,50))
        
        self.rect = self.image.get_rect(midbottom=pos)


    def update(self):
        self.rect.y -= 9