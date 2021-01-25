# -*- coding: utf-8 -*-
import sys
import pygame

pygame.init()
try:
    my_joystick = pygame.joystick.Joystick(0)
    my_joystick.init()
except pygame.error:
    print('Джойстик не был подключен')


fps = 120
fpsClock = pygame.time.Clock()

width, height = 376, 700
pygame.display.set_mode((width, height), 0)
programIcon = pygame.image.load('./favicon.ico')  # Изменяем иконку
pygame.display.set_icon(programIcon)
button = pygame.image.load('sprites/i.png')  # Кнопка начала игры
button = pygame.transform.scale(button, (120, 60))
bg = pygame.image.load("sprites/background-day.png")  # Меняем фон
bg = pygame.transform.scale(bg, (width, height))


class FlappyBird:
    def __init__(self):
        self.screen = pygame.display.set_mode((width, height))  # Создаем экран
        self.selectedBird = 0  # Выбранная птица
        self.buttonPlay = True  # Отображается кнопка или нет
        self.fillBackground()
        self.bird = pygame.image.load('sprites/yellowbird-midflap.png')  # Кнопка начала игры
        self.birdX = width // 2 - 34 // 2
        self.birdY = height // 2 - 34 // 2
        self.click = 0  # Счетчик нажатий
        self.center = -1
        if self.buttonPlay:
            self.screen.blit(button, (width // 2 - 60, height // 2 - 30))

    def buttons(self):  # Нажатия которые производят в игре
        if self.buttonPlay and 376 // 2 - 60 < event.pos[0] < 376 // 2 + 60 and 700 // 2 - 30 < event.pos[
            1] < 700 // 2 + 30:
            self.buttonPlay = False
        if not self.buttonPlay:
            self.fillBackground()
            self.update()
            self.screen.blit(self.bird, (self.birdX, self.birdY))

    def update(self):
        self.birdY -= 0.03 * self.center
        self.center -= 2
        self.fillBackground()  # Закрашиваем фон
        self.screen.blit(self.bird, (self.birdX, self.birdY))   # отрисовываем птицу

    def death(self):
        self.buttonPlay = True

    def fillBackground(self):
        self.screen.blit(bg, (0, 0))  # Рисуем фон


game = FlappyBird()
while True:
    for event in pygame.event.get():
        keys = pygame.key.get_pressed()
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == pygame.MOUSEBUTTONDOWN or keys[pygame.K_SPACE] or event.type == pygame.JOYBUTTONUP:
            if game.buttonPlay:
                game.buttons()
            elif not game.buttonPlay:
                game.center += 80
    if not game.buttonPlay:
        game.update()
    pygame.display.flip()
    fpsClock.tick(fps)