# -*- coding: utf-8 -*-
import sys
import pygame
import sounddevice as sd
import numpy as np
import random
from threading import Thread
from sound_controller import sound_controller


pygame.init()
try:
    my_joystick = pygame.joystick.Joystick(0)
    my_joystick.init()
except pygame.error:
    print('Джойстик не был подключен')

fpsClock = pygame.time.Clock()
score_surf = pygame.Surface((100, 50))

width, height = 376, 700
pygame.display.set_mode((width, height), 0)
programIcon = pygame.image.load('./favicon.ico')  # Изменяем иконку
pygame.display.set_icon(programIcon)  # Смена иконки окна игры
button = pygame.image.load('sprites/i.png')  # Кнопка начала игры
button = pygame.transform.scale(button, (120, 60))
bg = pygame.image.load("sprites/background-day.png")  # Меняем фон
bg = pygame.transform.scale(bg, (width, height))
skins = [['yellowbird-downflap.png', 'yellowbird-midflap.png', 'yellowbird-upflap.png'],
         ['redbird-downflap.png', 'redbird-midflap.png', 'redbird-upflap.png'],
         ['bluebird-downflap.png', 'bluebird-midflap.png', 'bluebird-upflap.png']]
pipes = ['pipe-green.png', 'pipe-red.png']
score = ['0.png', '1.png', '2.png', '3.png', '4.png', '5.png', '6.png', '7.png', '8.png', '9.png']


class FlappyBird:
    def __init__(self):
        self.sound_controller = sound_controller()
        self.score_count = 0
        self.volume = 0
        self.screen = pygame.display.set_mode((width, height))  # Создаем экран
        self.selectedBird = 0  # Номер списка выбранной птицы
        self.selectedPipe = 0  # Номер списка идущей трубы
        self.position = 1  # Позиция анимации птицы
        self.speed = 1  # Множитель скорости
        self.buttonPlay = True  # Нажата кнопка или нет
        self.fillBackground()
        self.load_bird()
        self.pipeXY()
        self.load_pipe()
        self.click = 0  # Счетчик нажатий
        self.center = -1
        self.load_button()

    def buttons(self):  # Нажатия которые производят в игре
        if self.buttonPlay and 376 // 2 - 60 < event.pos[0] < 376 // 2 + 60 and 700 // 2 - 30 < event.pos[
            1] < 700 // 2 + 30:
            self.buttonPlay = False
        if not self.buttonPlay:
            self.sound_controller.play()
            self.fillBackground()
            self.update()
            self.screen.blit(pygame.transform.rotate(self.bird, 180), (self.birdX, self.birdY))
            self.screen.blit(self.pipe, (self.pipeX, self.pipeYU))

    def update(self):  # Обновление экрана
        self.birdY -= 0.03 * self.center
        if self.center > 0:
            self.position = 2
        elif self.center == 0:
            self.position = 1
        elif self.center < 0:
            self.position = 0
        self.load_bird()
        self.center -= 2  # Чтобы птица уходила вниз
        self.fillBackground()
        self.gameplay_pipe()
        self.screen.blit(self.bird, (self.birdX, self.birdY))  # отрисовываем птицу
        self.screen.blit(pygame.transform.rotate(self.pipe, 180), (self.pipeX, self.pipeYU))  # отрисовываем верхнюю трубу
        self.screen.blit(self.pipe, (self.pipeX, self.pipeYD))  # отрисовываем нижнюю трубу
        if self.birdY < 0 or self.birdY > 670 \
                or (self.pipeX - 19 < self.birdX + 17 < self.pipeX + 26 and self.pipeYU < self.birdY < self.pipeYU + 750) \
                or (self.pipeX - 19 < self.birdX + 17 < self.pipeX + 26 and self.pipeYD < self.birdY + 24 < self.pipeYD + 750) \
                or (self.pipeX - 19 < self.birdX < self.pipeX + 26 and self.pipeYU < self.birdY < self.pipeYU + 750) \
                or (self.pipeX - 19 < self.birdX < self.pipeX + 26 and self.pipeYD < self.birdY < self.pipeYD + 750):
            self.sound_controller.fail()
            self.fail()
        self.score()

    def fail(self):  # Проигрыш
        self.buttonPlay = True
        self.reset_game()
        self.load_button()
        self.gameover = pygame.image.load('sprites/gameover.png')
        self.pipeXY()
        self.screen.blit(self.gameover, (self.birdX + 12 - 96, self.birdY - 90))
        self.score_count = 0    
        self.speed = 1
        self.center = 0
        sound_controller.stop_all()
        sound_controller.fail()

    def fillBackground(self):  # Рисуем фон
        self.screen.blit(bg, (0, 0))

    def load_bird(self):
        self.bird = pygame.image.load('sprites/' + str(skins[self.selectedBird][self.position]))  # Кнопка начала игры

    def load_pipe(self):
        self.pipe = pygame.image.load('sprites/' + str(pipes[self.selectedPipe]))

    def pipeXY(self):
        self.pipeX = random.randint(400, 550)
        self.pipeYU = random.randint(-670, -150)
        self.pipeYD = self.pipeYU + 850

    def gameplay_pipe(self):
        self.pipeX -= 1 * self.speed
        if self.pipeX < -60:
            self.score_count += 1
            self.speed += 0.3
            self.pipeXY()

    def reset_game(self):
        self.fillBackground()

    def load_button(self):
        if self.buttonPlay:
            self.screen.blit(button, (width // 2 - 60, height // 2 - 30))
            self.birdX = width // 2 - 34 // 2
            self.birdY = height // 2 - 34 // 2

    def score(self):
        self.x = 0
        for i in range(len(str(self.score_count))):
            score_image = pygame.image.load('sprites/' + score[int(str(self.score_count)[i])])
            self.x += score_image.get_size()[0]
            self.screen.blit(score_image, (self.x, 0))


game = FlappyBird()


def print_sound(indata, *args):
    volume_norm = np.linalg.norm(indata) * 10
    game.volume = int(volume_norm)
    # print(game.volume)


def s(*args):
    with sd.Stream(callback=print_sound):
        sd.sleep(-1)


s = Thread(target=s)
s.start()


sound_controller = sound_controller()
while True:
    for event in pygame.event.get():
        keys = pygame.key.get_pressed()
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == pygame.MOUSEBUTTONDOWN or keys[pygame.K_SPACE] or event.type == pygame.JOYBUTTONUP:
            # Срабатывает при нажатии на кнопку или при на кнопки на джойстике
            if game.buttonPlay:
                game.buttons()
            elif not game.buttonPlay:
                game.center += 80
                sound_controller.swoosh()
    if not game.buttonPlay:
        game.update()
        if game.volume > 20:
            if not game.buttonPlay:
                game.center += 5
    fpsClock.tick(120)
    pygame.display.flip()