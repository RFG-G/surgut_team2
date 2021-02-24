import pygame
import random
background = ['background2.mp3', 'background2.mp3', 'background3.mp3', 'background4.mp3', 'background5.mp3']


class sound_controller:
    def __init__(self):
        sound_position = random.randint(0, 4)
        self.sound = pygame.mixer.Sound('audio/background/' + str(background[sound_position]))
        self.fail_audio = pygame.mixer.Sound('audio/die.ogg')
        self.swoosh_audio = pygame.mixer.Sound('audio/swoosh.ogg')
        self.coin_audio = pygame.mixer.Sound('audio/point.ogg')

    def play(self):
        self.sound.play()

    def fail(self):
        self.fail_audio.play()

    def swoosh(self):
        self.swoosh_audio.play()

    def coin(self):
        self.coin_audio.play()

    def stop_all(self):
        pygame.mixer.stop()