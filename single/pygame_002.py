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
position = turtle.get_rect()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    position = position.move(speed)

    if position.left < 0 or position.right > width:
        turtle = pygame.transform.flip(turtle,True,False)#true表示水平翻转，False表示不垂直翻转
        speed[0] = -speed[0]

    if position.top < 0 or position.bottom > height:
        speed[1] = -speed[1]
    #填充背景
    screen.fill(bg)
    #刷新图像
    screen.blit(turtle,position)
    #刷新界面
    pygame.display.flip()
#延迟10毫秒
    pygame.time.delay(10)