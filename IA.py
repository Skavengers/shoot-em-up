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
        super().__init__(random.randint(0,WIDTH),-50,1,"C:/Users/franc/PycharmProjects/shoot/Assets/enemie.png",screen)
        self.x = random.randint(1,WIDTH)
        self.y = -100
    def draw(self):
        if self.x<=0 and self.y<=0:
            self.sprite = pg.transform.scale(self.sprite, ( self.x, self.y))
            self.rect = self.sprite.get_rect(topleft=[self.x, self.y])
            self.screen.blit(self.sprite, (self.x, self.y))

    def collide(self, obj):
        self.rect = self.sprite.get_rect(topleft=[self.x, self.y])
        if self.rect.colliderect(obj):
            self.y = -100
            self.x = -100
        else:
            self.draw()

class Eyes(IAshooter):
    def __init__(self,screen,x,y):
        super().__init__(x,y,1,"C:/Users/franc/PycharmProjects/shoot/Assets/yeux.jpg",screen)
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




