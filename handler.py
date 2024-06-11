import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import pygame
import time

from Classes.Ball import Ball
from Classes.Goal import Goal
from Classes.Avatar import Avatar

score = 0
# set up pygame modules
pygame.init()
pygame.font.init()
font2 = pygame.font.SysFont('calibri', 35)
font = pygame.font.SysFont('comicsansms', 50)
displayintro = font.render("Click Anywhere To Continue", True, (255, 255, 255))
displayscore = font2.render("Score: "+ str(score), True, (255, 255, 255))
intro_over = False
# set up variables for the display
size = (800, 500)
screen = pygame.display.set_mode(size)

a=Goal(40,40)

running = True
while running:
    screen.fill((255, 0, 255))
    screen.blit(displayintro, (75, 200))








   
    for event in pygame.event.get():  
        pygame.display.update()
        if event.type == pygame.QUIT:  
            running = False
        if event.type == pygame.KEYDOWN:
            intro_over=True
        if intro_over==True:
            screen.blit(displayscore, (0, 0))


screen.blit(a.image, a.rect)
#screen.blit(b.image, b.rect)
#screen.blit(c.image, c.rect)
