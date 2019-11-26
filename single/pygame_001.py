import os
import pygame

def main():
    screen =pygame.display.set_mode((0,0),flags=pygame.FULLSCREEN)
    #background = pygame.image.load("/Users/gangch/Documents/material/turtle.png")
    background = pygame.image.load("/Users/gangch/Downloads/CV0002721.jpg")
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        screen.blit(background,(0,0))
        pygame.display.update()


if __name__ == '__main__':
    main()