import pygame
from pygame.locals import *
import sys
import time
import random


size_of_block = 30


class Food:
    # создаём класс еды для змейки

    def __init__(self, screen):
        self.screen = screen
        self.food = pygame.image.load('apple.png').convert()

        # задаём начальное положение змейки

        self.x = random.randint(1, 39) * size_of_block
        self.y = random.randint(1, 23) * size_of_block

    def draw_food(self):
        self.screen.blit(self.food, (self.x, self.y))
        pygame.display.flip()

    def move(self):
        self.x = random.randint(1, 39) * size_of_block
        self.y = random.randint(1, 23) * size_of_block


class Snake:
    # создаём класс змейки

    def __init__(self, screen, length):
        self.snake_length = length
        self.screen = screen
        self.block = pygame.image.load('block.jpg').convert()

        self.x = [30] * length
        self.y = [30] * length

        self.direction = 'down'

    def draw_snake_block(self):
        self.screen.fill('#000000')

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

    def update_snake_length(self):
        self.snake_length += 1
        self.x.append(-1)
        self.y.append(-1)


class Game:
    # создаём класс игрового процесса

    def __init__(self):
        pygame.init()

        self.size = self.width, self.height = 1200, 720
        self.surface = pygame.display.set_mode(self.size)

        pygame.display.set_caption('Snake Game')
        self.surface.fill('#000000')

        self.snake = Snake(self.surface, 10)
        self.snake.draw_snake_block()

        self.food = Food(self.surface)
        self.food.draw_food()

    def strike(self, x1, y1, x2, y2):
        # функции, когда змейка съедает еду

        if x1 >= x2 and x1 <= x2 + size_of_block:
            if y1 >= y2 and y1 <= y2 + size_of_block:
                return True

        return False

    def play(self):
        self.snake.body_moves()
        self.food.draw_food()

        if self.strike(self.snake.x[0], self.snake.y[0], self.food.x, self.food.y):
            self.food.move()

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

            self.play()

            time.sleep(0.1)


if __name__ == '__main__':
    game = Game()
    game.run()
    print('Game over:(')
