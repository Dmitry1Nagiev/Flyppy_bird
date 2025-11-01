from sprites.button import *
import random

import pygame
import os

current_path = os.path.dirname(__file__)
os.chdir(current_path)
pygame.init()
WIDHT = 400
HEIGHT = 100
N_BALLS = 3

WHITE = 255,255,255
GRAY = 239,239,239
COLOR = GRAY
screen = pygame.display.set_mode((WIDHT,HEIGHT))
pygame.display.set_caption('')
FPS = 60
clock = pygame.time.Clock()
window = pygame.display.set_mode((WIDHT,HEIGHT))
ControlFps = 0
button = SimpleButton(window,(150,30),r'assets/images/buttonUp.png',
                                        r'assets/images/buttonDown.png')

pygame.init()


running = True
while running:



    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        if button.handleEvent(event):
            print('Ты нажал кнопку, поздравляю.')
    window.fill(GRAY)
    button.draw()
    pygame.display.update()
    clock.tick(FPS)


pygame.quit()