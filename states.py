import pygame, sys
from settings import *
from game import *
from characters import *

class State:

    def __init__(self, game):
        self.game = game
        self.prev_state = None

    def enter_state(self):
        if len(self.game.states) < 1:
            self.prev_state = self.game.states[-1]
        self.game.states.append(self)
    
    def exit_state(self):
        self.game.states.pop()

    def updated(self,dt):
        pass

    def draw(self, screen):
        pass

class SplashScreen(State):

    def __init__(self,game):
        State.__init__(self, game)
    
    def updated(self, dt):
        if INPUTS["space"]:
            Scene(self.game).enter_state()
            self.game.reset_inputs()
            print(vec(1,0))

    def draw(self,screen):
        screen.fill(COLORS["blue"])
        self.game.render_text("Splash screen, press space", COLORS["white"], self.game.font, (WIDTH/2, HEIGHT/2))
        

class Scene(State):

    def __init__(self,game):
        State.__init__(self, game)

        self.update_sprites = pygame.sprite.Group()
        self.drawn_sprites = pygame.sprite.Group()

        self.player = Player(self.game, self, [self.update_sprites, self.drawn_sprites], (WIDTH/2, HEIGHT/2), "Player")
    
    def updated(self, dt):
        self.update_sprites.update(dt)

    def draw(self,screen):
        screen.fill(COLORS["red"])
        self.drawn_sprites.draw(screen)
        