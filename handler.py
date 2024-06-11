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
background_image_path = os.path.join(script_dir, '.', 'Assets', 'Field.jpg')

background = pygame.image.load(background_image_path)\

background = pygame.transform.rotate(background, 90)  # Rotate the background image 90 degrees
size = (800, 500)
background = pygame.transform.scale(background, size)
font = pygame.font.SysFont('comicsansms', 50)
font2 = pygame.font.SysFont('calibri', 35)
displayintro = font.render("Click Anywhere To Continue", True, (255, 255, 255))
displayscore = font2.render("Score: "+ str(score), True, (255, 255, 255))

screen = pygame.display.set_mode(size)
a = Goal(650, 150, 200, 200, 270)
b = Ball(500, 215, 50, 50, 0)  # Ensure to initialize with appropriate arguments if needed
c = Avatar(400, 165, 100, 100, 0)

while running:
    screen.fill((255, 255, 255))
    screen.blit(background, [0,0])
    screen.blit(a.image, a.rect)
    screen.blit(b.image, b.rect)
    screen.blit(c.image, c.rect)
    


    

    for event in pygame.event.get():  
        pygame.display.update()
        if event.type == pygame.QUIT:  
            running = False
        if event.type == pygame.KEYDOWN:
            intro_over=True
        if intro_over==True:
            screen.blit(displayscore, (0, 0))

    pygame.display.update()