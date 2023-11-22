#Initializator for game app

#File importation
import pygame as pg
import random as rm
import game as gm
import sprites as sp
import map as mp
import sys 

#Window creation
size = (1300, 800)

#Colors 

black = (   0,   0,   0)
white = ( 255, 255, 255)
red = (255, 0 ,0)
green = (0,255,0)
blue = (0,0,255)
special_color = (243, 188, 171)

def main():
    pg.init()

    #Window creation
    screen = pg.display.set_mode(size)

    clock = pg.time.Clock()

    #Loop vars
    finish = False

    game = gm.Game(black)
    game.player.rect.y = 550


    #Player x and y movement
    vel = 0
    vel_y = 0

    #main loop
    while not finish:
        for event in pg.event.get():
            #Event exit

            if event.type == pg.QUIT:
                sys.exit()

            #Game start and finish

            if event.type == pg.MOUSEBUTTONDOWN:
                if game.gameover:
                    game.__init__(black)

            #Laser shoot

            if event.type == pg.MOUSEBUTTONDOWN:
                laser = sp.Laser_blast(black)
                laser.rect.x = game.player.rect.x + 250
                laser.rect.y = game.player.rect.y + 50
                game.laser_list.add(laser)
                game.sprite_list.add(laser)

            #Player movement

            if event.type == pg.KEYDOWN:
                if event.key == 32:
                    vel_y = -3
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_a or event.key == pg.K_LEFT:
                    vel = -3
                elif event.key == pg.K_d or event.key == pg.K_RIGHT:
                    vel = 3
            elif event.type == pg.KEYUP:
                if event.key == pg.K_a or event.key == pg.K_LEFT:
                    vel = 0
                elif event.key == pg.K_d or event.key == pg.K_RIGHT:
                    vel = 0

        #Position of the player icon

        vel = game.player.stop_move(game.player.rect.x, vel)

        if vel == 0 and game.player.rect.x <= 0:
            while game.player.rect.x <= 0:
                game.player.rect.x += 1
        elif vel == 0 and game.player.rect.x >= 1050:
            while game.player.rect.x >= 1050:
                game.player.rect.x -= 1

        game.player.rect.x += vel

        game.player.rect.y += vel_y

        if game.player.rect.y <= 200:
            vel_y *= -1
        elif game.player.rect.y >= 550:
            vel_y = 0
            game.player.rect.y = 550

        if game.player.rect.x >= game.obj.rect.x - 150 and game.player.rect.x <= game.obj.rect.x + 200:
            if game.player.rect.y <= 250:
                game.player.rect.y = 250

        
        #Logic stuff for game

        game.run_logic(size)
        game.display_refresh(screen, size, blue, white, black, special_color)
        clock.tick(120)
    
    pg.quit()

main()