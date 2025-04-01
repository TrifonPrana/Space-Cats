import pygame as pg
import time
import random

from sprites import *


def dialogue_mode(sprite,text):
    screen.blit(bg,(0,0))
    screen.blit(sprite.image,sprite.rect)
    sprite.update()

    text1 = font.render(text[text_number],True,"white")
    screen.blit(text1,(280,450))
    if text_number < len(text) - 1:
        text2 = font.render(text[text_number+1],True,"white")
        screen.blit(text2,(280,470))

pg.init()

size = (800,600)
screen = pg.display.set_mode(size)
pg.display.set_caption("Космические коты")


#Объекты спрайтов
captain = Captain()
cat_starship = Cat_Starship()
alien_cat = Alien()
#Группы спрайтов
meteorites = pg.sprite.Group()#Meteorite()
mouse_starships = pg.sprite.Group()
lasers = pg.sprite.Group()

FPS = 120
clock = pg.time.Clock()

bg = pg.image.load("images/space.png")






is_running = True

mode = "start_scene"

start_text = ["Мы засекли сигнал с планеты Мур.",
              "",
              "Наши друзья, инопланетные коты,",
              "нуждаются в помощи.",
              "Космические мыши хотят съесть их луну,",
              "потому что она похожа на сыр.",
              "Как долго наш народ страдал от них, ",
              "теперь и муряне в беде...",
              "Мы должны помочь им.",
              "Вылетаем прямо сейчас.",
              "Спасибо, что починил звездолёт, штурман. ",
              "Наконец-то функция автопилота работает.",
              "Поехали!"]
alien_text = ["СПАСИТЕ! МЫ ЕЛЕ ДЕРЖИМСЯ!",
              "",
              "Мыши уже начали грызть луну...",
              "Скоро куски луны будут падать на нас.",
              "Спасите муриан!", ]
final_text = ["Огромное вам спасибо,",
              "друзья с планеты Мяу!",
              "Как вас называть? Мяуанцы? Мяуриане?",
              "В любом случае, ",
              "теперь наша планета спасена!",
              "Мы хотим отблагодарить вас.",
              "Капитан Василий и его штурман получают",
              "орден SKYSMART.",
              "А также несколько бутылок нашей",
              "лучшей валерьянки.",
              "",
              ""]
game_over_text = ["О нет!",
                  "Вы не уследили за прочностью",
                  "своего космического корабля!",
                  "Он разбился а экипаж погиб!",
                  "Попробуйте еще раз!",
                  "",
                  "Нажмите любую клавишу чтобы продолжить"
                  ]

text_number = 0
font = pg.font.Font("fonts/FRACTAL.otf",25)

heart_count = 3
heart = pg.image.load("images/heart.png")
heart = pg.transform.scale(heart,(50,50))

pg.mixer.music.load("sounds/Tense Intro.wav")
pg.mixer.music.set_volume(0.1)
pg.mixer.music.play()

win_sound = pg.mixer.Sound("sounds/Victory Screen Appear 01.wav")

while is_running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            is_running=False
        if event.type == pg.KEYDOWN:
            if mode == "death_scene":
                text_number+=2
                if text_number > len(game_over_text):
                        screen.blit(bg,(0, 0))
                        mode = "meteorites"
                        heart_count = 3
                        text_number = 0
                        start_time = time.time()
            if mode == "start_scene":
                    text_number+=2
                    if text_number > len(start_text):                     
                        mode = "meteorites"
                        text_number = 0
                        start_time = time.time()
            if mode == "alien_scene":
                    text_number+=2
                    if text_number > len(alien_text):
                        mode = "star_vors"
                        text_number = 0
                        start_time = time.time()
                        cat_starship.mode = "star_vors"
                        cat_starship.rect.y = 600-150
                        cat_starship.rect.x = 350
                        cat_starship.switch_textures("cat_starship")
            if mode == "star_vors":
                    if event.key == pg.K_SPACE or event.key == pg.K_UP:
                        lasers.add(Lasers(cat_starship.rect.midtop))
            if mode == "end_scene":
                    text_number+=2
                    print(text_number)
                    print(len(final_text))
                    if text_number >= len(final_text): 
                        text_number = 0
                        mode = "end_animation"
    if mode == "death_scene":
        dialogue_mode(alien_cat,game_over_text)
    if mode == "start_scene":
        dialogue_mode(captain,start_text)
    if mode == "meteorites":
        
        if time.time() - start_time > 30:
            screen.blit(bg,(0,0))
            screen.blit(cat_starship.image,cat_starship.rect)
            speed =0
            while not cat_starship.rect.right <= 600:
                screen.blit(cat_starship.image,cat_starship.rect)
                cat_starship.rect.x += speed
                speed+=20
                time.sleep(0)
            mode = "alien_scene"

        screen.blit(bg,(0,0))

        #добавляем метеорит в группу
        a = random.randint(0,100)
        if a < 4:
            meteorites.add(Meteorite())

        hits = pg.sprite.spritecollide(cat_starship,meteorites,True)
        for hit in hits:
            if heart_count > 0:
                heart_count -= 1
                #2486
                #1QazwsxedC2
            else:
                mode = "death_scene"
            
        meteorites.update()
        count = 0
        for i in range(heart_count):
            screen.blit(heart,(count,0))
            count+=50
        #Отрисовка  
        meteorites.draw(screen)
        screen.blit(cat_starship.image,cat_starship.rect)
        cat_starship.update(2,True,False)
    if mode == "alien_scene":
        dialogue_mode(alien_cat,alien_text)
    if mode == "star_vors":

        if time.time() - start_time > 30:
            pg.mixer.music.fadeout(3)
            win_sound.play()
            mode = "end_scene"

        screen.blit(bg,(0,0))
        screen.blit(cat_starship.image,cat_starship.rect)
        cat_starship.update(4,False,True)

        #добавляем метеорит в группу
        a = random.randint(0,175)
        if a < 2:
            mouse_starships.add(Mouse_Starship())  
        mouse_starships.update()
        mouse_starships.draw(screen)

                
        keys = pg.key.get_pressed()
        if keys[pg.K_SPACE] or keys[pg.K_UP]:
            lasers.add(Lasers(cat_starship.rect.midtop))
        hits = pg.sprite.groupcollide(lasers,mouse_starships,True,True)

        hits = pg.sprite.spritecollide(cat_starship,mouse_starships,True)
        for hit in hits:
            if heart_count > 0:
                heart_count -= 1
            else:
                mode = "death_scene"

        count = 0
        for i in range(heart_count):
            screen.blit(heart,(count,0))
            count+=50
        
        lasers.update()
        lasers.draw(screen)
    if mode == "end_scene":
        dialogue_mode(alien_cat,final_text)
    # if mode == "end_animation":
    #     screen.blit(bg,(0,0))
    #     cat_starship.rect.x = 300
    #     cat_starship.rect.y = 250
    #     cat_starship.switch_textures("cat_starship_horizontal")
    #     screen.blit(cat_starship.image,cat_starship.rect)
        
    #     if random.randint(0,4000) <=2:
    #         meteorites.add(Meteorite(end_animation=True))
    #     for meteorite in meteorites:
    #         meteorite.update()
    #     meteorites.draw(screen)
    pg.display.flip()

    clock.tick(FPS)