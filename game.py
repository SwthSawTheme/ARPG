import pygame, sys
from settings import *

class Game:

    def __init__(self):
        pygame.init()
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode(WIDTH,HEIGHT)
        self.font = pygame.font.Font(FONT,TILESIZE)
        self.running = True

        self.states = []
        self.splash_screen = SplashScreen(self)
        self.states.append(self.splash_screen)
    
    def get_inputs(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    INPUTS["escape"] = True
                    self.running = False
                elif event.key == pygame.K_SPACE:
                    INPUTS["space"] = True
                elif event.key in (pygame.K_LEFT, pygame.K_a):
                    INPUTS["left"] = True
                elif event.key in (pygame.K_RIGHT, pygame.K_d):
                    INPUTS["right"] = True
                elif event.key in (pygame.K_UP, pygame.K_w):
                    INPUTS["up"] = True
                elif event.key in (pygame.K_DOWN, pygame.K_s):
                    INPUTS["down"] = True

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_SPACE:
                    INPUTS["space"] = False
                elif event.key in (pygame.K_LEFT, pygame.K_a):
                    INPUTS["left"] = False
                elif event.key in (pygame.K_RIGHT, pygame.K_d):
                    INPUTS["right"] = False
                elif event.key in (pygame.K_UP, pygame.K_w):
                    INPUTS["up"] = False
                elif event.key in (pygame.K_DOWN, pygame.K_s):
                    INPUTS["down"] = False