import pygame
from pygame.locals import *
import sys
import time

size_of_block = 30


class Snake:
    # создаём класс змейки

    def __init__(self, screen):
        self.snake_length = 1
        self.screen = screen
        self.block = pygame.image.load('block.png').convert()
        self.x = [30]
        self.y = [30]
        self.direction = 'down'

    def draw_snake_block(self):
        self.screen.fill('#aed6dc')
        for i in range(self.snake_length):
            self.screen.blit(self.block, (self.x[i], self.y[i]))

        pygame.display.flip()

    def move_up(self):
        self.direction = 'up'

    def move_down(self):
        self.direction = 'down'

    def move_left(self):
        self.direction = 'left'

    def move_right(self):
        self.direction = 'right'

    def body_moves(self):
        # обновление тела

        for i in range(self.snake_length - 1, 0, -1):
            self.x[i] = self.x[i - 1]
            self.y[i] = self.y[i - 1]

        # изменение направления движения головы

        if self.direction == 'up':
            self.y[0] -= size_of_block
        if self.direction == 'down':
            self.y[0] += size_of_block

        if self.direction == 'left':
            self.x[0] -= size_of_block
        if self.direction == 'right':
            self.x[0] += size_of_block

        self.draw_snake_block()


class Game:
    # создаём класс игрового процесса

    def __init__(self):
        pygame.init()

        self.size = self.width, self.height = 1000, 700
        self.screen = pygame.display.set_mode(self.size)

        pygame.display.set_caption('Snake Game')
        self.screen.fill('#aed6dc')

        self.snake = Snake(self.screen)
        self.snake.draw_snake_block()

    def run(self):
        print("Let's go!!!")
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

            self.snake.body_moves()
            time.sleep(0.3)


if __name__ == '__main__':
    game = Game()
    game.run()
    print('Game over:(')
