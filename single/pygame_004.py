import pygame
import sys

pygame.init()
#指定窗口的宽和高
size = width,height = 1200,900
#指定移动速度，左上角为0，0
speed = [-4,2]
bg = (255,255,255)
#创建一个size规定大小的窗口
screen = pygame.display.set_mode(size)
#指定窗口标题
pygame.display.set_caption("The First pygame window!")

turtle =pygame.image.load("/Users/gangch/Documents/material/turtle.png")
#获得图像的位置信息
font = pygame.font.Font(None,20)
line_height = font.get_linesize()
position = 0
screen.fill(bg)


l_head = turtle
r_head = pygame.transform.flip(turtle,True,False)
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        screen.blit(font.render(str(event),True,(0,255,0)),(0,position))
        position += line_height

        if position > height:
            position = 0
            screen.fill(bg)

    #刷新界面
    pygame.display.flip()
