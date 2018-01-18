import sys, pygame
import time
from pygame import Rect, draw
from datetime import datetime, date
from pygame.locals import *

def get_difference(a, b):
    if a > b:
        return (a - b) * -1
    else:
        return b - a


pygame.init()

size = width, height = 640, 480
speed = [0, 0]
black = 0, 0, 0

screen = pygame.display.set_mode(size)

ball = pygame.image.load("res/ball.png")
ballrect = ball.get_rect()
paddle1 = pygame.image.load("res/paddle.png")
paddle1rect = Rect(5,height/2-50,10,100)
paddle2 = pygame.image.load("res/paddle.png")
paddle2rect = Rect(width-15,height/2-50,10,100)

start_time = datetime.now()
last_tick = start_time
myfont = pygame.font.SysFont('Comic Sans MS', 11)
fps = 0
last_second = start_time
text_fps = myfont.render(str(fps), False, (255, 255, 255), (0,0,0))

while 1:
    current_tick = datetime.now()
    time_since_last_tick = current_tick - last_tick
    #Speed 100 fps
    while time_since_last_tick.microseconds < 10000:
        time.sleep(0.0002)
        current_tick = datetime.now()
        time_since_last_tick = current_tick - last_tick
    fps += 1
    time_since_last_fps_update = current_tick - last_second
    last_tick = current_tick
    #print("tick"+str(current_tick.time()))
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

    mouse_position = pygame.mouse.get_pos()
    center = [(((ballrect.right - ballrect.left) / 2) + ballrect.left), (((ballrect.bottom - ballrect.top ) / 2) + ballrect.top)]
    distance = [0,0]

    distance[0] = get_difference(center[0], mouse_position[0])
    distance[1] = get_difference(center[1], mouse_position[1])
    if distance[0] == 1 or distance[0] == -1:
        speed[0] = distance[0]
    else:
        speed[0] = distance[0] / 10
    if distance[1] == 1 or distance[1] == -1:
        speed[1] = distance[1]
    else:
        speed[1] = distance[1] / 10

    if 0 < speed[0] < 1:
            speed[0] = 1
    elif -1 < speed[0] < 0:
            speed[0] = -1
    if 0 < speed[1] < 1:
            speed[1] = 1
    elif -1 < speed[1] < 0:
            speed[1] = -1
    if time_since_last_fps_update.seconds >= 1:
        text_fps = myfont.render(str(fps) + ' fps', False, (255, 255, 255), (0,0,0))
        fps = 0
        last_second = current_tick

    textsurface = myfont.render(str(speed), False, (255, 255, 255), (0,0,0))
    ballrect = ballrect.move(speed)
#    if ballrect.left < 0 or ballrect.right > width:
#        speed[0] = -speed[0]
#    if ballrect.top < 0 or ballrect.bottom > height:
#        speed[1] = -speed[1]

    screen.fill(black)
    screen.blit(ball, ballrect)
    screen.blit(paddle1, paddle1rect)
    screen.blit(paddle2, paddle2rect)
    screen.blit(textsurface, (0, 0))
    screen.blit(text_fps, (0, 12))
    pygame.display.flip()


