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

        # задаём начальное положение еды

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
        print('Your snake looks more and more like a real python!')

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

        self.snake = Snake(self.surface, 1)
        self.snake.draw_snake_block()

        self.food = Food(self.surface)
        self.food.draw_food()

    def strike(self, x1, y1, x2, y2):
        # функция, когда змейка съедает еду

        if x1 >= x2 and x1 < x2 + size_of_block:
            if y1 >= y2 and y1 < y2 + size_of_block:
                return True

        return False

    def play(self):
        self.snake.body_moves()
        self.food.draw_food()
        self.score()

        pygame.display.flip()

        if self.strike(self.snake.x[0], self.snake.y[0], self.food.x, self.food.y):
            self.snake.update_snake_length()
            self.food.move()

        # если змейка 'столкнулась' сама с собой
        for i in range(1, self.snake.snake_length):
            if self.strike(self.snake.x[0], self.snake.y[0], self.snake.x[i], self.snake.y[i]):

                raise "Your snake eat yourself"

        # если змейка врезалась в стенки экрана
        if not (0 <= self.snake.x[0] <= 1200 and 0 <= self.snake.y[0] <= 720):

            raise "Your snake hit the boundary"

    def game_over(self):

        font = pygame.font.SysFont('Cavorting', 30)
        line1 = font.render(f"Вы проиграли! Ваш рекорд {self.snake.snake_length}", True, (255, 0, 0))
        self.surface.blit(line1, (300, 310))

        line2 = font.render("Чтобы сыграть снова нажмите Enter. Чтобы выйти нажмите Escape", True, (255, 0, 0))
        self.surface.blit(line2, (300, 360))

        pygame.display.flip()

    def new_game(self):
        # функция перезапуска игры

        self.snake = Snake(self.surface, 1)
        self.food = Food(self.surface)

    def score(self):
        font = pygame.font.SysFont('Cavorting', 30)
        score = font.render(f"Рекорд: {self.snake.snake_length}", True, (255, 000, 000))

        self.surface.blit(score, (20, 20))

    def run(self):
        print("Let's go!!!")
        fail = False
        running = True

        while running:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == K_ESCAPE:
                        running = False

                    if event.key == K_RETURN or event.key == K_KP_ENTER:
                        fail = False

                    if not fail:

                        if event.key == K_RIGHT or event.key == K_d:
                            self.snake.move_right()
                        if event.key == K_LEFT or event.key == K_a:
                            self.snake.move_left()

                        if event.key == K_UP or event.key == K_w:
                            self.snake.move_up()
                        if event.key == K_DOWN or event.key == K_s:
                            self.snake.move_down()

                elif event.type == pygame.QUIT:
                    running = False

            try:

                if not fail:
                    self.play()

            except Exception as e:
                self.game_over()
                fail = True
                self.new_game()

            time.sleep(0.1)


if __name__ == '__main__':
    game = Game()
    game.run()
    print('Game over:(')

