import os
import pygame

class Avatar:
    def __init__(self, x, y):
        script_dir = os.path.dirname(os.path.abspath(__file__))
        image_path = os.path.join(script_dir, '..', 'Assets', 'Avatar.png')
        self.x = x
        self.y = y
        self.image = pygame.image.load(image_path)
        self.image_size = self.image.get_size()
        self.rect = pygame.Rect(self.x, self.y, self.image_size[0], self.image_size[1])


    def move(self, new_x, new_y):
        self.x = new_x
        self.y = new_y
        self.rect = pygame.Rect(self.x, self.y, self.image_size[0], self.image_size[1])