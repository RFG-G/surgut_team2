import sys

import pygame
from pygame.locals import *

pygame.init()

fps = 60
fpsClock = pygame.time.Clock()

width, height = 376, 700
screen = pygame.display.set_mode((width, height))

programIcon = pygame.image.load('./favicon.ico')
pygame.display.set_icon(programIcon)

while True:
    # FPS
    fps_text = pygame.font.Font(None, 48).render('FPS:' + str(int(fpsClock.get_fps())), True, (1, 1, 1))
    screen.blit(fps_text, (10, 25))

    bg = pygame.image.load("sprites/background-day.png")
    bg = pygame.transform.scale(bg, (width, height))
    screen.blit(bg, (0, 0))
    print(feature_1)
    print("ыфвфыв")
    print(feature_1)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            print('closed')
            sys.exit()

    pygame.display.flip()
    fpsClock.tick(fps)
