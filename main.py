import pygame as pg
from settings import *
BLACK = (0,)*3


class Ship:
    def __init__(self, link_sprite, health=10, lvl=0):
        self.time_laser = 0
        self.lvl = lvl
        self.health = health
        self.sprite = pg.image.load(link_sprite).convert_alpha()
        self.true_sprite = pg.image.load(r"C:\Users\franc\PycharmProjects\shoot\Assets\truesprite.png").convert_alpha()
        self.true_rect = self.true_sprite.get_rect(topleft=[108, 113])
        self.rect = self.sprite.get_rect(topleft=[100, 100])
        self.pos_shoot = []
    def draw(self,rectyeux):
        red = (255,0,0)
        font = pg.font.SysFont("earthorbiter.ttf", 70)
        show_health = font.render(str(self.health), True, red)
        screen.blit(show_health, (20, 20))
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
            screen.blit(die_animation, (self.rect.x + 2, self.rect.y - HEIGTH - self.sprite.get_height()))
            self.time_laser -= 1 / 30
        except:
            pass

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
        if keys[pg.K_b] and count % (FPS/4) == 0 :
            self.pos_shoot.append([self.rect.x,self.rect.y])
        if keys[pg.K_a]and count % (FPS/4) == 0:
            self.uselaser()






def run():
    font = pg.font.SysFont("earthorbiter.ttf", 70)
    pg.display.set_caption('to the moon')
    icon = pg.image.load(r"C:\Users\franc\PycharmProjects\shoot\Assets\pycon.png").convert()
    monster1 = pg.image.load(r'C:\Users\franc\PycharmProjects\shoot\Assets\yeux.jpg').convert()
    pg.display.set_icon(icon)
    rectyeux = monster1.get_rect(topleft = [200, 200])
    ship = Ship(r'C:\Users\franc\PycharmProjects\shoot\Assets\char1.png',10)
    count = 0
    while True:
        screen.fill('blue')
        count += 1
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
        ship.keys(count, rectyeux)
        ship.laser()
        ship.bullet()
        if ship.health == 0:
            ship.die()
        """img = font.render('You Die ', True, BLACK)
        while True:
            screen.blit(img, (20, 20))
            pg.display.flip()
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()"""



        screen.blit(monster1,rectyeux)
        ship.draw(rectyeux)
        pg.display.flip()
        """pg.display.update()"""
        clock.tick(FPS)

if __name__ == '__main__':
    screen = pg.display.set_mode((WIDTH, HEIGTH))
    pg.init()
    clock = pg.time.Clock()
    run()

