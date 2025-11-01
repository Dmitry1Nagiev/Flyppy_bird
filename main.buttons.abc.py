from sprites.buttons import *
import random

import pygame
import os

pygame.display.set_caption('Кнопочке')
current_path = os.path.dirname(__file__)
os.chdir(current_path)
pygame.init()
WIDHT = 700
HEIGHT = 200
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
buttonA = SimpleButton(window,(15,30),r'assets/images/buttonUpA.png',
                                        r'assets/images/buttonDownA.png')
buttonB = SimpleButton(window,(210,30),r'assets/images/buttonDownB.png',
                                        r'assets/images/buttonUpB.png',
                                            callBack=myCallBackFunction)
myCallBack = CallBackClass()
buttonC = SimpleButton(window,(400,30),r'assets/images/buttonUpC.png',
                                        r'assets/images/buttonDownC.png',
                                                callBack=myCallBack.myMethod)


pygame.init()


running = True
while running:



    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        if buttonA.handleEvent(event):
            print('Ты нажал первую кнопку, поздравляю.')

        buttonB.handleEvent(event)
        buttonC.handleEvent(event)
    window.fill(WHITE)
    buttonA.draw()
    buttonB.draw()
    buttonC.draw()
    pygame.display.update()
    clock.tick(FPS)


pygame.quit()