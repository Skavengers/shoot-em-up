import pygame

class Object:
    def __init__(self, name, str_carac, img):
        self.name = name
        self.str_carac = str_carac
        self.img = img
    def upgrade(self):
        normal_luck = {
            "boost_reactor" : 20
        }
