import pygame as pg
from settings import *
BLACK = (0,)*3

def run():
    font = pg.font.SysFont("earthorbiterdeep3.ttf", 70)
    screen = pg.display.set_mode((WIDTH, HEIGTH))
    pg.display.set_caption('to the moon')
    icon = pg.image.load(r"C:\Users\franc\PycharmProjects\shoot\Assets\pycon.png").convert()
    sprite1 = pg.image.load(r'C:\Users\franc\PycharmProjects\shoot\Assets\char1.png')
    sprite2 = pg.image.load(r'C:\Users\franc\PycharmProjects\shoot\Assets\shoot.png').convert()
    monster1 = pg.image.load(r'C:\Users\franc\PycharmProjects\shoot\Assets\yeux.jpg').convert()
    pg.display.set_icon(icon)
    clock = pg.time.Clock()

    sprite1_rect = sprite1.get_rect(topleft = [100, 100])
    rectyeux = monster1.get_rect(topleft = [200, 200])
    x,y,x_shoot,y_shoot,count = 100,100,-100,-100,0
    pos_shoot = []
    while True:
        screen.fill('blue')
        count += 1
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
        keys = pg.key.get_pressed()
        if not sprite1_rect.colliderect(rectyeux):
            if keys[pg.K_LEFT] and sprite1_rect.x>0 :
                sprite1_rect.left -= SPEED
            if keys[pg.K_RIGHT] and sprite1_rect.x<WIDTH-SIZE_w :
                sprite1_rect.right += SPEED
            if keys[pg.K_UP] and sprite1_rect.y>0 :
                sprite1_rect.top -= SPEED
            if keys[pg.K_DOWN] and sprite1_rect.y<HEIGTH-SIZE_h :
                sprite1_rect.bottom += SPEED
            if keys[pg.K_b] and count % (FPS/4) == 0:
                pos_shoot.append([sprite1_rect.x+3,sprite1_rect.y])
        else:
            img = font.render('You Die ', True, BLACK)
            while True:
                screen.blit(img, (20, 20))
                pg.display.flip()
                for event in pg.event.get():
                    if event.type == pg.QUIT:
                        pg.quit()

        compteur = 0
        for i in range (len(pos_shoot)):
            i -= compteur
            if len(pos_shoot) != 0:
                pos_shoot[i][1] -= int(SHOOT_SPEED)
                screen.blit(sprite2,(pos_shoot[i][0], pos_shoot[i][1]))
                if pos_shoot[i][1] < 0:
                    del pos_shoot[i]
                    compteur += 1

        screen.blit(monster1,rectyeux)
        screen.blit(sprite1,sprite1_rect)
        pg.display.flip()
        """pg.display.update()"""
        clock.tick(FPS)

if __name__ == '__main__':
    pg.init()
    run()

