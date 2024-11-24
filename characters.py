import pygame
from settings import *

class NPC(pygame.sprite.Sprite):

    def __init__(self,game, scene, group, pos, name):
        super().__init__(group)

        self.game = game
        self.scene = scene
        self.name = name
        self.image = pygame.Surface((TILESIZE,TILESIZE*1.5))
        self.image.fill(COLORS["green"])
        self.rect = self.image.get_frect(topleft = pos)
        self.speed = 60
        self.force = 2000
        self.acc = vec()
        self.vel = vec()
        self.fric = -15
    
    def physics(self,dt):
        pass

    def update(self, dt):
        pass


class Player(NPC):
    def __init__(self, game, scene, group, pos, name):
        super().__init__(game, scene, group, pos, name)