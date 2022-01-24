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
    def __init__(self, save):
        # test for save file existance
        if os.path.exists("output/save"):
            with open("output/save", "r") as f:
                self.save = json.load(f)
        else:
            with open("output/save", 'w') as f:
                self.save = json.load(f)
        
        # window initialization
        self.screen = pygame.display.set_mode((800, 600))
        pygame.display.set_caption(title)
        self.clock = pygame.time.Clock()
        self.fps = 60
        self.running = True
        self.font = pygame.font.SysFont("monospace", 20)
