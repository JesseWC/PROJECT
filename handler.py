import sys
import os
import pygame
import threading
import time

# Append the path for relative imports
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from Classes.Ball import Ball
from Classes.Goal import Goal
from Classes.Avatar import Avatar

# Initialize Pygame
pygame.init()
pygame.font.init()

# Flags and initial states
running = False
intro_over = False

# Get the script directory and set the background image path
script_dir = os.path.dirname(os.path.abspath(__file__))
background_image_path = os.path.join(script_dir, 'Assets', 'Field.jpg')

# Score and timer
score = 0
seconds_timer = 0
size = (800, 500)

# Load and transform the background image
background = pygame.image.load(background_image_path)
background = pygame.transform.rotate(background, 90)  # Rotate the background image 90 degrees
background = pygame.transform.scale(background, size)

# Initialize fonts
font = pygame.font.SysFont('comicsansms', 50)
font2 = pygame.font.SysFont('calibri', 35)

# Render initial texts
displayintro = font.render("Click Anywhere To Continue", True, (255, 255, 255))

# Set up the screen
screen = pygame.display.set_mode(size)

# Initialize game objects
goal = Goal(650, 150, 200, 200, 270)
ball = Ball(375, 215, 50, 50, 0)
avatar = Avatar(300, 165, 100, 100, 0)

# Function to get user input
def get_user_input():
    global running, difficulty
    difficulty = input('Please enter either "E", "M", "D" (difficulty) for gameplay: ')
    print('Go play! You only have 60 seconds!')
    running = True

# Function to move sprites based on difficulty
def moveSprites():
    global direction
    speed = 1
    if difficulty == "E":
        speed = 1
    elif difficulty == "M":
        speed = 2
    elif difficulty == "D":
        speed = 3

    dy = speed if direction == 'down' else -speed
    avatar.rect.y += dy
    ball.rect.y += dy  # Move the ball along with the avatar

    # Change direction if avatar hits screen bounds
    if avatar.rect.top <= 0:
        direction = 'down'
    elif avatar.rect.bottom >= size[1]:
        direction = 'up'

# Function to reset ball position
def reset_ball():
    ball.move(avatar.rect.x + 75, avatar.rect.y + 50)

def animate_ball():
    global score
    while ball.rect.x < goal.rect.x:
        ball.move(ball.rect.x + 1, ball.rect.y)
        pygame.display.update()
        pygame.event.pump()  # Process Pygame events to keep the window responsive
        if ball.rect.x >= goal.rect.x:
            if ball.rect.colliderect(goal.rect):
                score += 1
                reset_ball()
            else:
                reset_ball()
            break

# Start the input thread
input_thread = threading.Thread(target=get_user_input)
input_thread.start()

# Main game loop
start_time = time.time()  # Initialize start time
direction = 'down'  # Initialize movement direction

# Initial render of texts
displayscore = font2.render(f"Score: {score}", True, (0, 0, 0))  # Black text for visibility
displaytimer = font2.render(f"Time Left: {60} seconds", True, (0, 0, 0))  # Initial timer text

clock = pygame.time.Clock()  # Create a clock object to control frame rate

while True:
    screen.fill((255, 255, 255))
    screen.blit(background, [0, 0])
    screen.blit(goal.image, goal.rect)
    screen.blit(ball.image, ball.rect)
    screen.blit(avatar.image, avatar.rect)

    if running:
        current_time = time.time()
        elapsed_time = current_time - start_time

        if elapsed_time >= 1:
            seconds_timer += 1
            start_time = current_time
        
        time_left = max(0, 60 - seconds_timer)
        displaytimer = font2.render(f"Time Left: {time_left} seconds", True, (0, 0, 0))  # Black text for visibility

        if seconds_timer >= 60:
            running = False

        moveSprites()  # Call moveSprites function based on difficulty

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:  # Check if right arrow key is pressed
                # Animate the ball towards the goal
                    target_x = goal.rect.x
                    animate_ball()

    screen.blit(displayscore, (0, 0))
    screen.blit(displaytimer, (0, 40))  # Display the timer

    pygame.display.update()
    clock.tick(60)  # Run the loop at 60 frames per second
