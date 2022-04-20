import pygame
import os

# Allows the program to be run in the background, reading inputs even when not focused
os.environ["SDL_JOYSTICK_ALLOW_BACKGROUND_EVENTS"] = "1"


# Define some colors.
BLACK = pygame.Color('black')
WHITE = pygame.Color('#f5f5f5') # Not exactly white but sticks out nicer
BROWN = pygame.Color('#8b4513')
RED = pygame.Color('red')
GREY = pygame.Color('#3A3B3C')


# Class for printing things to screen
class TextPrint(object):
    def __init__(self):
        self.reset()
        self.font = pygame.font.Font(None, 20)

    def tprint(self, screen, textString):
        textBitmap = self.font.render(textString, True, BLACK)
        screen.blit(textBitmap, (self.x, self.y))
        self.y += self.line_height

    def reset(self):
        self.x = 10
        self.y = 10
        self.line_height = 15

    # def indent(self):
    #     self.x += 10

    # def unindent(self):
    #     self.x -= 10


pygame.init()

reso = (550, 300)

# Set the width and height of the screen (width, height).
screen = pygame.display.set_mode(reso)

screenWidth = screen.get_width()
screenHeight = screen.get_height()


pygame.display.set_caption("Input Viewer (Press Tab to switch controllers)")

# Loop until the user clicks the close button.
done = False

# Used to manage how fast the screen updates.
clock = pygame.time.Clock()

# Initialize the joysticks.
pygame.joystick.init()

# Get ready to print.
textPrint = TextPrint()

# -------- Main Program Loop -----------
while not done:
    # Get count of joysticks.
    joystick_count = pygame.joystick.get_count()

    # EVENT PROCESSING STEP
    currentController = 0
    for event in pygame.event.get(): # User did something.
        if event.type == pygame.QUIT: # If user clicked close.
            done = True # Flag that we are done so we exit this loop.
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_TAB:
                currentController += 1
                if currentController >= joystick_count:
                    currentController -= joystick_count

    # DRAWING STEP
    screen.fill(BROWN)
    textPrint.reset()

    if joystick_count > 0:

        joystick = pygame.joystick.Joystick(currentController)
        joystick_name = joystick.get_name()
        textPrint.tprint(screen, "Current Joystick: {}".format(joystick_name))

        # Creating the blanks underneath
        pygame.draw.circle(screen, BLACK, [120, 145], 42) #stick
        pygame.draw.circle(screen, BLACK, [290, 105], 31) #1p
        pygame.draw.circle(screen, BLACK, [353, 79],  31) #2p
        pygame.draw.circle(screen, BLACK, [419, 90],  31) #3p
        pygame.draw.circle(screen, BLACK, [483, 118], 31) #4p
        pygame.draw.circle(screen, BLACK, [280, 177], 31) #1k
        pygame.draw.circle(screen, BLACK, [344, 151], 31) #2k
        pygame.draw.circle(screen, BLACK, [411, 162], 31) #3k
        pygame.draw.circle(screen, BLACK, [475, 190], 31) #4k


        dpad = joystick.get_hat(0) #dpad[0] is left right, dpad[1] is up down
        if dpad[0] == 1:
            stickX = 150
        elif dpad[0] == -1:
            stickX = 90
        else:
            stickX = 120
        
        if dpad[1] == -1:
            stickY = 175
        elif dpad[1] == 1:
            stickY = 115
        else:
            stickY = 145
        pygame.draw.circle(screen, RED, [stickX, stickY], 40)


        # Handles all of the buttons, black circles go white when input is received
        if joystick.get_button(2): #1p, X
            pygame.draw.circle(screen, WHITE, [290, 105], 28)
        else:
            pygame.draw.circle(screen, GREY, [290, 105], 28)

        if joystick.get_button(3): #2p, Y
            pygame.draw.circle(screen, WHITE, [353, 79], 28)
        else:
            pygame.draw.circle(screen, GREY, [353, 79], 28)

        if joystick.get_button(5): #3p, RB
            pygame.draw.circle(screen, WHITE, [419, 90], 28)
        else:
            pygame.draw.circle(screen, GREY, [419, 90], 28)

        if joystick.get_button(4): #4p, LB
            pygame.draw.circle(screen, WHITE, [483, 118], 28)
        else:
            pygame.draw.circle(screen, GREY, [483, 118], 28)

        if joystick.get_button(0): #1k, A
            pygame.draw.circle(screen, WHITE, [280, 177], 28)
        else:
            pygame.draw.circle(screen, GREY, [280, 177], 28)

        if joystick.get_button(1): #2k, B
            pygame.draw.circle(screen, WHITE, [344, 151], 28)
        else:
            pygame.draw.circle(screen, GREY, [344, 151], 28)
            
        if joystick.get_axis(5) > 0: #3k, RT
            pygame.draw.circle(screen, WHITE, [411, 162], 28)
        else:
            pygame.draw.circle(screen, GREY, [411, 162], 28)

        if joystick.get_axis(4) > 0: #4k, LT
            pygame.draw.circle(screen, WHITE, [475, 190], 28)
        else:
            pygame.draw.circle(screen, GREY, [475, 190], 28)


    #
    # ALL CODE TO DRAW SHOULD GO ABOVE THIS COMMENT
    #

    # Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

    # Limit to 20 frames per second.
    clock.tick(20)

# Close the window and quit.
# If you forget this line, the program will 'hang'
# on exit if running from IDLE.
pygame.quit()