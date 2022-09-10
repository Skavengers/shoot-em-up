import pygame as pg
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


class Chest(IAshooter):
    def __init__(self,screen,x):
        super().__init__(x,-10,1,"C:/Users/franc/PycharmProjects/shoot/Assets/xpbullet.png",screen)
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
            return True
        else:
            return False
class Xpbullet(IAshooter):
    def __init__(self,screen,x):
        super().__init__(x,-10,1,"C:/Users/franc/PycharmProjects/shoot/Assets/xpbullet.png",screen)
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
            return True
        else:
            return False

class Chest(IAshooter):
    def __init__(self,screen,xinit,yinit,x2,y2,v):
        super().__init__(xinit,yinit,1,"C:/Users/franc/PycharmProjects/shoot/Assets/chest.png",screen)
        self.x2 = x2
        self.y2 = y2
        self.directionx = self.x2 - self.x
        self.directiony = self.y2 - self.y
    def draw(self):
        self.sprite = pg.transform.scale(self.sprite, ( self.x- self.directionx, self.y- self.directiony))
        super(Xpbullet, self).draw()

class Eyes(IAshooter):
    def __init__(self,screen,x,y):
        super().__init__(x,y,1,"C:/Users/franc/PycharmProjects/shoot/Assets/yeux.jpg",screen)




