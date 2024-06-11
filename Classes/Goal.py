import os
import pygame

class Goal:
    def __init__(self, x, y, width=None, height=None, angle=0):
        script_dir = os.path.dirname(os.path.abspath(__file__))
        image_path = os.path.join(script_dir, '..', 'Assets', 'Goal.png')
        self.x = x
        self.y = y
        self.image = pygame.image.load(image_path)
        
        # If width and height are provided, scale the image
        if width and height:
            self.image = pygame.transform.scale(self.image, (width, height))
        
        # Rotate the image if an angle is provided
        if angle != 0:
            self.image = pygame.transform.rotate(self.image, angle)
        
        self.image_size = self.image.get_size()
        self.rect = self.image.get_rect(topleft=(self.x, self.y))

# class Goal:
#     def __init__(self, x, y):
#         script_dir = os.path.dirname(os.path.abspath(__file__))
#         image_path = os.path.join(script_dir, '..', 'Assets', 'Goal.png')
#         self.x = x
#         self.y = y
#         self.image = pygame.image.load(image_path)
#         self.image_size = self.image.get_size()
#         self.rect = pygame.Rect(self.x, self.y, self.image_size[0], self.image_size[1])


    def move(self, new_x, new_y):
        self.x = new_x
        self.y = new_y
        self.rect = pygame.Rect(self.x, self.y, self.image_size[0], self.image_size[1])