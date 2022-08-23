import pygame as pg
from settings import *
from levelup import *

class Ship:
    def __init__(self, link_sprite, health=10, lvl=0, power=3):
        self.time_laser = 0
        self.lvl = lvl
        self.health = health
        self.power = power
        self.sprite = pg.image.load(link_sprite).convert_alpha()
        self.true_sprite = pg.image.load(r"C:\Users\franc\PycharmProjects\shoot\Assets\truesprite.png").convert_alpha()
        self.true_rect = self.true_sprite.get_rect(topleft=[108, 113])
        self.true_sprite.set_colorkey(WHITE)
        self.sprite.set_colorkey(WHITE)
        self.rect = self.sprite.get_rect(topleft=[100, 100])
        self.pos_shoot = []
    def draw(self,rectyeux):
        red = (255,0,0)
        font = pg.font.SysFont("earthorbiter.ttf", 70)
        show_health = font.render(str(self.health), True, red)
        show_power = font.render("Power: "+str(self.power),True, BLACK)
        screen.blit(show_health, (20, 20))
        screen.blit(show_power,(900,20))
        if self.rect.colliderect(rectyeux):
            screen.blit(self.true_sprite, self.true_rect)
        else:
            screen.blit(self.sprite, self.rect)
    def die(self):
        """animation qui prend tout l’écran qui doit être plus petite pour ne pas impacter son coéquippier"""
        die_animation_list = [pg.image.load(r"C:\Users\franc\PycharmProjects\shoot\Assets\animation\die\animation.png").convert(),
                         pg.image.load(r"C:\Users\franc\PycharmProjects\shoot\Assets\animation\die\animation2.png").convert(),
                         pg.image.load(r"C:\Users\franc\PycharmProjects\shoot\Assets\animation\die\animation3.png").convert()]
        value = 0
        walk = True
        while walk:
            if value >= len(die_animation_list):
                """value = 0"""
                break
            pg.display.update()
            die_animation = die_animation_list[value]
            screen.blit(die_animation, (0, 0))
            clock.tick(1)
            value += 1
    def bullet(self):
        sprite_bullet = pg.image.load(r'C:\Users\franc\PycharmProjects\shoot\Assets\shoot.png').convert_alpha()
        sprite_bullet.set_colorkey(WHITE)
        compteur = 0
        for i in range(len(self.pos_shoot)):
            i -= compteur
            if len(self.pos_shoot) != 0:
                self.pos_shoot[i][1] -= int(SHOOT_SPEED)
                screen.blit(sprite_bullet, (self.pos_shoot[i][0] + sprite_bullet.get_width()/2-4, self.pos_shoot[i][1]))
                if self.pos_shoot[i][1] < 0:
                    del self.pos_shoot[i]
                    compteur += 1
    def uselaser(self):
        self.time_laser = 6
        self.power -=1
    def laser(self):
        laser_animation = [pg.image.load(r"C:\Users\franc\PycharmProjects\shoot\Assets\animation\laser\laser.png").convert_alpha(),
                           pg.image.load(r"C:\Users\franc\PycharmProjects\shoot\Assets\animation\laser\laser1.png").convert_alpha(),
                           pg.image.load(r"C:\Users\franc\PycharmProjects\shoot\Assets\animation\laser\laser2A.png").convert_alpha(),
                           pg.image.load(r"C:\Users\franc\PycharmProjects\shoot\Assets\animation\laser\laser2B.png").convert_alpha(),
                           pg.image.load(r"C:\Users\franc\PycharmProjects\shoot\Assets\animation\laser\laser3.png").convert_alpha(),
                           pg.image.load(r"C:\Users\franc\PycharmProjects\shoot\Assets\animation\laser\laser4.png").convert_alpha(),
                           pg.image.load(r"C:\Users\franc\PycharmProjects\shoot\Assets\animation\laser\laser5.png").convert_alpha(),
                           pg.image.load(r"C:\Users\franc\PycharmProjects\shoot\Assets\animation\laser\laser7.png").convert_alpha(),
                           pg.image.load(r"C:\Users\franc\PycharmProjects\shoot\Assets\animation\laser\laser8.png").convert_alpha()]
        int_time_run = int(self.time_laser)
        try:
            die_animation = laser_animation[int_time_run]
            die_animation.set_colorkey(WHITE)
            screen.blit(die_animation, (self.rect.x + 2, self.rect.y - HEIGTH - self.sprite.get_height()-20))
            self.time_laser -= 1 / 30
            return True
        except:
            return False

    def keys(self,count,rectyeux):
        keys = pg.key.get_pressed()
        if self.true_rect.colliderect(rectyeux):
            self.health -= 1
        if keys[pg.K_LEFT] and self.rect.x>0 :
            self.rect.left-= SPEED
            self.true_rect.left-= SPEED
        if keys[pg.K_RIGHT] and self.rect.x<WIDTH-SIZE_w :
            self.rect.right += SPEED
            self.true_rect.right += SPEED
        if keys[pg.K_UP] and self.rect.y>0 :
            self.rect.top -= SPEED
            self.true_rect.top -= SPEED
        if keys[pg.K_DOWN] and self.rect.y<HEIGTH-SIZE_h :
            self.rect.bottom += SPEED
            self.true_rect.bottom += SPEED
        if keys[pg.K_b] and count % (FPS/4) == 0 and not self.laser():
            self.pos_shoot.append([self.rect.x, self.rect.y])
        if keys[pg.K_a] and not self.laser() and self.power != 0:
            self.uselaser()

class Object:
    def __init__(self, name, str_carac, img):
        self.card_background = ""
        self.name = name
        self.str_carac = str_carac
        self.img = pg.image.load(img).convert()
        self.font = pg.font.SysFont("essential.ttf", 50)
    def draw(self):
        text_name = self.font.render(self.name, True, GREY)
        text_carac = self.font.render(self.str_carac, True, GREY)
        screen.blit(text_name,(500,50))
        screen.blit(self.img,(300,100))
        screen.blit(text_carac,(500,800))


def lvlup():
    list_object = [["stong steel","give +1 health ","C:/Users/franc/PycharmProjects/shoot/Assets/objects/strong steel.png"],[""]]
    ob = Object(list_object[0][0],list_object[0][1],list_object[0][2])
    ob.draw()





def run():
    global SPEED
    font = pg.font.SysFont("earthorbiter.ttf", 70)
    pg.display.set_caption('to the moon')
    icon = pg.image.load(r"C:\Users\franc\PycharmProjects\shoot\Assets\pycon.png").convert()
    background = pg.image.load(r"C:\Users\franc\PycharmProjects\shoot\Assets\background.jpg").convert()
    monster1 = pg.image.load(r'C:\Users\franc\PycharmProjects\shoot\Assets\yeux.jpg').convert()
    monster1.set_colorkey(WHITE)
    pg.display.set_icon(icon)
    rectyeux = monster1.get_rect(topleft=[200, 200])
    ship = Ship(r'C:\Users\franc\PycharmProjects\shoot\Assets\char1.png',10)
    count = 0
    while True:
        screen.blit(background, (0, 0))
        count += 1
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
        """lvlup()"""

        ship.keys(count, rectyeux)
        islaseractivate = ship.laser()
        if islaseractivate:
            SPEED = 1
        else:
            SPEED = 5
        ship.bullet()
        if ship.health == 0:
            ship.die()

        screen.blit(monster1,rectyeux)
        ship.draw(rectyeux)
        pg.display.flip()
        clock.tick(FPS)


if __name__ == '__main__':
    screen = pg.display.set_mode((WIDTH, HEIGTH))
    pg.init()
    clock = pg.time.Clock()
    run()

