#All sprites for game

import pygame as pg
import random as rm
import sys

class Player(pg.sprite.Sprite):
    def __init__(self, black) -> None:
        super().__init__()
        self.image = pg.image.load("s_ship.png").convert()
        self.image.set_colorkey(black)
        self.rect = self.image.get_rect()
        self.lifes = 3
        self.score = 0

    def jump(self, vel_y):
        if self.rect.y <= 350:
            vel_y *= -1
        elif self.rect.y >= 550:
            vel_y = 0
            self.rect.y = 550

    def stop_move(self, x, vel):
        if x >= 1050:
            return 0 
        elif x < 0:
            return 0 
        else:
            return int(vel)

class Obj(pg.sprite.Sprite):
    def __init__(self, black) -> None:
        super().__init__()
        self.image = pg.image.load("obj_1.png").convert()
        self.image.set_colorkey(black)
        self.rect = self.image.get_rect()

    def update(self, size):
        self.rect.x = (size[0] // 2)- (323 // 2)
        self.rect.y = 450

class Laser_blast(pg.sprite.Sprite):
    def __init__(self, black) -> None:
        super().__init__()
        self.image = pg.image.load("laser_blast.png").convert()
        self.image.set_colorkey(black)
        self.rect = self.image.get_rect()

    def update(self, size):
        self.rect.x += 5

class Mob(pg.sprite.Sprite):
    def __init__(self, black) -> None:
        super().__init__()
        self.image = pg.image.load("mob.png").convert()
        self.image.set_colorkey(black)
        self.rect = self.image.get_rect()

    def update(self, size):
        self.rect.x -= 2

