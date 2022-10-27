import random
import pygame as pg
from settings import *
from IA import Xpbullet, Chest, Eyes, Vanguard, Vessel
import os

class Ship:
    def __init__(self, link_sprite, lvl=0, power=3):
        self.missile_dommage = 10
        self.time_laser = 0
        self.lvl = lvl
        self.power = power
        self.sprite = pg.image.load(link_sprite).convert_alpha()
        print(os.path.join(os.getcwd(),"Assets","truesprite.png"))
        self.true_sprite = pg.image.load(os.path.abspath("Assets/truesprite.png")).convert_alpha()
        self.true_rect = self.true_sprite.get_rect(topleft=[258, 113])
        self.true_sprite.set_colorkey(WHITE)
        self.sprite.set_colorkey(WHITE)
        self.rect = self.sprite.get_rect(topleft=[250, 100])
        self.pos_shoot = []
        self.l_rect_missile = []
        self.font = pg.font.Font(os.path.abspath("police\\neuropol\\neuropol.otf"), 40)
        self.speed = 6
        self.oldspeed = self.speed
        self.shoot_speed = 10
        self.doublebarrel = False

        self.target_health = 500
        self.current_health = 200
        self.max_health = 1000
        self.health_bar_length = 200
        self.health_ratio = self.max_health / self.health_bar_length
        self.health_change_speed = 5

    def advanced_health(self):
        transition_width = 0
        transition_color = (255, 0, 0)

        if self.current_health < self.target_health:
            self.current_health += self.health_change_speed
            transition_width = int((self.target_health - self.current_health) / self.health_ratio)
            transition_color = (0, 255, 0)

        if self.current_health > self.target_health:
            self.current_health -= self.health_change_speed
            transition_width = int((self.target_health - self.current_health) / self.health_ratio)
            transition_color = (255, 255, 0)

        health_bar_width = int(self.current_health / self.health_ratio)
        health_bar = pg.Rect(10, 20, health_bar_width, 25)
        transition_bar = pg.Rect(health_bar.right, 20, transition_width, 25)

        pg.draw.rect(screen, (255, 0, 0), health_bar)
        pg.draw.rect(screen, transition_color, transition_bar)
        pg.draw.rect(screen, (255, 255, 255), (10, 20, self.health_bar_length, 25), 4)

    def get_damage(self, amount):
        if self.target_health > 0:
            self.target_health -= amount
        if self.target_health < 0:
            self.target_health = 0

    def get_health(self, amount):
        if self.target_health < self.max_health:
            self.target_health += amount
        if self.target_health > self.max_health:
            self.target_health = self.max_health

    def draw(self):
        show_power = self.font.render("POWER: " + str(self.power), True, BLACK)
        screen.blit(show_power, (900, 20))
        self.advanced_health()
        screen.blit(self.sprite, self.rect)
        """
        if self.rect.colliderect(rectyeux):
            screen.blit(self.true_sprite, self.true_rect)
        else:
            screen.blit(self.sprite, self.rect)
        """

    def get_chest(self):
        self.object(True)

    def object(self, is_chest=False):
        list_object = [[os.path.abspath("Assets/objects/strong steel.png"), "carac", "hp", 200],
                       [os.path.abspath("Assets/objects/WingofHermes.png"), "carac", "speed", 3],
                       [os.path.abspath("Assets/objects/double-barrel.png"), "special", "2shoot"],
                       [os.path.abspath("Assets/objects/speedybullet.png"), "carac", "shoot_speeb", 10],
                       [os.path.abspath("Assets/objects/bomb.png"), "special", ""],
                       [os.path.abspath("Assets/objects/nothing.png"), "special", ""],
                       [os.path.abspath("Assets/objects/pow.png"), "carac", "power", 1],
                       [os.path.abspath("Assets/objects/shield.png"), "carac", "hp", 500]]
        random.shuffle(list_object)
        img_object1 = pg.image.load(list_object[0][0])
        img_object2 = pg.image.load(list_object[1][0])
        img_object3 = pg.image.load(list_object[2][0])
        if not is_chest:
            choice = 0
            self.animO()
            self.lvl += 1
            statement = self.font.render("CHOOSE YOUR ABILITY !", True, RED)
            background = pg.image.load(os.path.abspath(r"Assets\animation\objectroom\nf.png")).convert()
            choose = True
            x = 590
            count = 0
            action = pg.time.get_ticks()
            while choose:
                count += 1
                for event in pg.event.get():
                    if event.type == pg.QUIT:
                        pg.quit()
                keys = pg.key.get_pressed()
                if keys[pg.K_LEFT] and pg.time.get_ticks() - 500 > action:
                    action = pg.time.get_ticks()
                    if x == 1000:
                        x = 590
                    elif x == 190:
                        x = 1000
                    elif x == 590:
                        x = 190
                elif keys[pg.K_RIGHT] and pg.time.get_ticks() - 300 > action:
                    action = pg.time.get_ticks()
                    if x == 1000:
                        x = 190
                    elif x == 590:
                        x = 1000
                    else:
                        x = 590
                elif keys[pg.K_e]:
                    choose = False
                    if x == 190:
                        choice = 0
                    if x == 590:
                        choice = 1
                    if x == 1000:
                        choice = 2
                    if list_object[choice][1] == "carac":
                        if list_object[choice][2] == "hp":
                            self.get_health(list_object[choice][3])
                        if list_object[choice][2] == "speed" and self.speed < 20:
                            self.speed += list_object[choice][3]
                        if list_object[choice][2] == "power":
                            self.power += list_object[choice][3]
                        if list_object[choice][2] == "shoot_speed":
                            self.shoot_speed += list_object[choice][3]
                    if list_object[choice][1] == "special":
                        if list_object[choice][2] == "2shoot":
                            self.doublebarrel = True
                screen.blit(background, (0, 0))
                screen.blit(img_object1, (100, 150))
                screen.blit(img_object2, (500, 150))
                screen.blit(img_object3, (900, 150))
                screen.blit(self.sprite, (x, 600))
                screen.blit(statement, (WIDTH // 2, 50))
                pg.display.flip()
                clock.tick(FPS)
        else:
            value = 0
            eee = True
            action = pg.time.get_ticks()
            while eee or pg.time.get_ticks() - 500 > action:
                keys = pg.key.get_pressed()
                for event in pg.event.get():
                    if event.type == pg.QUIT:
                        pg.quit()
                if keys[pg.K_b]:
                    eee = False

                title = self.font.render("YOU GAIN ", True, RED)
                screen.blit(title, (400, 200))
                screen.blit(img_object1, (500, 150))
                value += 1
                clock.tick(FPS)
                pg.display.flip()

    def collide(self, ufo):
        if ufo[0] == "get_health":
            self.get_health(ufo[1])
        if ufo[0] == "get_damage":
            self.get_damage(ufo[1])
        if ufo == "object":
            self.object()
        if ufo == "chest":
            self.get_chest()

    def die(self):
        """animation qui prend tout l’écran qui doit être plus petite pour ne pas impacter son coéquippier"""
        die_animation_list = [
            pg.image.load(os.path.abspath(r"Assets\animation\die\animation.png")).convert(),
            pg.image.load(os.path.abspath(r"Assets\animation\die\animation2.png")).convert(),
            pg.image.load(os.path.abspath(r"Assets\animation\die\animation3.png")).convert()]
        value = 0
        walk = True
        while walk:
            if value >= len(die_animation_list):
                break
            pg.display.update()
            die_animation = die_animation_list[value]
            screen.blit(die_animation, (0, 0))
            clock.tick(1)
            value += 1

    def animO(self):
        """animation qui prend tout l’écran utiliser pour choisir la carte que l’on veut"""
        animation_list = [
            pg.image.load(r"C:\Users\franc\PycharmProjects\shoot\Assets\animation\objectroom\n1.png").convert_alpha(),
            pg.image.load(r"C:\Users\franc\PycharmProjects\shoot\Assets\animation\objectroom\n2.png").convert_alpha(),
            pg.image.load(r"C:\Users\franc\PycharmProjects\shoot\Assets\animation\objectroom\n3.png").convert_alpha(),
            pg.image.load(
                r"C:\Users\franc\PycharmProjects\shoot\Assets\animation\objectroom\n4png.png").convert_alpha(),
            pg.image.load(
                r"C:\Users\franc\PycharmProjects\shoot\Assets\animation\objectroom\n5png.png").convert_alpha(),
            pg.image.load(
                r"C:\Users\franc\PycharmProjects\shoot\Assets\animation\objectroom\n6png.png").convert_alpha(),
            pg.image.load(
                r"C:\Users\franc\PycharmProjects\shoot\Assets\animation\objectroom\n7png.png").convert_alpha(),
            pg.image.load(
                r"C:\Users\franc\PycharmProjects\shoot\Assets\animation\objectroom\n8png.png").convert_alpha(),
            pg.image.load(
                r"C:\Users\franc\PycharmProjects\shoot\Assets\animation\objectroom\n9png.png").convert_alpha(),
            pg.image.load(
                r"C:\Users\franc\PycharmProjects\shoot\Assets\animation\objectroom\n10png.png").convert_alpha(),
            pg.image.load(
                r"C:\Users\franc\PycharmProjects\shoot\Assets\animation\objectroom\n11png.png").convert_alpha(),
            pg.image.load(
                r"C:\Users\franc\PycharmProjects\shoot\Assets\animation\objectroom\n12png.png").convert_alpha(),
            pg.image.load(
                r"C:\Users\franc\PycharmProjects\shoot\Assets\animation\objectroom\n13png.png").convert_alpha(),
            pg.image.load(
                r"C:\Users\franc\PycharmProjects\shoot\Assets\animation\objectroom\n14png.png").convert_alpha(),
            pg.image.load(
                r"C:\Users\franc\PycharmProjects\shoot\Assets\animation\objectroom\n15png.png").convert_alpha(),
            pg.image.load(
                r"C:\Users\franc\PycharmProjects\shoot\Assets\animation\objectroom\n16png.png").convert_alpha(),
            pg.image.load(
                r"C:\Users\franc\PycharmProjects\shoot\Assets\animation\objectroom\n17png.png").convert_alpha(),
            pg.image.load(
                r"C:\Users\franc\PycharmProjects\shoot\Assets\animation\objectroom\n18png.png").convert_alpha(),
            pg.image.load(
                r"C:\Users\franc\PycharmProjects\shoot\Assets\animation\objectroom\n19png.png").convert_alpha(),
            pg.image.load(
                r"C:\Users\franc\PycharmProjects\shoot\Assets\animation\objectroom\n19png.png").convert_alpha(),
        ]
        value = 0
        walk = True
        while walk:
            if value >= len(animation_list):
                break
            pg.display.update()
            animation = animation_list[value]
            animation.set_colorkey(WHITE)
            screen.blit(animation, (0, 0))
            clock.tick(20)
            value += 1

    def bullet(self):
        sprite_bullet = pg.image.load(os.path.abspath(r'Assets\shoot.png')).convert_alpha()
        sprite_bullet.set_colorkey(WHITE)
        compteur = 0
        self.l_rect_missile = []
        for i in range(len(self.pos_shoot)):
            i -= compteur
            self.l_rect_missile.append(sprite_bullet.get_rect(topleft=self.pos_shoot[i]))
            if len(self.pos_shoot) != 0:
                self.pos_shoot[i][1] -= int(self.shoot_speed)
                screen.blit(sprite_bullet, (
                    self.pos_shoot[i][0] + sprite_bullet.get_width() / 2 - 4 if self.doublebarrel == False else
                    self.pos_shoot[i][0] + sprite_bullet.get_width() / 2 - 9, self.pos_shoot[i][1]))
                if self.doublebarrel:
                    screen.blit(sprite_bullet,
                                (self.pos_shoot[i][0] + sprite_bullet.get_width() / 2 + 2, self.pos_shoot[i][1]))
                if self.pos_shoot[i][1] < 0:
                    del self.pos_shoot[i]
                    compteur += 1

    def uselaser(self):
        self.time_laser = 6
        self.power -= 1

    def laser(self):
        if self.speed != 1:
            self.oldspeed = self.speed
        if self.time_laser == 6:
            self.speed = 1
        laser_animation = [
            pg.image.load(os.path.abspath(r"Assets\animation\laser\laser.png")).convert_alpha(),
            pg.image.load(os.path.abspath(r"Assets\animation\laser\laser1.png")).convert_alpha(),
            pg.image.load(os.path.abspath(r"Assets\animation\laser\laser2A.png")).convert_alpha(),
            pg.image.load(os.path.abspath(r"Assets\animation\laser\laser2B.png")).convert_alpha(),
            pg.image.load(os.path.abspath(r"Assets\animation\laser\laser3.png")).convert_alpha(),
            pg.image.load(os.path.abspath(r"Assets\animation\laser\laser4.png")).convert_alpha(),
            pg.image.load(os.path.abspath(r"Assets\animation\laser\laser5.png")).convert_alpha(),
            pg.image.load(os.path.abspath(r"Assets\animation\laser\laser7.png")).convert_alpha(),
            pg.image.load(os.path.abspath(r"Assets\animation\laser\laser8.png")).convert_alpha()]
        int_time_run = int(self.time_laser)

        try:
            die_animation = laser_animation[int_time_run]
            die_animation.set_colorkey(WHITE)
            screen.blit(die_animation, (self.rect.x + 2, self.rect.y - HEIGTH - self.sprite.get_height() - 20))
            self.time_laser -= 1 / 30
            return True
        except:
            self.speed = self.oldspeed

    def keys(self, count):
        keys = pg.key.get_pressed()
        if keys[pg.K_LEFT] and self.rect.x > 0:
            self.rect.left -= self.speed
            self.true_rect.left -= self.speed
        if keys[pg.K_RIGHT] and self.rect.x < WIDTH - SIZE_w:
            self.rect.right += self.speed
            self.true_rect.right += self.speed
        if keys[pg.K_UP] and self.rect.y > 0:
            self.rect.top -= self.speed
            self.true_rect.top -= self.speed
        if keys[pg.K_DOWN] and self.rect.y < HEIGTH - SIZE_h:
            self.rect.bottom += self.speed
            self.true_rect.bottom += self.speed
        if keys[pg.K_b] and count % (FPS / 4) == 0 and not self.laser():
            self.pos_shoot.append([self.rect.x, self.rect.y])
        if keys[pg.K_a] and not self.laser() and self.power != 0:
            self.uselaser()


def run():
    pg.display.set_caption('to the moon')
    icon = pg.image.load(os.path.abspath(r"Assets\pycon.png")).convert()
    background = pg.image.load(os.path.abspath(r"Assets\background.jpg")).convert()
    filemusic = pg.mixer.Sound(os.path.abspath("Assets\\Sound\\music\\BlueBoi.ogg"))
    filemusic.play()
    filemusic.stop()
    """filemusic.stop()"""
    pg.display.set_icon(icon)
    ship = Ship(os.path.abspath(r'Assets\char1.png'), 3)
    list_enemies = [Eyes(screen, 600, 100), Vanguard(screen, 800, -10), Xpbullet(screen, 200, -30),
                    Xpbullet(screen, 400, -500),
                    Eyes(screen, 100, 700), Eyes(screen, 100, -1000), Vanguard(screen, 20, 0), Chest(screen)]
    count = 0
    while True:
        screen.blit(background, (0, 0))
        count += 1
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
        ship.keys(count)
        ship.bullet()
        ship.laser()
        i = 0
        for en in list_enemies:
            i += 1
            en.draw()
            ship.collide(en.collide(ship.rect, ship.l_rect_missile))
            if en.health < 0 or en.y < -HEIGTH:
                del list_enemies[i-1]
        if ship.current_health == 0:
            ship.die()
        ship.draw()
        pg.display.flip()
        clock.tick(FPS)


if __name__ == '__main__':
    screen = pg.display.set_mode((WIDTH, HEIGTH))
    pg.init()
    pg.mixer.init()
    pg.mouse.set_visible(False)
    clock = pg.time.Clock()
    run()
