from sprites.ball import *
from sprites.button import *
from sprites.buttons import *

import random
import pygwidgets
import pygame
import os

current_path = os.path.dirname(__file__)
os.chdir(current_path)
pygame.init()
WIDHT = 1000
HEIGHT = 600
N_BALLS = 1
BLACK = (0,0,0)
WHITE = 255,255,255
GRAY = 239,239,239
screen = pygame.display.set_mode((WIDHT,HEIGHT))
pygame.display.set_caption('')
FPS = 60
clock = pygame.time.Clock()
pygame.init()


def orderBurgers(nBurgers,Ketchup=True,mustard=True,pickles=True):

    orderBurgers(3)
    orderBurgers(3,False)
    orderBurgers(3,mustard=False)

def orderPizza(size,style='regular',topping=None):

    orderPizza('large')
    orderPizza('large', style='regular')
    orderPizza('medium',style='deepdish',topping='mushrooms')
    orderPizza('small',topping='mushrooms')

bg = pygwidgets.Image(screen,(0,0),
                      r'assets/images/Fon.png')
button1 = pygwidgets.TextButton(screen,(500,370),'нажми')

textA = pygwidgets.DisplayText(screen,(20,50),
                               'Текст 1',fontSize=36,
                               textColor=WHITE)

textB = pygwidgets.DisplayText(screen,(20,150),
                               'Строка 1\nСтрока 2\nСтрока 3',
                               fontSize=36,textColor=WHITE,
                               justified='center')
inputA = pygwidgets.InputText(screen,(20,350),'',
                               fontSize=36,textColor=BLACK,
                              backgroundColor=WHITE)
inputB = pygwidgets.InputText(screen,(20,430),'',
                               width=400,fontSize=30,
                              textColor=WHITE,backgroundColor=BLACK)







#button = SimpleButton(screen,(730,450),r'assets/images/buttonUp.png',
                                        #r'assets/images/buttonDown.png')

myFont = pygame.font.SysFont('Comic Sans MS',30)

textSurface = myFont.render('Some text', True,(0,0,0))

screen.blit(textSurface,(10,10))

#buttonA = SimpleButton(screen,(15,30),r'assets/images/buttonUpA.png',
                                        #r'assets/images/buttonDownA.png')
#buttonB = SimpleButton(screen,(210,30),r'assets/images/buttonDownB.png',
                                        #r'assets/images/buttonUpB.png',
                                            #callBack=myCallBackFunction)
#myCallBack = CallBackClass()
#buttonC = SimpleButton(screen,(400,30),r'assets/images/buttonUpC.png',
                                        #r'assets/images/buttonDownC.png',
                                                #callBack=myCallBack.myMethod)




countLabel = SimpleText(screen,(160,20),'Счётчик кликов:' ,  BLACK)

countText = SimpleText(screen,(400,20),'',BLACK)

counter = 0

restartButton = SimpleButton(screen,(700,500),r'assets/images/R_UP.png',
                                               r'assets/images/R_DOWN.png')

ballGroup = pygame.sprite.Group()
for i in range(N_BALLS) :
    ball = Ball(screen,WIDHT, HEIGHT)
    ballGroup.add(ball)

ballGroup.update()
ballGroup.draw(screen)

running = True
while running:



    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            if ball.rect.collidepoint(mouse_pos):
                counter += 1
        #if buttonA.handleEvent(event):
            #print('Ты нажал первую кнопку, поздравляю.')
        if restartButton.handleEvent(event):
            counter = 0
            #for sprite in ballGroup:
                #if sprite.rect.collidepoint(mouse_pos):
                    #sprite.kill()
        if button1.handleEvent(event):
            print('кнопка была нажата')
        if inputA.handleEvent(event):
            userText = inputA.getText()
            print(f'В первое поле ввода пользователь ввел: {userText}')
        if inputB.handleEvent(event):
            userText = inputB.getText()
            print(f'Во второе поле ввода пользователь ввел: {userText}')
            if len(ballGroup) == 0:
                running = False
        #if button.handleEvent(event):
            #print('Ты нажал кнопку, поздравляю.')


        #buttonB.handleEvent(event)
        #buttonC.handleEvent(event)
    screen.fill(WHITE)
    ballGroup.update()
    #button.draw()
    ballGroup.draw(screen)
    countLabel.draw()
    countText.draw()
    countText.setValue(str(counter))
    restartButton.draw()
    #buttonA.draw()
    #buttonB.draw()
    #buttonC.draw()
    pygame.display.update()



    clock.tick(FPS)


pygame.quit()
