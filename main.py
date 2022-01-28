import pygame
from pygame.locals import *
import sys
import time
import os
import random


pygame.init()
sc = pygame.display.set_mode((400, 300))

pygame.mixer.music.load('music.mp3')
pygame.mixer.music.play()
#
sound1 = pygame.mixer.Sound('music.mp3')
sound2 = pygame.mixer.Sound('music.mp3')

size_of_block = 30
dis_width = 1200
dis_height = 720
size = dis_width, dis_height
screen = pygame.display.set_mode(size)
FPS = 50


def load_image(name, colorkey=None):
    fullname = name
    # если файл не существует, то выходим
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    image = pygame.image.load(fullname)
    if colorkey is not None:
        image = image.convert()
        if colorkey == -1:
            colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey)
    else:
        image = image.convert_alpha()
    return image


class Splashscreen:
    def __init__(self):
        self.show = True

    @staticmethod
    def terminate():
        pygame.quit()
        sys.exit()

    def start_screen(self):
        # print(self.show)
        if self.show:
            intro_text = ["", "",
                          "Нажмите на пробел, чтобы начать игру",
                          "Нажмите на клавишу r, чтобы перейти к правилам игры",
                          "Нажмите на клавишу Esc, чтобы выйти из игры"]

            fon = pygame.transform.scale(load_image('fon.jpg'), (dis_width, dis_height))
            screen.blit(fon, (0, 0))
            font = pygame.font.Font(None, 30)
            text_coord = 50
            for line in intro_text:
                string_rendered = font.render(line, 1, pygame.Color('red'))
                intro_rect = string_rendered.get_rect()
                text_coord += 10
                intro_rect.top = text_coord
                intro_rect.x = 10
                text_coord += intro_rect.height
                screen.blit(string_rendered, intro_rect)
            pygame.display.flip()

    def regulations(self):
        if self.show:
            img = pygame.image.load('rules.jpg')
            print('Я работаю')
            #screen = pygame.display.set_mode(img.get_size(), pygame.FULLSCREEN)
            screen.blit(img, (0, 0))
            pygame.display.flip()


splashscr = Splashscreen()


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
        splashscr.start_screen()
        pygame.display.flip()

    def move(self):
        self.x = random.randint(1, 39) * size_of_block
        self.y = random.randint(1, 23) * size_of_block


class Snake:
    # создаём класс змейки
    def __init__(self, screen, length):
        self.snake_length = length
        self.screen = screen
        self.block = pygame.image.load('circle.png').convert()

        self.x1 = dis_width / 2
        self.y1 = dis_height / 2

        self.x = [size_of_block] * length
        self.y = [size_of_block] * length

        self.direction = 'down'

    def draw_snake_block(self):
        self.screen.fill('#000000')

        for i in range(self.snake_length):
            self.screen.blit(self.block, (self.x[i], self.y[i]))

        pygame.display.flip()

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


class MyGameException(Exception):
    pass


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
                raise MyGameException("Your snake eat yourself")

        # если змейка врезалась в стенки экрана
        if not (0 <= self.snake.x[0] <= 1200 and 0 <= self.snake.y[0] <= 720):
            raise MyGameException("Your snake hit the boundary")

    def game_over(self):

        font = pygame.font.SysFont('Cavorting', 30)
        line1 = font.render(f"Вы проиграли! Ваш счёт {self.snake.snake_length}", True, (255, 0, 0))
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
        count = font.render(f"Счёт: {self.snake.snake_length}", True, (255, 000, 000))
        self.surface.blit(count, (20, 20))

        with open('score.txt', 'r') as f:
            tnp = int(f.read())

        with open('score.txt', 'w') as f:
            f.write(str(max(tnp, self.snake.snake_length)))

        font1 = pygame.font.SysFont('Cavorting', 30)
        score = font1.render(f"Рекорд: {tnp}", True, (255, 000, 000))
        self.surface.blit(score, (1050, 30))

    def run(self):
        print("Let's go!!!")

        fail = False
        running = True
        # clock = pygame.time.Clock()
        flag = True
        flag_rules = False
        splashscr.start_screen()
        while running:
            for event in pygame.event.get():
                print(event)
                print(flag_rules)
                if flag:
                    if event.type == pygame.QUIT:
                        splashscr.terminate()
                    if event.type == pygame.KEYDOWN and event.key == pygame.K_r:
                        # splashscr.show = False
                        flag_rules = True
                        print('rul')
                        splashscr.regulations()
                        print('Захожу сюда')
                        #input("")
                        continue

                    if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE and flag_rules:
                        print('пробел')
                        #splashscr.show = True
                        flag_rules = False
                        # fail = False
                        splashscr.start_screen()

                    if event.type == pygame.MOUSEBUTTONDOWN:
                        flag = False
                        splashscr.show = False
                        print('Клик удался')
                        continue
                    if event.type != pygame.KEYDOWN and \
                            event.type == pygame.MOUSEBUTTONDOWN:
                        flag = False
                        splashscr.show = False
                        print('elsee')

                else:
                    # while 1:
                    if event.type == pygame.QUIT:
                        sys.exit()

                    elif event.type == pygame.KEYUP:
                        if event.key == pygame.K_1:
                            pygame.mixer.music.pause()
                            # pygame.mixer.music.stop()
                        elif event.key == pygame.K_2:
                            pygame.mixer.music.unpause()
                            # pygame.mixer.music.play()
                            pygame.mixer.music.set_volume(0.5)
                        elif event.key == pygame.K_3:
                            pygame.mixer.music.unpause()
                            # pygame.mixer.music.play()
                            pygame.mixer.music.set_volume(1)

                    elif event.type == pygame.MOUSEBUTTONUP:
                        for i in range(1, 50):
                            pass
                            # if pygame.mixer.music.get_num_channels() != i:
                            #    sound1.play()

                        if event.button == 1:
                            sound1.play()
                        elif event.button == 3:
                            sound2.play()

                        pygame.time.delay(20)

                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_ESCAPE:
                            running = False
                        if event.key == pygame.K_RETURN or event.key == pygame.K_KP_ENTER:
                            fail = False

                        if not fail:
                            if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                                self.snake.direction = 'right'
                            if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                                self.snake.direction = 'left'

                            if event.key == pygame.K_UP or event.key == pygame.K_w:
                                self.snake.direction = 'up'
                            if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                                self.snake.direction = 'down'
                    elif event.type == pygame.QUIT:
                        running = False
            try:
                if not fail:
                    if flag:
                        splashscr.start_screen()
                    else:
                        self.play()


            except MyGameException as e:
                self.game_over()
                fail = True
                self.new_game()
            time.sleep(0.1)


if __name__ == '__main__':
    game = Game()
    game.run()
    print('Game over:(')