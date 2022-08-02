import pygame
import sys
from pygame.locals import *


# ------------------------------- Constants ------------------------------------

BACKGROUND_COLOR = "#1e1e1e"
VELOCITY = 10

# ------------------------------- Starting lines ------------------------------------

pygame.init()
clock = pygame.time.Clock()

screen = pygame.display.set_mode([1000, 600])
pygame.display.set_caption("The Gra 2")
screen.fill(BACKGROUND_COLOR)

# ------------------------------- Graphics ------------------------------------

logo_img = pygame.image.load("Graphics/logo.png")
logo_img = pygame.transform.scale(logo_img, (720, 390))

map_img = pygame.image.load("Graphics/map.png")
map_img = pygame.transform.scale(map_img, (720, 390))

position_img = pygame.image.load("Graphics/map_position.png")
position_img = pygame.transform.scale(position_img, (30, 30))

# ------------------------------- Menu ------------------------------------

screen.blit(logo_img, (150, 0))

font = pygame.font.SysFont("cambriacambriamath", 32)

start_game = font.render("Wciśnij dowolny klawisz aby rozpocząć grę", True, (255, 255, 255))
start_game.set_alpha(180)
screen.blit(start_game, (280, 400))

pygame.display.flip()

# ------------------------------- Main Loop ------------------------------------

sequence = 0

x_pos = 230
y_pos = 300
move_allow = 0

how_long = True
while how_long:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == KEYDOWN or event.type == MOUSEBUTTONDOWN:
            screen.fill(BACKGROUND_COLOR)
            sequence += 1

    keys = pygame.key.get_pressed()

    if sequence == 1:
        screen.blit(map_img, (150, 120))
        keys = pygame.key.get_pressed()
        screen.blit(position_img, (x_pos, y_pos))

    if (keys[pygame.K_RIGHT] or keys[pygame.K_d]) and move_allow == 1 and x_pos < 720:
        x_pos += 44
        move_allow = 0

    if keys[pygame.K_UP] and move_allow == 1 and y_pos > 200:
        y_pos -= 43
        move_allow = 0

    if keys[pygame.K_DOWN] and move_allow == 1 and y_pos < 400:
        y_pos += 43
        move_allow = 0

    if sequence == 2:
        for n in range(0, 1):
            if event.type == KEYDOWN or event.type == MOUSEBUTTONDOWN:
                screen.fill(BACKGROUND_COLOR)
                sequence -= 2
        move_allow = 1

    if sequence > 2:
        sequence = 1

    print(x_pos)
    pygame.display.update()
