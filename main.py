import pygame
from pygame.locals import *
import sys


def draw_snake_block():
    screen.fill('#aed6dc')
    screen.blit(block, (block_x, block_y))
    pygame.display.flip()


if __name__ == '__main__':
    pygame.init()

    size = width, height = 1000, 700
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption('Snake Game')
    screen.fill('#aed6dc')

    block = pygame.image.load('block.png').convert()

    block_x = 0
    block_y = 0
    screen.blit(block, (block_x, block_y))

    pygame.display.flip()
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False

                if event.key == K_RIGHT or event.key == K_d:
                    block_x += 5
                    draw_snake_block()
                if event.key == K_LEFT or event.key == K_a:
                    block_x -= 5
                    draw_snake_block()

                if event.key == K_UP or event.key == K_w:
                    block_y -= 5
                    draw_snake_block()
                if event.key == K_DOWN or event.key == K_s:
                    block_y += 5
                    draw_snake_block()


            if event.type == pygame.QUIT:
                running = False


        pygame.display.flip()

    pygame.quit()
