#All functions for the main game

import pygame as pg
import random as rm
import sprites as sp
import map as mp
import sys

class Game:
    def __init__(self, black) -> None:
        #Game essencials

        self.gameover = False

        #All lists

        self.sprite_list = pg.sprite.Group()
        self.laser_list = pg.sprite.Group()
        self.mob_list = pg.sprite.Group()

        #Sprite list

        self.player = sp.Player(black) 
        self.obj = sp.Obj(black)
        self.laser_blast = sp.Laser_blast(black)

        #Sprite adding

        self.sprite_list.add(self.obj)

        #Mob special adding

        x = rm.randint(1400, 1500)
        for mob in range(rm.randint(50, 100)):
            x += rm.randint(1000, 2000)
            mob = sp.Mob(black)
            mob.rect.x = x
            mob.rect.y = 400
            self.mob_list.add(mob)
            self.sprite_list.add(mob)

        self.sprite_list.add(self.player)

        #Background image

        self.bg = pg.image.load("game_bg.jpg").convert()

    def run_logic(self, size):
        #Update sprite

        self.sprite_list.update(size)

        #Mob movement limations

        for mob in self.mob_list:
            if mob.rect.x <= -100:
                mob.rect.x = rm.randint(1200, 1500)

        #Colission mechanism


        for lasser in self.laser_list:
            self.dead_mobs = []
            for mob in self.mob_list:
                if lasser.rect.x == mob.rect.x:
                    self.laser_list.remove(lasser)
                    self.sprite_list.remove(lasser)
                    self.dead_mobs.append(mob)
            for mob in self.dead_mobs:
                self.player.score += 1
                self.mob_list.remove(mob)
                self.sprite_list.remove(mob)
                print(self.player.score)
            if lasser.rect.x >= 850:
                self.laser_list.remove(lasser)

        #Player death mecanism

        for mob in self.mob_list:
            if mob.rect.x == self.player.rect.x and mob.rect.y == self.player.rect.y - 150:
                self.player.lifes -= 1

        if self.player.lifes == 0 or len(self.mob_list) == 0:
            self.gameover = True

    def display_refresh(self, screen, size, blue, white, black, color):
        screen.blit(self.bg, [0,0])
        if not self.gameover:
            pg.mouse.set_visible(0)
            self.sprite_list.draw(screen)

            #Show in screen lives and amount of mobs
            life_mobs = mp.Lifes_and_mobs(self.player.lifes, white, screen, len(self.mob_list))
            life_mobs.update(size)
        else:
            pg.mouse.set_visible(1)
            screen.fill(black)
            font = pg.font.SysFont("serif", 50)
            text = font.render("Game over, click to continue", True, color)
            center_x = (size[0] // 2) - (text.get_width() // 2)
            center_y = (size[1] // 2) - (text.get_height() // 2)
            screen.blit(text, [center_x, center_y])
        pg.display.flip()
