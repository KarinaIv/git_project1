import pygame
import sys

size = 1000, 700
screen = pygame.display.set_mode(size)
surf = pygame.Surface((30, 80))
surf.fill('#ff9a8d')

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    screen.fill('#aed6dc')
    screen.blit(surf, (500, 350))
    pygame.display.update()

