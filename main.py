import pygame
from pygame.locals import *
import sys


if __name__ == '__main__':
    pygame.init()
    size = width, height = 1000, 700
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption('Snake Game')
    screen.fill('#aed6dc')

    block = pygame.image.load('block.png').convert()
    screen.blit(block, (500, 350))

    pygame.display.flip()
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
            if event.type == pygame.QUIT:
                running = False


        pygame.display.flip()

    pygame.quit()
