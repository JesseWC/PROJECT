import sys
import os
import pygame
import time

# Append the path for relative imports
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from Classes.Ball import Ball
from Classes.Goal import Goal
from Classes.Avatar import Avatar

# Initialize Pygame
pygame.init()
pygame.font.init()

# Constants
size = (800, 500)
background_image_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'Assets', 'Field.jpg')
font1 = pygame.font.SysFont('comicsansms', 30)
font2 = pygame.font.SysFont('calibri', 35)
font3 = pygame.font.SysFont("century", 20)
title_font = pygame.font.SysFont("pristina", 50)
# WHITE = (255, 255, 255)
# BLACK = (0, 0, 0)

# Global variables
running = False
ball_moving = False
score = 0
high_score = 0
seconds_timer = 0
direction = ''
difficulty = ""

# Load and transform the background image
background = pygame.image.load(background_image_path)
background = pygame.transform.rotate(background, 90)  # Rotate the background image 90 degrees
background = pygame.transform.scale(background, size)

# Screen setup
screen = pygame.display.set_mode(size)

# Game objects
goal = Goal(650, 150, 200, 200, 270)
ball = Ball(375, 215, 50, 50, 0)
avatar = Avatar(300, 165, 100, 100, 0)

# Render initial texts
displayintro = font1.render("Click E, M, or D to Select Difficulty", True, (255,255,255))
instructions = font3.render("Click E for Easy, Click M for Medium and D for Difficult", True, (255,255,255))
instructions2 = font3.render("Use the Right Arrow Key to Shoot the Ball!", True, (255, 255, 0))
gamename = title_font.render("SOCCERMAN", True, (255,0,255))
displayscore = font2.render(f"Score: {score}", True, (255,255,255))
displaytimer = font2.render(f"Time Left: {60} seconds", True, (255,255,255))

# Function to move sprites based on difficulty, higher difficulty= higher speed
def move_sprites():
    global direction
    if difficulty == "E":
        speed = 5
    elif difficulty == "M":
        speed = 6
    elif difficulty == "D":
        speed = 7
    else:
        speed = 5


    dy = speed if direction == 'down' else -speed
    avatar.rect.y += dy
    ball.rect.y += dy  # Move the ball along with the avatar

    # Change direction if avatar hits screen bounds
    if avatar.rect.top <= 0:
        direction = 'down'
    elif avatar.rect.bottom >= size[1]:
        direction = 'up'

    # Change direction if avatar hits screen bounds
    if avatar.rect.top <= 0:
        direction = 'down'
    elif avatar.rect.bottom >= size[1]:
        direction = 'up'

# Function to reset ball position
def reset_ball():
    global ball_moving
    ball_moving = False
    ball.move(avatar.rect.x + 75, avatar.rect.y + 50)

# Function to animate the ball towards the goal
def animate_ball():
    global score
    if ball.rect.x < goal.rect.x:
        ball.move(ball.rect.x + 6, ball.rect.y)
        if ball.rect.x >= goal.rect.x:
            if ball.rect.colliderect(goal.rect):
                score += 1
                reset_ball()
            else:
                reset_ball()

# Function to initialize the game
def initialize_game():
    global running, seconds_timer, start_time
    running = True
    seconds_timer = 0 #timer is set to 0
    start_time = time.time()

# Function to update timer
def update_timer():
    global seconds_timer, start_time
    current_time = time.time()
    if current_time - start_time >= 1:
        seconds_timer += 1
        start_time = current_time

# Function to display the introduction screen
def introduction_screen():
    global difficulty
    intro_running = True
    while intro_running:
        screen.fill((0,0,0))
        screen.blit(displayintro, (150, 200))
        screen.blit(instructions, (150, 250))
        screen.blit(instructions2, (150, 290))
        screen.blit(gamename, (225, 0))
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN: #picks up the user input, depending on what key the user input's, it corresponds to a difficulty and that value will be set to difficulty
                if event.key == pygame.K_e:
                    difficulty = 'E'
                    intro_running = False
                elif event.key == pygame.K_m:
                    difficulty = 'M'
                    intro_running = False
                elif event.key == pygame.K_d:
                    difficulty = 'D'
                    intro_running = False


#function to display the game_over screen, includes final score, retry or quiot
def game_over_screen():
    global score, running, seconds_timer
    
    running = False  # Stop the main game loop

    screen.fill((0, 0, 0))  # Fill the screen with black

    # Render game over text and score
    game_over_text = font1.render("Game Over!", True, (255, 0, 0))
    game_over_score = font2.render(f"Final Score: {score}", True, (255, 255, 255))
    retry_text = font1.render("Press R to Retry", True, (255, 255, 255)) #has option to quit or retry game
    quit_text = font1.render("Press Q to Quit", True, (255, 255, 255))

    screen.blit(game_over_text, (300, 200))
    screen.blit(game_over_score, (300, 250))
    screen.blit(retry_text, (300, 300))
    screen.blit(quit_text, (300, 350))

    pygame.display.update()

    # Wait for player input to retry or quit
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    # Restart the game
                    reset_game() #calls function to reset game
                    return
                elif event.key == pygame.K_q:
                    # Quit the game
                    pygame.quit()
                    sys.exit()

#resets the game after user presses "r" during game over screen, resets everything, new game 
def reset_game():
    global running, ball_moving, score, seconds_timer, start_time, direction, difficulty

    # Reset game state variables
    difficulty = ""
    introduction_screen()
    move_sprites()
    running = False
    ball_moving = False
    score = 0
    seconds_timer = 0
    start_time = time.time()
    direction = ''

    # Reset game object positions
    avatar.rect.x = 300
    avatar.rect.y = 165
    ball.rect.x = 375
    ball.rect.y = 215

    initialize_game() 
# Start the introduction screen
introduction_screen()

# Initialize the game
initialize_game()


clock = pygame.time.Clock()  # Create a clock object to control frame rate
# Main game loop
while True:
    # Initial render of score text
    displayscore = font2.render(f"Score: {score}", True, (0,0,0))

    screen.fill((0,0,0))
    screen.blit(background, [0, 0])
    screen.blit(goal.image, goal.rect)
    screen.blit(ball.image, ball.rect)
    screen.blit(avatar.image, avatar.rect)
    screen.blit(displayscore, (0, 0))
    screen.blit(displaytimer, (0, 40))

    if running:
        update_timer()
        time_left = max(0, 60 - seconds_timer)
        displaytimer = font2.render(f"Time Left: {time_left} seconds", True, (0,0,0)) #displays the time

        if seconds_timer >= 60:
            running = False

        move_sprites()  # Call move_sprites function based on difficulty

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:  # Check if right arrow key is pressed
                    ball_moving = True

        if ball_moving:
            animate_ball() #animates the ball toward the goal
        
        if seconds_timer >= 60:
            game_over_screen() #if 60 seconds have elspased, the game over screen is presented, game ended

    pygame.display.update()
    clock.tick(60)
