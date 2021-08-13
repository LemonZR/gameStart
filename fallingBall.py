import pygame
import pymunk


def main():
    x = 45
    y = 10
    vx = 1
    vy = 0
    g = 9.8
    pygame.init()
    clock = pygame.time.Clock()
    area = [1500, 150]
    screen = pygame.display.set_mode(area)
    pygame.display.set_caption("PHY")
    time = 0
    while time < 10:
        screen.fill(0)
        event = pygame.event.poll()
        if event.type == pygame.QUIT:
            pygame.quit()
            exit(0)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_n:
                pygame.quit()
                exit(0)
        clock.tick(60)

        x += vx
        vy = vy + g * time
        y = y + vy * time
        print(vy)

        if y > 100:
            y = 100
            vy = -vy

        pygame.draw.circle(screen, [100, 0, 0], [x, y], 10)
        pygame.display.update()
        time += 1 / 60
        clock.tick(60)


if __name__ == "__main__":
    main()
