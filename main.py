import pygame
from pygame.locals import *
import sys

size_of_block = 30


class Snake:
    def __init__(self, screen):
        self.snake_length = 1
        self.screen = screen
        self.block = pygame.image.load('block.png').convert()
        self.x = [30]
        self.y = [30]

    def draw_snake_block(self):
        self.screen.fill('#aed6dc')
        for i in range(self.snake_length):
            self.screen.blit(self.block, (self.x[i], self.y[i]))

        pygame.display.flip()

    def move_up(self):
        self.y[0] -= size_of_block
        self.draw_snake_block()

    def move_down(self):
        self.y[0] += size_of_block
        self.draw_snake_block()

    def move_left(self):
        self.x[0] -= size_of_block
        self.draw_snake_block()

    def move_right(self):
        self.x[0] += size_of_block
        self.draw_snake_block()


class Game:
    def __init__(self):
        pygame.init()

        self.size = self.width, self.height = 1000, 700
        self.screen = pygame.display.set_mode(self.size)
        pygame.display.set_caption('Snake Game')
        self.screen.fill('#aed6dc')

        self.snake = Snake(self.screen)
        self.snake.draw_snake_block()

    def run(self):
        running = True

        while running:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == K_ESCAPE:
                        running = False

                    if event.key == K_RIGHT or event.key == K_d:
                        self.snake.move_right()
                    if event.key == K_LEFT or event.key == K_a:
                        self.snake.move_left()

                    if event.key == K_UP or event.key == K_w:
                        self.snake.move_up()
                    if event.key == K_DOWN or event.key == K_s:
                        self.snake.move_down()

                if event.type == pygame.QUIT:
                    running = False


if __name__ == '__main__':
    game = Game()
    game.run()
