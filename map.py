#map bg and other objects for map

import pygame as pg
import random as rm
import sys

class BackGround:
    def __init__(self) -> None:
        pass
        
class Lifes_and_mobs:
    def __init__(self, life, white, screen, mobs) -> None:
        self.screen = screen

        #Text creation for life of player
        self.font_life = pg.font.SysFont("serif", 50)
        self.text = self.font_life.render(f"Lifes: {str(life)}", True, white)
        self.text_x = 60
        self.text_y = 20

        #Text creation for mobs amount
        self.font_mob = pg.font.SysFont("serif", 30)
        self.text_mob = self.font_mob.render(f"mobs amount: {str(mobs)}", True, white)
        self.text_x_mob = 1000
        self.text_y_mob = 20

    def update(self, size):
        self.screen.blit(self.text, [self.text_x, self.text_y])
        self.screen.blit(self.text_mob, [self.text_x_mob, self.text_y_mob])
