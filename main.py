import sys

import pygame
from pygame.locals import *

pygame.init()

fps = 60
fpsClock = pygame.time.Clock()

width, height = 576, 900
screen = pygame.display.set_mode((width, height))

while True:
    screen.fill((255, 255, 255))

    # FPS
    fps_text = pygame.font.Font(None, 48).render('FPS:' + str(int(fpsClock.get_fps())), True, (1, 1, 1))
    screen.blit(fps_text, (10, 25))

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            print('closed')
            sys.exit()

    pygame.display.flip()
    fpsClock.tick(fps)
