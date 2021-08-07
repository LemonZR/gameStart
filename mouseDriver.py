import os, pygame

from pygame.locals import *

from sys import exit

import moveSprite
from random import *

pygame.init()

white = (255, 255, 255)
black = (0, 0, 0)

screenw = 800
screenh = 600

screen = pygame.display.set_mode((screenw, screenh))

pygame.display.set_caption("Game")  # Here I create a display.

clock = pygame.time.Clock()


def main():
    car_group = pygame.sprite.Group()  # Make a group

    player = moveSprite.Car()
    player2 = moveSprite.Car()

    player.set_img("bilibili.ico")
    player2.set_img("bilibili.ico")
    car_group.add(player,player2)


    go_exit = False

    FPS = 60

    while 1:

        for event in pygame.event.get():

            if event.type == QUIT:

                exit()

            elif event.type == MOUSEBUTTONDOWN:

                pressed_array = pygame.mouse.get_pressed()

                for index in range(len(pressed_array)):

                    if pressed_array[index]:

                        if index == 0:

                            print('Pressed LEFT Button!')

                        elif index == 1:

                            print('The mouse wheel Pressed!')

                        elif index == 2:

                            print('Pressed RIGHT Button!')

            elif event.type == MOUSEMOTION:

                # return the X and Y position of the mouse cursor

                pos = pygame.mouse.get_pos()

                mouse_x = pos[0]

                mouse_y = pos[1]
                player.set_pos(mouse_x, mouse_y)  # Blit the player to the screen
        screen.fill(black)
        car_group.draw(screen)
        clock.tick(FPS)
        pygame.display.update()


if __name__ == '__main__':
    main()