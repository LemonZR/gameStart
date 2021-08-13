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
    # pygame.display.flip()
    while not go_exit:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            pygame.display.update()
            car_group.draw(screen)
            clock.tick(FPS)


if __name__ =='__main__':
    main()