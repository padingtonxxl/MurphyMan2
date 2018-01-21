import pygame
from lib.Config import Config
from lib.murphyMan2Game import MurphyMan2Game


pygame.init()
config = Config("murphyman2.ini")
game = MurphyMan2Game("Murphy", config)

while 1:
    game.tick()

    for event in pygame.event.get():
        game.handleEvent(event)

    game.update()

    game.display()