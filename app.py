import pygame
from pygame.locals import *
import sys
import os
import time
import random
import json

title = "THE IDEA"
pygame.init()

class Game:
    def __init__(self):
        
        self.save = open("save", "w")

        # window initialization
        self.screen = pygame.display.set_mode((800, 600))
        pygame.display.set_caption(title)
        self.clock = pygame.time.Clock()
        self.fps = 60
        self.running = True
        self.font = pygame.font.SysFont("fonts/journal.ttf", 20)
        self.font_title = pygame.font.Font("fonts/journal.ttf", 40)
        self.font_title_small = pygame.font.Font("fonts/journal.ttf", 30)

game = Game()
class Player(game.save):
    def __init__(self, save):
        super().__init__(Game.save)

player = Player(game.save)


while game.running:
    pygame.display.flip()