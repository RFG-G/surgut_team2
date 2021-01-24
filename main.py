import sys

import pygame

pygame.init()

fps = 60
fpsClock = pygame.time.Clock()

width, height = 376, 700
screen = pygame.display.set_mode((width, height))

programIcon = pygame.image.load('./favicon.ico')  # Изменяем иконку
pygame.display.set_icon(programIcon)
button = pygame.image.load('sprites/i.png')  # Кнопка начала игры
button = pygame.transform.scale(button, (120, 60))
buttonCount = True
while True:
    bg = pygame.image.load("sprites/background-day.png")  # Меняем фон
    bg = pygame.transform.scale(bg, (width, height))
    screen.blit(bg, (0, 0))
    if buttonCount:
        screen.blit(button, (376 // 2 - 60, 700 // 2 - 30))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if buttonCount and 376 // 2 - 60 < event.pos[0] < 376 // 2 + 60 and 700 // 2 - 30 < event.pos[1] < 700 // 2 + 30:
                buttonCount = False
    pygame.display.flip()
    fpsClock.tick(fps)
