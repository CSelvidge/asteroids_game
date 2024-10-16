import pygame
from constants import *
from player import Player



def main():
    pygame.init()
    timer = pygame.time.Clock()
    dt = 0
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    running = True

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")
        player.draw(screen)
        pygame.display.flip()
        dt = timer.tick(60) / 1000

if __name__ == "__main__":
    main()