import pygame

class Shoot:
    def __init__(self):
        sprite_bullet = pg.image.load(r'C:\Users\franc\PycharmProjects\shoot\Assets\shoot.png').convert()
        x_shoot, y_shoot, compteur = -100, 100, 0
    def rocket:
        for i in range(len(self.pos_shoot)):
            i -= compteur
            if len(self.pos_shoot) != 0:
                self.pos_shoot[i][1] -= int(SHOOT_SPEED)
                screen.blit(sprite_bullet, (self.pos_shoot[i][0]+sprite_bullet.get_width()/2-4, self.pos_shoot[i][1]))
                if self.pos_shoot[i][1] < 0:
                    del self.pos_shoot[i]
                    compteur += 1
