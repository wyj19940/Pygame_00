import pygame
import sys
from pygame.locals import *

pygame.init()
size = width, height = 1000, 665
speed = [-15, 10]
screen = pygame.display.set_mode(size)
pygame.display.set_caption("游戏设计")
turtle = pygame.image.load("snake.png")
background = pygame.image.load("background.jpg")
position = turtle.get_rect()


    
l_head = turtle
r_head = pygame.transform.flip(turtle, True, False)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == KEYDOWN:
            if event.key == K_LEFT:
                turtle = l_head
                speed = [-10, 0]
            if event.key == K_RIGHT:
                turtle = r_head
                speed = [10, 0]
            if event.key == K_UP:
                speed = [0, -10]
            if event.key == K_DOWN:
                speed = [0, 10]


    position = position.move(speed)
    if position.left < 0 or position.right > width: 
        turtle = pygame.transform.flip(turtle, True, False)
        speed[0] = -speed[0]
    if position.top < 0 or position.bottom > height:
        speed[1] = -speed[1]
    screen.blit(background, (0, 0))
    screen.blit(turtle, position)
    pygame.display.flip()   
    pygame.time.delay(20) 