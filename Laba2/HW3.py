import pygame
from pygame.draw import *

pygame.init()

FPS = 30
screen = pygame.display.set_mode((500, 500))

rect(screen, (200, 200, 200), (0, 0, 500, 500))  #  creating background

circle(screen, (200, 200, 0), (250, 250), 200)  #  body

circle(screen, (200, 0, 0), (160, 180), 30)
circle(screen, (200, 0, 0), (340, 180), 50)  #  right eye

circle(screen, (0, 0, 0), (160, 180), 15)
circle(screen, (0, 0, 0), (340, 180), 15)  #  left eye

rect(screen, (0, 0, 0), (130, 325, 250, 40))  #  mouth

surf = pygame.Surface((500, 500)) 
pygame.Surface.fill(surf,(255, 255, 255))
pygame.Surface.set_colorkey(surf,( 255, 255, 255))
rect(surf, ( 0, 0, 0), (50, 70, 100, 20))
surf1 = pygame.transform.rotate(surf, -45)
screen.blit(surf1, (0, 0))  #  right eyebrow


screen.blit(surf1, (0, 0))
surf = pygame.Surface((500, 500))
pygame.Surface.fill(surf,(255, 255, 255))
pygame.Surface.set_colorkey(surf,( 255, 255, 255))
rect(surf, ( 0, 0, 0), (250, 10, 100, 20))
surf1 = pygame.transform.rotate(surf, 45)
screen.blit(surf1, (-90, 0))  #  left eyebrow

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
pygame.quit()
