import random
from pygame.locals import *
import pygame


WHITE = 255,255,255


class Ball(pygame.sprite.Sprite):

    def __init__(self, window, windowWidth, windowHeight):
        super().__init__()
        self.window = window  # remember the window, so we can draw later
        self.windowWidth = windowWidth
        self.windowHeight = windowHeight

        self.image = pygame.image.load(r'assets/images/ball.png')
        self.rect = self.image.get_rect()
        self.image.set_colorkey(WHITE)
        self.maxWidth = windowWidth - self.rect.width
        self.maxHeight = windowHeight - self.rect.height

        # Pick a random starting position
        self.rect.x = random.randrange(0, self.maxWidth)
        self.rect.y = random.randrange(0, self.maxHeight)

        # Choose a random speed between -4 and 4, but not zero
        # in both the x and y directions
        speedsList = [-4, -3, -2, -1, 1, 2, 3, 4]
        self.xSpeed = random.choice(speedsList)
        self.ySpeed = random.choice(speedsList)

    def update(self):
        # Check for hitting a wall.  If so, change that direction.
        if self.rect.x < 0 or self.rect.x >= self.maxWidth:
            self.xSpeed = -self.xSpeed

        if self.rect.y < 0 or self.rect.y >= self.maxHeight:
            self.ySpeed = -self.ySpeed

        # Update the Ball's x and y, using the speed in two directions
        self.rect.x += self.xSpeed
        self.rect.y += self.ySpeed

    def draw(self):
        self.window.blit(self.image, self.rect)


class SimpleButton():
    STATE_IDLE = 'idle'
    STATE_ARMED = 'armed'
    STATE_DISAMED = 'disarmed'
    def __init__(self, window,loc,up,down):
        self.window = window
        self.loc = loc
        self.surfaceUp = pygame.image.load(up)
        self.surfaceDown = pygame.image.load(down)
        self.surfaceUp.set_colorkey(WHITE)
        self.surfaceDown.set_colorkey(WHITE)


        self.rect = self.surfaceUp.get_rect()
        self.rect[0] = loc[0]
        self.rect[1] = loc[1]
        self.state = SimpleButton.STATE_IDLE


    def handleEvent(self,eventObj):

        if eventObj.type not in (MOUSEMOTION, MOUSEBUTTONUP,MOUSEBUTTONDOWN):


            return False
        eventPointInButtonRect = self.rect.collidepoint(eventObj.pos)


        if self.state == SimpleButton.STATE_IDLE:
            if eventObj.type == MOUSEBUTTONDOWN and eventPointInButtonRect:
                self.state = SimpleButton.STATE_ARMED
        elif self.state == SimpleButton.STATE_ARMED:
            if eventObj.type == MOUSEBUTTONUP and eventPointInButtonRect:
                self.state = SimpleButton.STATE_IDLE
                return True
            if eventObj.type == MOUSEMOTION and not eventPointInButtonRect:
                self.state = SimpleButton.STATE_DISAMED
        elif self.state == SimpleButton.STATE_DISAMED:
            if eventPointInButtonRect:
                self.state = SimpleButton.STATE_ARMED
            elif eventObj.type == MOUSEBUTTONUP:
                self.state = SimpleButton.STATE_IDLE
        return False

    def draw(self):
        if self.state == SimpleButton.STATE_ARMED:
            self.window.blit(self.surfaceDown, self.loc)
        else:
            self.window.blit(self.surfaceUp, self.loc)
class SimpleText():
    def __init__(self,window,loc,value,textcolor):
        pygame.font.init()
        self.window = window
        self.loc = loc
        self.font = pygame.font.SysFont(None,30)
        self.textcolor = textcolor
        self.text = None
        self.setValue(value)
    def setValue(self, newText):
        if self.text == newText:
            return
        self.text=newText
        self.textSurface = self.font.render(self.text, True,self.textcolor)

    def draw(self):
        self.window.blit(self.textSurface,self.loc)