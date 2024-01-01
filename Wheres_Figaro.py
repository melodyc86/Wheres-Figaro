import pygame
import random

# Initialize Pygame
pygame.init()

# Screen dimensions
screen_width = 800
screen_height = 600

# Create the screen
screen = pygame.display.set_mode((screen_width, screen_height))

# Background images
background_images = ['background1.jpg', 'background2.jpg', 'background3.jpg']
backgrounds = [pygame.image.load(img).convert() for img in background_images]

# Current background index
current_background = 0

# Randomly place Figaro
Figaro = pygame.image.load('Figaro.png').convert_alpha()

# Function to place Figaro randomly
def place_Figaro():
    Figaro_rect = Figaro.get_rect()
    Figaro_rect.topleft = (random.randint(0, screen_width - Figaro_rect.width), 
                          random.randint(0, screen_height - Figaro_rect.height))
    return Figaro_rect

Figaro_rect = place_Figaro()

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # Check if Figaro is found
            if Figaro_rect.collidepoint(event.pos):
                print("You found Figaro!")
                # Switch to the next background
                current_background = (current_background + 1) % len(backgrounds)
                Figaro_rect = place_Figaro()

    # Draw everything
    screen.blit(backgrounds[current_background], (0, 0))
    screen.blit(Figaro, Figaro_rect)
    pygame.display.flip()

pygame.quit()
