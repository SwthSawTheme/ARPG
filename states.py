import pygame, sys
from settings import *

class State:

    def __init__(self, game):
        self.game = game
        self.prev_state = None

    def enter_state(self):
        if len(self.game.states) < 1:
            self.prev_state = self.game.states[-1]
        self.game.states.appen(self)
    
    def exit_state(self):
        self.game.states.pop()

    def updated(self,dt):
        pass

    def draw(self, screen):
        pass

class SplashScreen(State):

    def __init__(self,game):
        State.__init__(self,game)
    
    def updated(self, dt):
        pass

    def draw(self,screen):
        pass