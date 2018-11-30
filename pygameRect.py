import pygame
from pygame.locals import *

"""
Isaac Sutor
PyGame Intro
"""


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super(Player, self).__init__()
        # create surface
        self.surf = pygame.Surface((75, 75))
        # color surface
        self.surf.fill((255, 255, 255))
        self.rect = self.surf.get_rect()


# initialize
pygame.init()

# create screen
screen = pygame.display.set_mode((800, 600))

player = Player()

# Variable to keep main loop running
running = True

# Main Loop
while running:
    # for loop through the event queue
    for event in pygame.event.get():
        # check KEYDOWN event;
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
            # check for QUIT
            elif event.type == pygame.QUIT:
                running = False

    # draw rect
    screen.blit(player.surf, (400, 300))
    pygame.display.flip()
