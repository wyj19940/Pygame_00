import pygame
import sys
import time


pygame.init()
size = width,height = 800,600
screen = pygame.display.set_mode(size)
color = 255,255,255
ball = pygame.image.load('ball.png')
ball = pygame.transform.scale(ball, (50, 50))
ballrect = ball.get_rect()

rect = pygame.image.load('rect.png')
rect = pygame.transform.scale(rect, (200, 30))
rectarea = rect.get_rect()
rectarea.move_ip(400-100,600-35)
speed =[5,5]
state_time = pygame.time.Clock()
x,y=400,600-30
move_x=move_y=0
while True:  # 死循环确保窗口一直显示
    for event in pygame.event.get():  # 遍历所有事件
        if event.type == pygame.QUIT:  # 如果单击关闭窗口，则退出
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                move_x = -5
            elif event.key == pygame.K_RIGHT:
                move_x = 5
            elif event.key == pygame.K_UP:
                move_y = -5
            elif event.key == pygame.K_DOWN:
                move_y = 5
        elif event.type == pygame.KEYUP:
            move_x = 0
            move_y = 0
    x += move_x
    y += move_y
    state_time.tick(50)
    ballrect = ballrect.move(speed)
    screen.fill(color)
    screen.blit(ball,ballrect)
    screen.blit(rect,(x,y))
    pygame.display.flip()

    if ballrect.left<0 or ballrect.right>width:
        speed[0] = -speed[0]
    if ballrect.top<0:
        speed[1] = -speed[1]
    if ballrect.bottom==600-30 and ballrect.left+50>=x and ballrect.left<=x+200 :
        speed[1] = -speed[1]
    if ballrect.bottom>600+50:
        break
pygame.quit()