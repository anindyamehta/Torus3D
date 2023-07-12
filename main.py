import pygame
import math
from pygame.locals import *
from sys import exit

'''Draw
    Purpose: Draws the torus
    Takes 6 parameters
    x: x-axis position
    y: y-axis position
    screen: pygame display
    color: torus color
    x_offset: offset value
    y_offset: offset value
'''


def draw(x, y, screen, color, x_offset, y_offset):
    pygame.draw.circle(screen, color, (x + x_offset, y + y_offset), 1)

'''create_screen - runs the math for building the torus and simulating it'''
def create_screen():
    pygame.init()
    width = 500
    height = 500
    screen = pygame.display.set_mode((width, height))
    background_color = (0, 0, 0)
    torus_color = (0, 255, 0)
    x_offset = width / 2
    y_offset = height / 2
    radius1 = 75
    radius2 = 100
    a = 0  # x-axis rotation
    b = 0  # z-axis rotation

    while True:
        screen.fill(background_color)
        cos_b, sin_b = math.cos(b), math.sin(b)
        cos_a, sin_a = math.cos(a), math.sin(a)

        for point in range(0, 628, 9):
            cos_t = math.cos(point / 100)
            sin_t = math.sin(point / 100)
            x = radius2 + radius1 * cos_t
            y = radius1 * sin_t
            for z in range(0, 628, 4):
                cos_p = math.cos(z / 100)
                sin_p = math.sin(z / 100)
                x2 = radius1 * sin_b * sin_t + cos_b * cos_p * x
                y2 = - cos_a * sin_b * cos_p * x + radius1 * cos_a * cos_b * sin_t - sin_a * sin_p * x
                draw(x2, y2, screen, torus_color, x_offset, y_offset)
        if a != 2:
            a += 0.001
            b += 0.0005
        else:
            a = 0
            b = 0
        for event in pygame.event.get():
            if event.type == QUIT:
                exit()
        pygame.display.update()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    create_screen()
