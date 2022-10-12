import pygame as pg
from settings import *
import random

class IAshooter:
    def __init__(self,x,y,health,sprite,screen):
        self.x = x
        self.y = y
        self.health = health
        self.sprite = pg.image.load(sprite).convert_alpha()
        self.rect = self.sprite.get_rect(topleft=[self.x, self.y])
        self.screen = screen
    def draw(self):
        self.rect = self.sprite.get_rect(topleft=[self.x, self.y])
        self.screen.blit(self.sprite,(self.x,self.y))


class Xpbullet(IAshooter):
    def __init__(self,screen,x,y):
        super().__init__(x,y,1,"C:/Users/franc/PycharmProjects/shoot/Assets/xpbullet.png",screen)
    def draw(self):
        self.sprite = pg.transform.scale(self.sprite, (35, 35))
        super(Xpbullet, self).draw()
        self.y += 1
        """
        if self.y > 720:
            self.x = random.randint(0, HEIGTH)
            self.y = 100"""
    def collide(self,obj):
        self.rect = self.sprite.get_rect(topleft=[self.x, self.y])
        if self.rect.colliderect(obj):
            self.y = -100
            self.x = -100
            return "object"
        else:
            self.draw()
            return "nothing"


class Chest(IAshooter):
    def __init__(self,screen):
        super().__init__(random.randint(0,WIDTH), random.randint(0,HEIGTH),1,"C:/Users/franc/PycharmProjects/shoot/Assets/chest.png",screen)
        self.sprite = pg.transform.scale(self.sprite, (30, 30))
        self.rect = self.sprite.get_rect(topleft=[self.x, self.y])
    def draw(self):
        self.screen.blit(self.sprite, (self.x, self.y))
    def collide(self, obj):
        self.rect = self.sprite.get_rect(topleft=[self.x, self.y])
        if self.rect.colliderect(obj):
            self.y = -100
            self.x = -100
            return "chest"
        else:
            self.draw()
            return "nothing"


class Eyes(IAshooter):
    def __init__(self,screen,x,y):
        super().__init__(x,y,1,"C:/Users/franc/PycharmProjects/shoot/Assets/mob/yeux.jpg",screen)
        self.sprite.set_colorkey(WHITE)
    def draw(self):
        self.x += random.randint(-2,2)
        self.y += 1
        super(Eyes, self).draw()
    def collide(self, obj):
        self.rect = self.sprite.get_rect(topleft=[self.x, self.y])
        if self.rect.colliderect(obj):
            return "get_damage", 25
        else:
            return "nothing"


class Vanguard(IAshooter):
    def __init__(self,screen,x,y):
        super(Vanguard, self).__init__(x,y,10,r"C:\Users\franc\PycharmProjects\shoot\Assets\mob\enemie.png",screen)
        self.sprite.set_colorkey(WHITE)
        self.charge = 3
        self.action = pg.time.get_ticks()
        self.y_bullet = self.y
        self.sprite_bullet = pg.image.load(r'C:\Users\franc\PycharmProjects\shoot\Assets\animation\vanguardbullet\b1.png').convert_alpha()
        self.sprite_bullet.set_colorkey(WHITE)
    def draw(self):
        super(Vanguard, self).draw()
        if self.y_bullet > -HEIGTH:
            self.y_bullet = self.y
            self.bullet()
        if self.charge == 0:
            self.y -= 1
        elif self.y < 100:
            self.y += 1
        elif self.charge > 0 and pg.time.get_ticks() - 500 > self.action:
            self.action = pg.time.get_ticks()
            self.charge -= 1
    def bullet(self):
        shoot_speed = 1
        self.y_bullet -= shoot_speed
        self.screen.blit(self.sprite_bullet, (self.x, self.y_bullet))

    def collide(self,obj):
        self.rect = self.sprite.get_rect(topleft=[self.x, self.y])
        if self.rect.colliderect(obj):
            self.x = 0
            self.y = 2000
            return "get_damage", 100
        else:
            return "nothing"


class Vessel(IAshooter):
    def __init__(self,screen, x, y,x_end, y_end, health):
        super(Vessel, self).__init__(x, y, health, "C:/Users/franc/PycharmProjects/shoot/Assets/vessel.png", screen)
        self.x_end = x_end
        self.y_end = y_end
        self.k = (self.x - self.y_end, self.y - self.x_end)
    def draw(self):
        super(Vessel, self).draw()
        self.x -= self.k
    def collide(self,obj):
        self.rect = self.sprite.get_rect(topleft=[self.x, self.y])
        if self.rect.colliderect(obj):
            self.x = 0
            self.y = 2000
            return "get_damage", 50
        else:
            return "nothing"









