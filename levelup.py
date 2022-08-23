"""import pygame as pg
from settings import *
from main import *

class Object:
    def __init__(self, name, str_carac, img):
        self.card_background = ""
        self.name = name
        self.str_carac = str_carac
        self.img = pg.image.load(img).convert()
        self.font = pg.font.SysFont("essential.ttf", 50)
    def draw(self):
        text_name = self.font.render(self.name, True, GREY)
        text_carac = self.font.render(self.str_carac, True, BLACK)
        screen.blit(text_name,(500,50))
        screen.blit(self.img,(300,100))
        screen.blit(text_carac,(500,800))


def lvlup():
    list_object = [["stong steel","give +1 health ","C:/Users/franc/PycharmProjects/shoot/Assets/objects/strong steel.png"],[""]]
    ob = Object(list_object[0][0],list_object[0][1],list_object[0][2])
    ob.draw()"""
