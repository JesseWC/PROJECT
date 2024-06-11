import sys
import os
import pygame
import time

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from Classes.Ball import Ball
from Classes.Goal import Goal
from Classes.Avatar import Avatar

pygame.init()
pygame.font.init()

running = True
score = 0
intro_over = False
script_dir = os.path.dirname(os.path.abspath(__file__))
background_image_path = os.path.join(script_dir, '..', 'Assets', 'Field.jpg')

background = pygame.image.load(background_image_path)
font = pygame.font.SysFont('comicsansms', 50)
font2 = pygame.font.SysFont('calibri', 35)
displayintro = font.render("Click Anywhere To Continue", True, (255, 255, 255))
displayscore = font2.render("Score: "+ str(score), True, (255, 255, 255))
size = (800, 500)
screen = pygame.display.set_mode(size)
a = Goal(40,40)

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
