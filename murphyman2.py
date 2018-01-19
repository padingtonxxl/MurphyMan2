import pygame
from lib.murphyMan2Game import MurphyMan2Game


pygame.init()
game = MurphyMan2Game("Murphy")

while 1:
    game.tick()

    for event in pygame.event.get():
        game.handleEvent(event)

    game.display()