import pygame as pg
import random
from settings import *


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
    def __init__(self,screen,x):
        super().__init__(x,-10,1,"C:/Users/franc/PycharmProjects/shoot/Assets/xpbullet.png",screen)
    def draw(self):
        self.sprite = pg.transform.scale(self.sprite, (35, 35))
        super(Xpbullet, self).draw()
        self.y += 1
        if self.y>720:
            self.x = random.randint(0, HEIGTH)
            self.y = 100
    def collide(self,obj):
        if self.rect.colliderect(obj):
            return True
        else:
            return False
"""
class Catterpillar(IAshooter):
    def __init__(self):
        pass
"""


