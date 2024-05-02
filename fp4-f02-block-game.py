# - FP4-F02 Pygame - #
# - Xzavier Moosomin - #
# - 05/02/2024 - #

# - Imports - #

import random

import pygame

# - Classes - #

class Block:
    def __init__(self, color, width, height):
        super().__init__() # man im smart
        self.image = pygame.Surface([width, height])
        self.image.fill(color) # changes the blocks color to whatever color was passed as. for ex. black
        self.rect = self.image.get_rect() # creates the rectangle
        self.rect.x = screen_width // 2 # determines the rectangles dimentions, dividing the screen's by two
        self.rect.y = screen_height // 2

    def move(self, x, y):
        # allows the block to move around
        self.rect.x += x
        self.rect.y += y

        # this block of code makes sure that it doesn't go outside the window
        if self.rect.left < 0:
            self.rect.left = 0
            
        elif self.rect.right > screen_width:
            self.rect.right = screen_width
            
        if self.rect.top < 0:
            self.rect.top = 0
            
        elif self.rect.bottom > screen_height:
            self.rect.bottom = screen_height

# - Variables - #

running = True
colval1 = random.randint(0, 255) # random color values 
colval2 = random.randint(0, 255) # add up
colval3 = random.randint(0, 255) # to make a random color

randcolor = (colval1, colval2, colval3) # then it saves as randcolor

# - Constants - #

white = (255, 255, 255)
screen_width = 800
screen_height = 600

block = Block(randcolor, 50, 50) # then passed as color argument

# - Pygame Initialization - #
pygame.init()

# - Game Settings -#

screen = pygame.display.set_mode((screen_width, screen_height)) # set screen dimension
pygame.display.set_caption("Funny Rainbow Block Hahaha") # set window name

clock = pygame.time.Clock() # moderates the frame rate

# - Main Code - #

while running:
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # checks every frame to see if a key was pressed
    keys = pygame.key.get_pressed()

    # Move the block based on arrow key input
    if keys[pygame.K_LEFT]:
        block.move(-5, 0) # 5 frames to the left
    
    if keys[pygame.K_RIGHT]:
        block.move(5, 0) # 5 frames to the right
    
    if keys[pygame.K_UP]:
        block.move(0, -5) # 5 frames up 
    
    if keys[pygame.K_DOWN]:
        block.move(0, 5) # 5 frames down

    # gives the window a white background
    screen.fill(white)

    # then it draws the block on top
    screen.blit(block.image, block.rect)

    # updates display for that frame
    pygame.display.flip()

    # caps the frame rate to 120 fps (optimal for gamers)
    clock.tick(120)

# player quits the game
pygame.quit()
