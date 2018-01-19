import sys
import pygame
import time
from datetime import datetime
from pygame.locals import *


def get_difference(a, b):
    if a > b:
        return (a - b) * -1
    else:
        return b - a

pygame.init()

size = width, height = 640, 480
speed = [0, 0]
black = 0, 153, 0
points = [0, 0]

screen = pygame.display.set_mode(size)

ball = pygame.image.load("res/ball.png")
ballRect = Rect(width / 2 - 10, height / 2 - 10, 20, 20)
paddle1 = pygame.image.load("res/paddle.png")
paddle1rect = Rect(5, height/2-50, 10, 100)
paddle2 = pygame.image.load("res/paddle.png")
paddle2rect = Rect(width-15, height/2-50, 10, 100)

paddle1Speed = 0
paddle2Speed = 0

start_time = datetime.now()
last_tick = start_time
defaultFont = pygame.font.SysFont('Arial', 11)
pointsFont = pygame.font.SysFont('Arial Black', 24)
fps = 0
last_second = start_time
text_fps = defaultFont.render(str(fps), False, (255, 255, 255), black)
points_display = pointsFont.render("0 : 0", False, (255, 255, 255), black)
message = None


while 1:
    current_tick = datetime.now()
    time_since_last_tick = current_tick - last_tick
    while time_since_last_tick.microseconds < 10000:
        time.sleep(0.0002)
        current_tick = datetime.now()
        time_since_last_tick = current_tick - last_tick
    fps += 1
    time_since_last_fps_update = current_tick - last_second
    last_tick = current_tick
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        keys = pygame.key.get_pressed()

        if keys[K_UP]:
            paddle2Speed = -5
        elif keys[K_DOWN]:
            paddle2Speed = 5
        else:
            paddle2Speed = 0

        if keys[K_w]:
            paddle1Speed = -5
        elif keys[K_s]:
            paddle1Speed = 5
        else:
            paddle1Speed = 0

        if event.type == pygame.KEYDOWN:
            if keys[K_SPACE]:
                ballRect = Rect(width / 2 - 10, height / 2 - 10, 20, 20)
                speed = (6, 0)
                message = None

    paddle1rect.top += paddle1Speed
    paddle1rect.top -= paddle1Speed

    if paddle1rect.top <= 0 and paddle1Speed < 0:
        paddle1Speed = 0
    elif paddle1rect.bottom >= height and paddle1Speed > 0:
        paddle1Speed = 0

    if paddle2rect.top <= 0 and paddle2Speed < 0:
        paddle2Speed = 0
    elif paddle2rect.bottom >= height and paddle2Speed > 0:
        paddle2Speed = 0

    if time_since_last_fps_update.seconds >= 1:
        text_fps = defaultFont.render(str(fps) + ' fps', True, (255, 255, 255), black)
        fps = 0
        last_second = current_tick

    textsurface = defaultFont.render(str(speed), True, (255, 255, 255), black)

    if ballRect.top < 0 or ballRect.bottom > height:
        speed = [speed[0], speed[1]*-1]

    ballRect = ballRect.move(speed[0], speed[1])
    paddle1rect = paddle1rect.move(0, paddle1Speed)
    paddle2rect = paddle2rect.move(0, paddle2Speed)
    paddle1UpperRect = Rect(paddle1rect.left, paddle1rect.top, paddle1rect.width, paddle1rect.height / 2)
    paddle1LowerRect = Rect(paddle1rect.left, paddle1rect.top + paddle1rect.height / 2, paddle1rect.width,
                            paddle1rect.height / 2)
    paddle2UpperRect = Rect(paddle2rect.left, paddle2rect.top, paddle2rect.width, paddle2rect.height / 2)
    paddle2LowerRect = Rect(paddle2rect.left, paddle2rect.top + paddle2rect.height / 2, paddle2rect.width,
                            paddle2rect.height / 2)

    if ballRect.colliderect(paddle1rect) or ballRect.colliderect(paddle2rect):
        speed = [speed[0] * -1, speed[1]]
        if ballRect.colliderect(paddle1UpperRect) and speed[1] > -3:
            speed = [speed[0], speed[1]-1]
        elif ballRect.colliderect(paddle1LowerRect) and speed[1] < 3:
            speed = [speed[0], speed[1]+1]
        elif ballRect.colliderect(paddle2UpperRect) and speed[1] > -3:
            speed = [speed[0], speed[1]-1]
        elif ballRect.colliderect(paddle2LowerRect) and speed[1] < 3:
            speed = [speed[0], speed[1]+1]

    if ballRect.left < 0:
        points[1] += 1
        points_display = pointsFont.render(str(points[0])+" : "+str(points[1]), True, (255, 255, 255), black)
        ballRect = Rect(width / 2 - 10, height / 2 - 10, 20, 20)
        speed = (0, 0)
        paddle1rect = Rect(5, height / 2 - 50, 10, 100)
        paddle2rect = Rect(width - 15, height / 2 - 50, 10, 100)
    elif ballRect.right > width:
        points[0] += 1
        points_display = pointsFont.render(str(points[0]) + " : " + str(points[1]), True, (255, 255, 255), black)
        ballRect = Rect(width / 2 - 10, height / 2 - 10, 20, 20)
        speed = (0, 0)
        paddle1rect = Rect(5, height / 2 - 50, 10, 100)
        paddle2rect = Rect(width - 15, height / 2 - 50, 10, 100)

    if points[0] >= 5:
        message = pointsFont.render("Player one wins!", False, (255, 255, 255), black)
        points = [0, 0]
        points_display = pointsFont.render(str(points[0]) + " : " + str(points[1]), True, (255, 255, 255), black)
    elif points[1] >= 5:
        message = pointsFont.render("Player two wins!", False, (255, 255, 255), (0, 0, 0))
        points = [0, 0]
        points_display = pointsFont.render(str(points[0]) + " : " + str(points[1]), True, (255, 255, 255), black)

    screen.fill(black)
    screen.blit(ball, ballRect)
    screen.blit(paddle1, paddle1rect)
    screen.blit(paddle2, paddle2rect)
    screen.blit(textsurface, (0, 0))
    screen.blit(text_fps, (0, 12))
    screen.blit(points_display, (width/2-30, 0))
    if message!= None:
        screen.blit(message, (width / 2 - 100, height-50))
    pygame.display.flip()
