import sys
import os
# Prevent PyGame showing a welcome message
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"  # noqa due to PyGame
import pygame
from board import *
from peg_colors import *
from pygame.locals import *
from game import *


# define the main main testing function
def test():
    test_peg_colors()
    test_board()
    test_game()


# define a main function
def main():

    # initialize the pygame module
    pygame.init()
    pygame.display.set_caption("kiri")

    # create a surface on screen that has the size of 240 x 180
    screen = pygame.display.set_mode(960, 720)

    # draws a rectangle to become the playing field
    DISPLAY = pygame.display.set_mode((500, 400), 0, 32)

    PERU = (205, 133, 63)
    SIENNA = (160, 82, 45)

    DISPLAY.fill(SIENNA)

    pygame.draw.rect(DISPLAY, PERU, (200, 200, 200, 50))

    # define a variable to control the main loop
    running = True

    # create a font
    font = pygame.font.SysFont(None, 64)

    # main loop
    while running:
        # event handling, gets all event from the event queue
        for event in pygame.event.get():
            # only do something if the event is of type QUIT
            if event.type == pygame.QUIT:
                # change the value to False, to exit the main loop
                running = False

        # Draw orange background rectangle
        pygame.draw.rect(screen, (255, 128, 0), (120, 120, 320, 40))
        # Draw text, from
        # https://pygame.readthedocs.io/en/latest/4_text/text.html#work-with-text
        img = font.render("MASTERMIND", True, (0, 0, 0))
        screen.blit(img, (120, 120))

        # Draw a red round peg on a random location
        pygame.draw.circle(screen, (255, 0, 0), (220, 220), 40)

        # Draw a green ellipse on a random location
        pygame.draw.ellipse(screen, (0, 255, 0), (220, 220, 40, 40))

        pygame.display.update()


# run the main function only if this module is executed as the main script
# (if you import this as a module then nothing is executed)
if __name__ == "__main__":
    if (len(sys.argv) == 2 and sys.argv[1] == "--test"):
        test()
        exit(0)

    # call the main function
    main()
