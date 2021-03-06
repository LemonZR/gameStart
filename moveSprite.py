import pygame
import sys
import os
import random
import time
from pygame.locals import *

pygame.init()
white = (255, 255, 255)
black = (0, 0, 0)

screen_w = 800
screen_h = 600

screen = pygame.display.set_mode((screen_w, screen_h))
pygame.display.set_caption("move test")  # Here I create a display.
icon = pygame.image.load('bilibili.ico')
pygame.display.set_icon(icon)
clock = pygame.time.Clock()


class Car(pygame.sprite.DirtySprite):  # Here I create a class.

    def __init__(self, color=black, width=100, height=100):
        pygame.sprite.DirtySprite.__init__(self)

        self.image = pygame.Surface((width, height))

        self.image.fill(color)

        self.rect = self.image.get_rect()

    def set_pos(self, x, y):
        self.rect.x = x
        self.rect.y = y

    def set_img(self, filename=None):
        if filename:
            self.image = pygame.image.load(filename)
            self.rect = self.image.get_rect()


def main():
    x_change = 0
    y_change = 0

    x = 0
    y = 0

    car_group = pygame.sprite.Group()  # Make a group

    player = Car()

    player.set_img("bilibili.ico")

    car_group.add(player)

    go_exit = False

    FPS = 60
    #
    while not go_exit:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_LEFT:
                    x_change = -10

                elif event.key == pygame.K_RIGHT:
                    x_change = 10

                elif event.key == pygame.K_UP:
                    y_change = -10

                elif event.key == pygame.K_DOWN:
                    y_change = 10

            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    y_change = 0
                    if x_change != 0:
                        x_change = x_change / abs(x_change)  # 保持移动方向，速度1

                if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    x_change = 0
                    if y_change != 0:
                        y_change = y_change / abs(y_change)

        x += x_change
        y += y_change
        if x > screen_w:
            x = 0
        if x < 0:
            x = screen_w
        if y > screen_h:
            y = 0
        if y < 0:
            y = screen_h
        screen.fill(black)
        player.set_pos(x, y)  # Blit the player to the screen
        car_group.draw(screen)
        clock.tick(FPS)
        pygame.display.update()


if __name__ == '__main__':
    main()
    pygame.quit()
    sys.exit()
