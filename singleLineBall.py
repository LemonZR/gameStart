import sys
import pygame
from pygame.locals import *
import pymunk
import pymunk.constraints

# some const
RADIUS = 10
SCREEN_SIZE = 600
FPS = 60
POINT_SIZE = 5
STRING_SIZE = 2

# init screen
pygame.init()
screen = pygame.display.set_mode((SCREEN_SIZE, SCREEN_SIZE))
pygame.display.set_caption("title")
clock = pygame.time.Clock()
# init simul space
space = pymunk.Space()
space.gravity = (0., -900.)


class Ball:
    def __init__(self, x, y):
        self.body = pymunk.Body()
        self.body.position = x, y
        self.shape = pymunk.Circle(self.body, RADIUS)
        self.shape.density = 1.
        self.shape.elasticity = 1.
        space.add(self.body, self.shape)

    def draw(self):
        index = int(self.body.position[0]), SCREEN_SIZE - int(self.body.position[1])
        pygame.draw.circle(screen, (0, 0, 255), index, RADIUS, POINT_SIZE)


class String:
    def __init__(self, body1, body2, isBody=True):
        self.body1 = body1
        if isBody:
            self.body2 = body2
        else:
            self.body2 = pymunk.Body(body_type=pymunk.Body.STATIC)
            self.body2.position = body2
        joint = pymunk.PinJoint(self.body1, self.body2)
        space.add(joint)

    def draw(self):
        index1 = int(self.body1.position[0]), SCREEN_SIZE - int(self.body1.position[1])
        index2 = int(self.body2.position[0]), SCREEN_SIZE - int(self.body2.position[1])
        pygame.draw.line(screen, (0, 0, 0), index1, index2, STRING_SIZE)


def main():
    # init balls
    myball1 = Ball(400, 400)
    myball2 = Ball(500, 300)
    string1 = String(myball1.body, (300, 500), isBody=False)
    string2 = String(myball1.body, myball2.body, isBody=True)
    objects = [myball1, myball2, string1, string2]

    while True:
        # press "esc" to exit
        event = pygame.event.poll()
        if event.type == pygame.QUIT:
            pygame.quit()
            exit(0)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_n:
                pygame.quit()
                exit(0)
        # move forward one step on simul envi
        space.step(1 / FPS)
        # render
        screen.fill((255, 255, 255))
        for obj in objects:
            obj.draw()
        # display the result
        pygame.display.flip()
        clock.tick(FPS)


if __name__ == '__main__':
    sys.exit(main())
