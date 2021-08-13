import sys, pygame

import interval
from pygame.locals import *
from interval import Interval

pygame.init()

size = width, height = 320, 240
speed = [1, 1]
black = 0, 0, 0

screen = pygame.display.set_mode(size)
#
# ball = pygame.image.load("intro_ball.gif")

ball = pygame.image.load("bilibili.ico")
ballrect = ball.get_rect()

print(ballrect)
clock = pygame.time.Clock()
while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == MOUSEBUTTONDOWN:
            x = pygame.mouse.get_pos()[0]
            y = pygame.mouse.get_pos()[1]

            mouse_area = pygame.Rect(x - 10, y - 10, x + 10, y + 10)

            if ballrect.colliderect(mouse_area):
                if (ballrect.centerx - x) * speed[0] < 0:
                    speed[0] = -speed[0]
                if (ballrect.centery - y) * speed[0] < 0:
                    speed[1] = -speed[1]

    if ballrect.left < 0 or ballrect.right > width:
        speed[0] = -speed[0]
    if ballrect.top < 0 or ballrect.bottom > height:
        speed[1] = -speed[1]
    ballrect = ballrect.move(speed)
    screen.fill(black)
    screen.blit(ball, ballrect)
    pygame.display.flip()
    clock.tick(60)
