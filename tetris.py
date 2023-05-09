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

    # METHOD:
    def __init__(self, x, y, shape):
        self.x = x
        self.y = y

        # use index for color below
        self.shape = shape

        # look at index of self.shape in shape list, use corresponding index to find matching color in list (could have done dict instead)
        self.color = shape_colors[shapes.index(shape)]

        # default rotation = 0. When up arrow is pressed, adds 1, finds index in multi-dimensional list and rotates accordingly
        self.rotation = 0

def create_grid(locked_positions={}):

    ''' 
    creates a grid of black squares 20 height (rows) x 10 width (columns):

        for i in range(20) = ROWS / Y / i --> each item in list is a row with elements from sublist
        for j in range(10) = COLUMNS / X / j --> each item in list is a column with 10 elements
        0,0,0 = BLACK SQUARES --> each item in Columns list is a black square
    '''
    grid = [[(0,0,0) for x in range(10)] for x in range(20)]

    '''
    looks each grid block and sees if is a locked_position value
    if it is, change the default grid block black to color, as per the locked_postions dictionary
    '''

    for grid_block_y_axis in range(len(grid)):
        # for i in range
        # this will = 20 because grid is a list of 20 elements
        for grid_block_x_axis in range(len(grid[grid_block_y_axis])):
            # for j in range
            # this will = 10 because sublist of grid is a list of 10 elements
            if (grid_block_x_axis, grid_block_y_axis) in locked_positions:
                # if (j, i) in locked_positions
                # if the block position is in the locked_positions dictionary, then....
                locked_position_block = locked_positions[(grid_block_x_axis, grid_block_y_axis)]
                # c = locked_positions[(j, i)]
                # assign the locked_position_block value to the current x and y location as the first value in the locked_positions dictionary
                grid[grid_block_y_axis][grid_block_x_axis] = locked_position_block
                    # grid[i][j] = c
                    # set the grid index values to the locked position value just assigned
    
    return grid


def convert_shape_format(shape):
    pass

def valid_space(shape, grid):
    pass

def check_lost(positions):
    pass

def get_shape():
    '''
    picks a random shape from the shapes list
    Uses the Piece() function to create piece
    5 = x position = column
    0 = y position = row --> top of screen --> can start in neg position to be above screen
    '''
    return Piece(5, 0, random.choice(shapes))

def draw_text_middle(text, size, color, surface):
    pass

# -------------------- TODO: start part 2 of tutorial here: https://youtu.be/XGf2GcyHPhc?t=11429

def draw_grid(surface, grid):
    
    '''
    draw grey lines over the top of each block
    '''

    sx = top_left_x
    sy = top_left_y
    # start x, start y

    for i in range(len(grid)):
    # i = y = row

        pygame.draw.line(surface, (128,128,128), (sx, sy+i*block_size), (sx+play_width, sy+i*block_size))
        # draw 20 vertical lines: X location stays the same (same column every time), y location changes (moved down each row within the column)
        # where, colour, location
        
        for j in range(len(grid[i])):
        # j = x = column

            pygame.draw.line(surface, (128,128,128), (sx, sy+j*block_size, sy), (sx+j*block_size, sy + play_height))
            # draw 10 horizontal lines

    pass

def clear_rows(grid, locked):
    pass

def draw_next_shape(shape, surface):
    pass

def draw_window(surface, grid):
    surface.fill((0,0,0))
    # surface: drawing the grid on surface (canvas)
    # change the surface to black

    pygame.font.init()
    font = pygame.font.SysFont('arial', 60)
    label = font.render('Tetris', 1, (255,255,255))
        # set the title label, font, colour and size for the game using pygame
        # https://www.pygame.org/docs/ref/font.html
        # font = sets the font and font size to draw to screen
        # label = sets the text for the label and colour --> not sure why 1 is there?

    surface.blit(label, (top_left_x + play_width/2 - (label.get_width()/2), 30))
        # draw the title using pygame function
        # surface = where to draw
        # blit = ?
        # label = what to draw
            # (top_left_x + play_width/2) = center of the screen = top left position and half of the width
            # label.get_width() = width of label
            # (top_left_x + play_width/2 - (label.get_width()/2)) 
                # --> draw the label in the center of the screen calc LESS the label width
            # 30 = Y axis location = 30th Row
    
    '''
    this function is used in draw_window below
    draw grid objects onto screen using
        find column (j) location and * by block size = X position to draw
        find row (i) location and * by block size = Y position to draw
    '''

    for grid_block_y_axis in range(len(grid)):
    # for i in range(len(grid)):
    # for each row
        for grid_block_x_axis in range(len(grid[grid_block_y_axis])):
        # for j in range(len(grid[i])):
        # for each column in the row
            pygame.draw.rect(surface, grid[grid_block_y_axis][grid_block_x_axis], (top_left_x + grid_block_x_axis*block_size, top_left_y+ grid_block_y_axis*block_size, block_size, block_size), 0)
            # pygame.draw.rect(surface, grid[i][j], (top_left_x + j*block_size, top_left_y+ i*block_size, block_size, block_size), 0)

                # color of block = grid[grid_block_y_axis][grid_block_x_axis]
                # position of block = (top_left_x + j*block_size, top_left_y+ i*block_size)
                # width, height = block_size, block_size
                # fill shape (not just border) = 0 --> leave off if just border
    
    pygame.draw.rect(surface, (255,0,0), (top_left_x, top_left_y, play_width, play_height), 4)
    # draw red rectangle that represents play area with border size of 4

    draw_grid(surface, grid)
    # call function to draw

    pygame.display.update()
    # update screen with above

def main(win):
    locked_positions = {}
        # passing into create_grid
    grid = create_grid(locked_positions)
    change_piece = False
    run = True
        #for while loop
    current_piece = get_shape()
        # gets random shape element from shapes list
    next_piece = get_shape()
        # gets random shape element from shapes list
    clock = pygame.time.Clock()
        # uses Clock function in pygame
    fall_time = 0

    while run:
        # while run is True

        for event in pygame.event.get()
            # get the pygame event. For each event check the the event type
            if event.type == pygame.QUIT:
                # if the event type is quit
                run = False
                    # break the loop and Quit the game
            
            if event.type == pygame.KEYDOWN:
                # if event type is keydown (if a key is pressed)

                if event.key == pygame.K_LEFT:
                    # if left is hit, move one position left
                    current_piece.x -= 1
                    # current_piece = get_shape()
                    # get_shape() = create piece, color it, size it, set rotation, position it at top

                    if not(valid_space(current_piece, grid)):
                        # if the space where the current piece is going to be moved to is not valid
                        current_piece += 1
                        # change the position back to where it was

                if event.key == pygame.K_RIGHT:
                    # if right is hit, move one position right
                    current_piece.x += 1

                    if not(valid_space(current_piece, grid)):
                        # if the space where the current piece is going to be moved to is not valid
                        current_piece -= 1
                        # change the position back to where it was

                if event.key == pygame.K_DOWN:
                    # if down is hit, move one position down
                    current_piece.y += 1
                    
                    if not(valid_space(current_piece, grid)):
                        # if the space where the current piece is going to be moved to is not valid
                        current_piece.y -= 1
                        # change the position back to where it was

                if event.key == pygame.K_UP:
                    # if up is hit, rotate shape
                    current_piece.rotation += 1

                    if not(valid_space(current_piece, grid)):
                        # if the rotation will put piece off screen
                        current_piece -= 1
        
        draw_window(win, grid)
        # uses win created (as global out of this function), to pop up display game window

def main_menu(win):
    main(win)

win = pygame.display.set_mode((s_width, s_height))
    # creates pop up game-play screen

pygame.display.set_caption('Tetris')
    # creates a name for the display created

main_menu(win)  # start game