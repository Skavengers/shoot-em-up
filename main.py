import random
import pygame as pg
from settings import *

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
        self.levelup = False
        self.font = pg.font.SysFont("earthorbiter.ttf", 70)
    def draw(self,rectyeux):
        red = (255,0,0)
        show_health = self.font.render(str(self.health), True, red)
        show_power = self.font.render("Power: "+str(self.power), True, BLACK)
        screen.blit(show_health, (20, 20))
        screen.blit(show_power,(900,20))
        if self.rect.colliderect(rectyeux):
            screen.blit(self.true_sprite, self.true_rect)
        else:
            screen.blit(self.sprite, self.rect)
        """if self.rect.colliderect(mobxp.rect):
            self.lvl += 1
            self.levelup = True"""
    def object(self):
        statement = self.font.render("choose your ability ", True, BLACK)
        list_object = [["C:/Users/franc/PycharmProjects/shoot/Assets/objects/strong steel.png", "carac", "hp", 1],
                       ["C:/Users/franc/PycharmProjects/shoot/Assets/objects/WingofHermes.png", "carac", "speed", 1],
                       ["C:/Users/franc/PycharmProjects/shoot/Assets/objects/double-barrel.png", "special", ],
                       ["C:/Users/franc/PycharmProjects/shoot/Assets/objects/speedybullet.png", "carace"]]
        random.shuffle(list_object)
        img_object1 = pg.image.load(list_object[0][0])
        img_object2 = pg.image.load(list_object[1][0])
        img_object3 = pg.image.load(list_object[2][0])
        choose = True
        x = 590
        while choose:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
            keys = pg.key.get_pressed()
            if keys[pg.K_LEFT]:
                if x >= 90:
                    x -= 400
                    print("ppp")
                else:
                    x = 890
                    print("no")
            if keys[pg.K_RIGHT]:
                if x != 890:
                    x += 400
                else:
                    x = 90
            if keys[pg.K_KP_ENTER]:
                choose = False
            screen.blit(img_object1, (100, 150))
            screen.blit(img_object2, (500, 150))
            screen.blit(img_object3, (900, 150))
            screen.blit(self.sprite, (x, 700))
            screen.blit(statement, (WIDTH//2, 50))
            pg.display.flip()
            clock.tick(FPS)



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
        if keys[pg.K_u]:
            self.object()


class IAshooter:
    def __init__(self,x,y,health,sprite):
        self.x = x
        self.y = y
        self.health = health
        self.sprite = pg.image.load(sprite).convert_alpha()
        self.rect = self.sprite.get_rect()
    def draw(self):
        screen.blit(self.sprite,(self.x,self.y))

class Xpbullet(IAshooter):
    def __init__(self):
        super().__init__(random.randint(0,HEIGTH),-10,1,"C:/Users/franc/PycharmProjects/shoot/Assets/xpbullet.png")



class Object:
    def __init__(self, img, type, precise_type, nb):
        self.img = pg.image.load(img).convert()
        self.type = type
        self.precise_type = precise_type
        self.nb = nb
        if self.type == "carac":
            if self.precise_type == "hp":
                e = ""
    def draw(self):
        screen.blit(self.img, (300, 100))


def chooseupgrape():
    keys = pg.key.get_pressed()
    if keys[pg.K_LEFT]:
        pass
    if keys[pg.K_RIGHT]:
        pass
    if keys[pg.K_KP_ENTER]:
        pass

def lvlup():
    #oof = pg.mixer.Sound('C:/Users/franc/PycharmProjects/shoot/Assets/Sound/noise/roblox-death-sound-oof-sound-effect-hd-homemadesoundeffects.mp3')
    list_object = [["C:/Users/franc/PycharmProjects/shoot/Assets/objects/strong steel.png","carac","hp",1],
                   ["C:/Users/franc/PycharmProjects/shoot/Assets/objects/WingofHermes.png","carac","speed",1],
                   ["C:/Users/franc/PycharmProjects/shoot/Assets/objects/double-barrel.png","special",]]
    random.shuffle(list_object)
    object1 = Object(list_object[0][0],list_object[0][1],list_object[0][2],100,100)
    object2 = Object(list_object[1][0],list_object[1][1],list_object[1][2],500,100)
    object3 = Object(list_object[2][0],list_object[2][1],list_object[2][2],900,100)
    object1.draw()
    object2.draw()
    object3.draw()
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
        Choice = chooseupgrape()








def run():
    global SPEED
    font = pg.font.SysFont("earthorbiter.ttf", 70)
    pg.display.set_caption('to the moon')
    icon = pg.image.load(r"C:\Users\franc\PycharmProjects\shoot\Assets\pycon.png").convert()
    background = pg.image.load(r"C:\Users\franc\PycharmProjects\shoot\Assets\background.jpg").convert()
    monster1 = pg.image.load(r'C:\Users\franc\PycharmProjects\shoot\Assets\yeux.jpg').convert()
    filemusic = pg.mixer.Sound("C:\\Users\\franc\\PycharmProjects\\shoot\\Assets\\Sound\\music\\BlueBoi.ogg")
    filemusic.play()
    monster1.set_colorkey(WHITE)
    pg.display.set_icon(icon)
    rectyeux = monster1.get_rect(topleft=[200, 200])
    mobxp = Xpbullet()
    ship = Ship(r'C:\Users\franc\PycharmProjects\shoot\Assets\char1.png',10)
    count = 0
    while True:
        screen.blit(background, (0, 0))
        count += 1
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
        if ship.levelup :
            lvlup()
            ship.levelup = False
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
        mobxp.draw()
        ship.draw(rectyeux)
        pg.display.flip()
        clock.tick(FPS)


if __name__ == '__main__':
    screen = pg.display.set_mode((WIDTH, HEIGTH))
    pg.init()
    pg.mixer.init()
    pg.mouse.set_visible(False)
    clock = pg.time.Clock()
    run()