import pygame
from constants import *



def main():
    pygame.init()
    timer = pygame.time.Clock()
    dt = 0

    running = True

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")
        pygame.display.flip()
        dt = timer.tick(60) / 1000

if __name__ == "__main__":
    main()