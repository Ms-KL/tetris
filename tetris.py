import pygame
import random

# creating the data structure for pieces
# setting up global vars
# functions
# - create_grid
# - draw_grid
# - draw_window
# - rotating shape in main
# - setting up the main

"""
10 x 20 square grid
shapes: S, Z, I, O, J, L, T
represented in order by 0 - 6
"""

pygame.font.init()

# GLOBALS VARS

# whole screen
s_width = 800
s_height = 700

# redbox playing field -> creates perfect square if width 50% of height
play_width = 300  # meaning 300 // 10 = 30 width per block
play_height = 600  # meaning 600 // 20 = 30 height per block
block_size = 30

# enables checking for collision within playing field
top_left_x = (s_width - play_width) // 2
top_left_y = s_height - play_height


# SHAPE FORMATS

# each element within list = rotation
# 5x5 block of .
    # 0 represents where block exists

S = [['.....',
    '......',
    '..00..',
    '.00...',
    '.....'],
    ['.....',
    '..0..',
    '..00.',
    '...0.',
    '.....']]

Z = [['.....',
    '.....',
    '.00..',
    '..00.',
    '.....'],
    ['.....',
    '..0..',
    '.00..',
    '.0...',
    '.....']]

I = [['..0..',
    '..0..',
    '..0..',
    '..0..',
    '.....'],
    ['.....',
    '0000.',
    '.....',
    '.....',
    '.....']]

O = [['.....',
    '.....',
    '.00..',
    '.00..',
    '.....']]

J = [['.....',
    '.0...',
    '.000.',
    '.....',
    '.....'],
    ['.....',
    '..00.',
    '..0..',
    '..0..',
    '.....'],
    ['.....',
    '.....',
    '.000.',
    '...0.',
    '.....'],
    ['.....',
    '..0..',
    '..0..',
    '.00..',
    '.....']]

L = [['.....',
    '...0.',
    '.000.',
    '.....',
    '.....'],
    ['.....',
    '..0..',
    '..0..',
    '..00.',
    '.....'],
    ['.....',
    '.....',
    '.000.',
    '.0...',
    '.....'],
    ['.....',
    '.00..',
    '..0..',
    '..0..',
    '.....']]

T = [['.....',
    '..0..',
    '.000.',
    '.....',
    '.....'],
    ['.....',
    '..0..',
    '..00.',
    '..0..',
    '.....'],
    ['.....',
    '.....',
    '.000.',
    '..0..',
    '.....'],
    ['.....',
    '..0..',
    '.00..',
    '..0..',
    '.....']]

# holds the shapes above, can index easily
shapes = [S, Z, I, O, J, L, T]
# corresponding shape colours below (Based on index)
shape_colors = [(0, 255, 0), (255, 0, 0), (0, 255, 255), (255, 255, 0), (255, 165, 0), (0, 0, 255), (128, 0, 128)]
# index 0 - 6 represent shape


class Piece(object):
    ''' 
    Main data structure for game
    Includes width, height and shape parameters
    '''
    def __init__(self, x, y, shape):
        self.x = x
        self.y = y

        # use index for color below
        self.shape = shape

        # look at index of self.shape in shape list, use corresponding index to find matching color in list (could have done dict instead)
        self.color = shape_colors[shapes.index(shape)]

        # default rotation = 0. When up arrow is pressed, adds 1, finds index in multi-dimensional list and rotates accordingly
        self.rotation = 0

# TODO: Continue Tutorial from here: https://youtu.be/XGf2GcyHPhc?t=10240
def create_grid(locked_positions={}):

    pass

def convert_shape_format(shape):
    pass

def valid_space(shape, grid):
    pass

def check_lost(positions):
    pass

def get_shape():
    pass


def draw_text_middle(text, size, color, surface):
    pass

def draw_grid(surface, row, col):
    pass

def clear_rows(grid, locked):


def draw_next_shape(shape, surface):


def draw_window(surface):
    pass

def main():
    pass

def main_menu():
    pass

main_menu()  # start game
');