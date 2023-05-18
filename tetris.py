# this game is based on the tutorial by Tech with Tim
# https://www.youtube.com/watch?v=zfvxp7PgQ6c
    # steps according to tutorial:
        # creating the data structure for pieces
        # setting up global vars
        # create functions
        # - create_grid
        # - draw_grid
        # - draw_window
        # - rotating shape in main
        # - setting up the main

# --- IMPORTS:

import pygame
import random

"""
10 x 20 square grid
shapes: S, Z, I, O, J, L, T
represented in order by 0 - 6
"""

# --- PYGAME INITIALIZATION of FONTS:

pygame.font.init() 

# _____ GLOBAL VARIABLES _____

# --- GAME WINDOW:

s_width = 800
s_height = 700

# --- PLAYING FIELD (GRID / red box):

play_width = 300  # meaning 300 // 10 = 30 width per block = column / x / j
play_height = 600  # meaning 600 // 20 = 30 height per block = row / y / i
block_size = 30
    # this is the size of each block in the playing field
    # this is used to create the grid and the shapes
    # this is also used to create the red box that will be used to check if the piece is within the playing field
    # grid / red box is 10 x 20

# --- POSITION OF PLAYING FIELD:

top_left_x = (s_width - play_width) // 2
top_left_y = s_height - play_height
    # this will be used to check if the piece is within the playing field
    # if not, the piece will not be able to move in that direction, rotate or the game may end if the piece is at the top of the playing field
    # this is because the piece will be blocked by the redbox created by the play_width and play_height 


# --- SHAPE FORMATS:

    # this is a list of lists
        # each list = shape
        # each sublist = rotation of shape
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

# --- SHAPES:

shapes = [S, Z, I, O, J, L, T]
    # holds the shapes above, can index easily
    # this will be used to randomly select a shape

# --- COLOURS:

shape_colors = [(0, 255, 0), (255, 0, 0), (0, 255, 255), (255, 255, 0), (255, 165, 0), (0, 0, 255), (128, 0, 128)]
    # corresponding shape colours below (Based on index)
    # this will be used to randomly select a color
    # index 0 - 6 represent shape
    # index 0 - 6 represent color

# _______________________________________________________

class Piece(object):
    ''' 
    This is the main data structure for game pieces

    parameters:
        x = x coordinate
        y = y coordinate
        shape = shape of piece
        color = color of piece
        rotation = rotation of piece
    
    global variables:
        shapes = list of shapes
        shape_colors = list of colors

    returns:
        piece object

    '''

    # METHOD:
    def __init__(self, x, y, shape):
        '''
        this function creates the piece and assigns it a random shape and color using variables shapes and shape_colors
        '''
        self.x = x # x coordinate / column
        self.y = y # y coordinate / row

        self.shape = shape 
            # use index for color below

        self.color = shape_colors[shapes.index(shape)]
            # this works by using the index of the shape in the shapes list to find the corresponding color in the shape_colors list

        self.rotation = 0
            # default rotation = 0. When up arrow is pressed, adds 1, finds index in multi-dimensional list and rotates accordingly
            # this works by using the modulo operator to find the remainder of the rotation
                # this is because the rotation is 0 - 3, so when the rotation is 4, it will be 0 again

# _______________________________________________________

def create_grid(locked_positions={}):

    ''' 
    this function creates the grid of black squares for the playing field and updates the grid with the locked positions
    locked_positions is a dictionary of locked positions and is empty by default
    the locked positions are updated in the draw_window function

    this function works by creating a list of lists = grid[]
        each list is a ROW with 20 elements = ROWS / Y / i (eg: for i in range(20))
            each sublist is a COLUMN with 10 elements = COLUMNS / X / j (eg: for j in range(10)
                each item in the sublist is a BLOCK = BLOCK_SIZE (eg: 30)
                    each block is a tuple of (0,0,0) which represents a black SQUARE

    the grid is 20 rows x 10 columns
        the rows are 20 because the playing field is 20 blocks high based on the play_height = 600
            the columns are 10 because the playing field is 10 blocks wide based on the play_width = 300

    parameters:
        locked_positions = dictionary of locked positions
    
    global variables:
        grid = list of lists

    returns:
        grid = list of lists

    '''

    # --- CREATE GRID:

    grid = [[(0,0,0) for x in range(10)] for x in range(20)]
        # grid is a list of 20 elements, each element is a sublist of 10 elements
        # each element in the sublist is a tuple of (0,0,0) which represents a black SQUARE

    # --- CHECK IF LOCKED POSITION IS IN GRID:

        # this will loop through the grid and check if the block is in the locked_positions dictionary by checking the x and y coordinates
        # if True, then change the default grid block black to color, as per the locked_positions dictionary
        # if False, then leave the default grid block black

    for i in range(len(grid)):
        # i / ROWS / Y
        # this will = 20 because grid is a list of 20 elements

        for j in range(len(grid[i])):
            # j / COLUMNS / X
            # this will = 10 because sublist of grid is a list of 10 elements

            if (j, i) in locked_positions:
                # if x and y coordinates (block position) are in locked_positions dictionary, then...
                # get the color from the locked_positions dictionary
                # assign the color to the variable locked_position_block
                # assign the variable locked_position_block to the current x and y location as the first value in the locked_positions dictionary
                # grid[i][j] = locked_positions[(j, i)]

                c = locked_positions[(j, i)]
                    # c = locked position block
                    # c = locked_positions[(j, i)]
                    # assign the c / locked_position_block value to the current x and y location as the first value in the locked_positions dictionary

                grid[i][j] = c
                    # grid[i][j] = c
                    # set the grid index values to the locked position value just assigned
    
    return grid

# _______________________________________________________

def convert_shape_format(shape):

    '''
    this function converts the list of shapes and rotation into a form that the computer can read.
        this is done by creating a list of tuples of the shape and color
            this is done by using the shape and rotation to find the x and y coordinates of the shape
    
            the way this works is by looping through the shape and rotation
                if the shape is not a dot, then...
                    get the x and y coordinates of the shape
                    add the x and y coordinates to the shape list
                    add the color to the shape list
                    add the shape list to the shape format list
                else, if the shape is a dot, then...
                    add the dot to the shape format list

    parameters:
        shape = shape of piece
        shape = [[rotation 0], [rotation 1], [rotation 2], [rotation 3]]
    
    global variables:
        shape_colors = list of colors for each shape

    returns:
        shape_format = list of tuples of the shape and color
        shape_format = [(shape, rotation, color)]

    eg:
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

        shape_format = [(0, 0, (0, 0, 0)),
                        (1, 0, (0, 0, 0)),
                        (2, 0, (0, 0, 0)),
                        (1, 1, (0, 0, 0)),
                        (2, 1, (0, 0, 0)),
                        (3, 1, (0, 0, 0)),
                        (2, 2, (0, 0, 0)),
                        (3, 2, (0, 0, 0)),
                        (2, 3, (0, 0, 0)),
                        (3, 3, (0, 0, 0))]
    '''

    # --- LIST OF POSITIONS:

    positions = []
        # goal = to create a list of positions

    # --- GET SHAPE AND ROTATION:

    format_shape = shape.shape[shape.rotation % len(shape.shape)]
        # goal = to get the element within sublist (rotation of the shape)
            # list = T
            # sublist (rotations) = ['.....','..0..','.000.','.....','.....']
            # element = '..0..'
            # len = 4

            # modulus % is a remainder that is used to index against the shape list
                # it works by dividing the first number by the second number and returning the remainder
                # the remainder is then used to index against the list using the remainder as the index number in len(shape.shape)
                # in this example, the shape.rotation is divided by the len(shape.shape) and the remainder is used to index against the shape list
                    # eg: len = 4, so the remainder will be 0, 1, 2, 3
                        # eg: shape.shape = T, shape.rotation = 0, len(shape.shape) = 4, shape.rotation % len(shape.shape) = 0
                        # eg: shape.shape = T, shape.rotation = 1, len(shape.shape) = 4, shape.rotation % len(shape.shape) = 1
                        # eg: shape.shape = T, shape.rotation = 2, len(shape.shape) = 4, shape.rotation % len(shape.shape) = 2
                        # eg: shape.shape = T, shape.rotation = 3, len(shape.shape) = 4, shape.rotation % len(shape.shape) = 3
                            # eg: shape.shape = T, shape.rotation = 4, len(shape.shape) = 4, shape.rotation % len(shape.shape) = 0
                            # eg: shape.shape = T, shape.rotation = 5, len(shape.shape) = 4, shape.rotation % len(shape.shape) = 1
                            # eg: shape.shape = T, shape.rotation = 6, len(shape.shape) = 4, shape.rotation % len(shape.shape) = 2
    
    # --- GET X AND Y COORDINATES:

    for i, line in enumerate(format_shape):
        # i = index of the line
        # line = the line within the shape
        # eg: '..0..' = line

        row = list(line) 
            # row = the line within the shape
            # returns the current line as a list
            # eg: ['.', '.', '0', '.', '.']

            # eg:
            # first loop --> i = 0, line = '..0..'
            # second loop --> i = 1, line = '..0..'
            # third loop --> i = 2, line = '..0..'

        for j, column in enumerate(row):
            # j = index of the column
            # column = the column within the shape
            # eg: '..0..' = column

            # eg:
            # first loop --> j = 0, column = '.'
            # second loop --> j = 1, column = '.'
            # third loop --> j = 2, column = '0'
            # fourth loop --> j = 3, column = '.'
            # fifth loop --> j = 4, column = '.'
 
            if column == '0':
                # if the column in the current row is a 0, then...

                positions.append((shape.x + j, shape.y + i))
                    # add the x and y coordinates to the positions list
                    # eg: shape.x = 5, shape.y = 10, j = 2, i = 1
                        # shape.x + j = 5 + 2 = 7
                        # shape.y + i = 10 + 1 = 11
                        # positions.append((7, 11))

    # --- OFFSET THE POSITION LOCATION:
        # this is done because the position is skewed to the right and down due to the shape being in the top left corner, rather than the center

    for i, pos in enumerate(positions):
        # i = index of the position
        # pos = the position within the shape
        # eg: (7, 11) = pos

        positions[i] = (pos[0] - 2, pos[1] - 4)
            # this moves the position to the left and up by 2 and 4 respectively
                # eg: pos[0] = 7, pos[1] = 11
                    # eg: (7 - 2, 11 - 4) = (5, 7)
                        # eg: (5, 7) = positions[i]

    return positions

# _______________________________________________________

def valid_space(shape, grid):

    '''
    this function checks if the space is valid within the grid
    it works by checking if the space is empty
        if the space is empty, then it is valid
            if the space is not empty, then it is not valid

    parameters:
        shape = the shape that is being checked
        grid = the grid that is being checked
    
    global variables:
        accepted_pos = the list of positions that are empty

    returns:
        True = if the space is valid
        False = if the space is not valid

    '''

    # --- GET LIST OF POSITIONS:

    accepted_pos = [[(j, i) for j in range(10) if grid[i][j] == (0,0,0)] for i in range(20)] 
        # this will return a list of positions that are empty
            # j = x coordinate, i = y coordinate, grid[i][j] = color, (0,0,0) = empty
            # eg: [[(0,1)], [(2,3)]]
        # only allows if the position is empty. 0 color = empty

    # --- FLATTEN LIST OF POSITIONS:

    accepted_pos = [j for sub in accepted_pos for j in sub] 
        # this will flatten the list of positions
        # eg: [[(0,1)], [(2,3)]] --> [(0,1),(2,3)]
            # this is done because the accepted_pos list is a list of lists and needs to be flattened to be used in the next step

    # --- GET LIST OF POSITIONS FOR THE SHAPE:

    formatted_shape = convert_shape_format(shape) 
        # this will return a list of positions for the shape
        # converts the shape into a list of positions
        # will look like this: [(),()]

    # --- CHECK IF THE POSITION IS VALID:

    for pos in formatted_shape:
        # this will loop through each position in the shape
        # pos = the position within the shape
        # eg: (0,1) = pos
        # eg: (2,3) = pos

        if pos not in accepted_pos:
            # if the position is not in the list of accepted positions, then...

            if pos[1] > -1:
                # this finds the y coordinate of the position to see if it is above the screen
                # if the y coordinate is greater than -1, then...

                return False

    return True
        # all pieces start off screen and automatically invalid. Will ask once the piece has passed -1 position before asking for validation

# _______________________________________________________

def check_lost(positions):
    '''
    this function checks if the player has lost the game
    it works by checking if any of the positions are above the screen
        if any of the positions are above the screen, then the player has lost

    parameters:
        positions = the positions of the current shape
    
    global variables:
        positions = the list of positions that are empty

    returns:
        True = if the player has lost
        eg:
            if y = 0 then the position is lost / above screen
    '''

    # --- CHECK IF THE POSITION IS ABOVE THE SCREEN:

    for pos in positions:
        # this will loop through each position in the shape
        # pos = the position within the shape
        # eg: (0,1) = pos
        # eg: (2,3) = pos

        x, y = pos 
            # this will split the tuple into x and y coordinates
            # this is done because the positions are stored as tuples and need to be split to be used in the next step

        if y < 1:
            # this finds the y coordinate of the position to see if it is above the screen

            return True
                # if true, the position is above the screen, then the player has lost

    return False
        # if false, the position is not above the screen, then the player has not lost

# _______________________________________________________

def get_shape():
    '''
    this function picks a random shape from the shapes list
    it works by using the random.choice() function to pick a random shape from the shapes list
        it then uses the Piece() function to create the shape

    parameters:
        none

    global variables:
        shapes = the list of shapes

    eg: Piece(x, y, shape)
        5 = x position = column --> center of screen
        0 = y position = row --> top of screen --> can start in neg position to be above screen
        random.choice(shapes) = shape = random shape from shapes list
        eg: random.choice(shapes) = 'I'
    
    returns:
        Piece(5, 0, random.choice(shapes)) = the shape that is chosen
        eg: Piece(5, 0, random.choice(shapes)) = Piece(5, 0, 'I')

    '''

    # --- PICK A RANDOM SHAPE:

    return Piece(5, 0, random.choice(shapes))

# _______________________________________________________

def draw_text_middle(surface, text, size, color, ):
    '''
    this function draws the text in the middle of the screen
    it works by getting the width and height of the screen and dividing it by 2 to get the middle
        it then draws the text in the middle of the screen

    parameters:
        surface = the surface that the text is being drawn on
        text = the text that is being drawn
        size = the size of the text
        color = the color of the text

    global variables:
        play_width = the width of the grid
        play_height = the height of the grid
        top_left_x = the x coordinate of the top left corner of the grid
        top_left_y = the y coordinate of the top left corner of the grid
    
    returns:
        none

    '''

    # --- SET THE FONT AND TEXT:

    font = pygame.font.SysFont("arial", size, bold=True)
    label = font.render(text, 1, color)

    # --- DRAW THE TEXT:

    surface.blit(label, (top_left_x + play_width /2 - (label.get_width()/2), top_left_y + play_height /2 - label.get_height() / 2))
        # blit = draw
        # this will draw the text in the middle of the screen

        # top_left_x + play_width /2 - (label.get_width()/2) = x coordinate
            # top_left_x = the x coordinate of the top left corner of the grid
            # play_width /2 = half of the width of the grid
            # label.get_width()/2 = half of the width of the text

        # top_left_y + play_height /2 - label.get_height() / 2 = y coordinate
            # top_left_y = the y coordinate of the top left corner of the grid
            # play_height /2 = half of the height of the grid
            # label.get_height() / 2 = half of the height of the text

# _______________________________________________________

def draw_grid(surface, grid):
    
    '''
    this function draws the grid lines over the top of each block and is called in draw_window()
    it works by drawing a line from the top left corner of the grid to the top right corner of the grid
        it then moves down one block and draws another line from the top left corner of the grid to the top right corner of the grid
            it does this until it reaches the bottom of the grid

    parameters:
        surface = the surface that the grid is being drawn on
        grid = the grid that the grid lines are being drawn on

    global variables:
        top_left_x = the x coordinate of the top left corner of the grid
        top_left_y = the y coordinate of the top left corner of the grid
        play_width = the width of the grid
        play_height = the height of the grid
        block_size = the size of each block
    
    returns:
        none

    '''

    # --- GET THE STARTING X AND Y COORDINATES:

    sx = top_left_x # starting x = top_left_x
    sy = top_left_y # starting y = top_left_y

    # --- DRAW THE GRID LINES:

    for i in range(len(grid)):
        # this will loop through each row in the grid
        # i = y = row

        pygame.draw.line(surface, (128,128,128), (sx, sy + i*block_size), (sx+play_width, sy+ i*block_size))
            # this will draw a line: horizontal / left to right / across / x axis / row
            # (where, colour, x, y)
                # surface = the surface that the grid is being drawn on
                # (128,128,128) = colour = grey
                # (sx, sy + i*block_size) = start location = (x, y) = (column, row)
                # (sx+play_width, sy+ i*block_size) = end location = (x, y) = (column, row)

        for j in range(len(grid[i])):
            # this will loop through each column in the grid
            # j = x = column

            pygame.draw.line(surface, (128,128,128), (sx + j * block_size, sy), (sx + j * block_size, sy + play_height))
                # this will draw a line: vertical / top to bottom / down / y axis / column
                # (where, colour, x, y)
                    # surface = the surface that the grid is being drawn on
                    # (128,128,128) = colour = grey
                    # (sx + j * block_size, sy) = start location = (x, y) = (column, row)
                    # (sx + j * block_size, sy + play_height) = end location = (x, y) = (column, row)


# _______________________________________________________
# REFERENCE: https://youtu.be/zfvxp7PgQ6c?t=3872

def clear_rows(grid, locked):
    '''
    this function clears the rows that are full of locked pieces
    it works by looping through the grid backwards and checking if there are any black blocks
        if there are no black blocks, the row is full and needs to be cleared
            it then adds a new row at the top of the grid and shifts all the other rows down

    parameters:
        grid = the grid that the rows are being cleared from
        locked = the locked positions that are being cleared from


    global variables:
        none

    returns:
        inc = the number of rows that have been cleared
    '''

    # --- SET THE VARIABLES:

    inc = 0 #increment
    rows_to_clear = [] #stores what rows that need to clear

    # --- LOOP THROUGH THE GRID BACKWARDS TO CHECK FOR BLACK BLOCKS:
        # ? Why backwards?
        # this is done so that the bottom rows are cleared first
        # if the top rows were cleared first, the bottom rows would be shifted down and would overwrite the top rows
        # this would cause the top rows to be deleted and the bottom rows to be duplicated
        # this is because the locked positions are shifted down and the grid is made up of the locked positions
        # the locked positions are shifted down in the draw_grid() function
        # the grid is made up of the locked positions in the draw_window() function

    for i in range(len(grid) -1, -1, -1):
        # this will loop through the grid backwards, starting at the bottom row
        # the way it works is: range(start, stop, step)
            # len(grid) -1 = start at the bottom row
            # -1 = stop at the top row
            # -1 = go backwards one row at a time
            # i = y = row

        row = grid[i]
        # get the row from the grid
        # i = y = row
        # this will loop through each row in the grid

        # --- CHECK FOR BLACK BLOCKS:

        if (0,0,0) not in row:
            # if there are no black blocks in the row, the row is full and needs to be cleared

            inc += 1 
                # this works as a counter to find out how many rows need to be cleared
                # as a row is cleared, inc increases by 1
                # this is done because we need to know how many rows to shift down and how many to add at top of grid

            rows_to_clear.append(i) 
                # add the row to clear to the list
                
            # original code: ind = i <-- didn't work due to the way the grid is drawn... need to loop through the grid backwards

            for j in range(len(row)):
                # this will loop through each column in the row to get the x value for each block to be cleared

                # --- CLEAR THE BLOCKS:

                try:
                    del locked[(j,i)]
                    # delete the non-black positions from the locked positions list
                    # this will delete the row from the grid and the locked positions list (because grid is made up of locked positions and draw-grid elements)
                    # we now need to shift the grid down and add a new empty row at top to replace deleted row

                except KeyError:
                    # if there is a key error, it means that the block is not in the locked positions list
                    continue

    # --- SHIFT THE ROWS DOWN:

    if inc > 0:
        # if there are rows to clear, shift the rows down

        for key in sorted(list(locked), key=lambda x: x[1])[::-1]:
            # this will loop through the locked positions list
            # key = (x,y) = (column, row)
            # sorted(list(locked), key=lambda x: x[1])[::-1] = sorts the list of locked positions based on the y value
            # lambda x: x[1] = sorts based on the y value
            # [::-1] = reverses the list
                # eg: given this list:
                    # list = [(x,y), (x,y)]
                    # locked_positions = [(0,1), (0,0)]
                    # sorted = [(0,0), (0,1)]
                    # reversed = [(0,1), (0,0)]

            # this will loop through the locked positions list backwards, starting at the bottom row
                # this is done so that the bottom rows are shifted down first
                # if the top rows were shifted down first, the bottom rows would be shifted down and would overwrite the top rows
                # this would cause the top rows to be deleted and the bottom rows to be duplicated

            # this is the same as the loop above, but it loops through the locked positions list instead of the grid
            # for every key, sorted in the list of locked positions --> sorts based on the order of y value
            # for every key, reversed in the list of locked positions --> reverses the list so that it starts at the bottom row and goes up

            x, y = key 
                # x = column, y = row, key = (x,y) = locked position from locked_positions list
    
            if y < rows_to_clear[0]:
                # if the y value of the locked position is above the first row to clear, shift the rows down
            # original code: if y < ind: # if y/row value is above the current index in the loop (row), shift the rows above the y down <-- didnt work because of the way the grid is drawn (looping backwards)

                new_key = (x, y + inc) 
                    # new_key = (column, row + number of rows cleared)
                    # adds the number of deleted rows to y
                locked[new_key] = locked.pop(key)
                    # this will shift the locked position down by the number of deleted rows

    return inc
    # increment (how many rows cleared --> used for score)

# _______________________________________________________

def draw_next_shape(shape, surface):
    '''
    this function will draw the next shape in the next shape box

    parameters:
        shape = the shape that is being drawn
        surface = the surface that the shape is being drawn on

    global variables:
        none

    returns:
        none
    
    '''

    # --- SET THE VARIABLES:

    font = pygame.font.SysFont('arial', 30)
    label = font.render('Next Shape', 1, (255,255,255))
        # set the font and title of the box "next shape"

    # --- DRAW THE BOX:

    sx = top_left_x + play_width + 50
    sy = top_left_y + play_height/2 -100
        # this will set the x and y coordinates of the box and place it to the right of the game-play area
        # sx = x coordinate of the box
        # sy = y coordinate of the box

    format_shape = shape.shape[shape.rotation % len(shape.shape)]
        # this will get the shape from the shape list and the rotation of the shape to draw the shape in the correct rotation
        # shape.shape = the list of shapes
        # shape.rotation = the current rotation of the shape
        # len(shape.shape) = the length of the shape.shape list
        # shape.rotation % len(shape.shape) = the remainder of the current rotation divided by the length of the shape.shape list
            # eg: shape.shape = T, shape.rotation = 0, len(shape.shape) = 4, shape.rotation % len(shape.shape) = 0
                # goal = to get the element within sublist (rotation of the shape)
                # list = T
                # sublist (rotations) = ['.....','..0..','.000.','.....','.....']
                # element = '..0..'
                # len = 4

            # modulus % is a remainder that is used to index against the shape list
                # it works by dividing the first number by the second number and returning the remainder
                # the remainder is then used to index against the list using the remainder as the index number in len(shape.shape)
                # in this example, the shape.rotation is divided by the len(shape.shape) and the remainder is used to index against the shape list
                    # eg: len = 4, so the remainder will be 0, 1, 2, 3
                        # eg: shape.shape = T, shape.rotation = 0, len(shape.shape) = 4, shape.rotation % len(shape.shape) = 0
                        # eg: shape.shape = T, shape.rotation = 1, len(shape.shape) = 4, shape.rotation % len(shape.shape) = 1
                        # eg: shape.shape = T, shape.rotation = 2, len(shape.shape) = 4, shape.rotation % len(shape.shape) = 2
                        # eg: shape.shape = T, shape.rotation = 3, len(shape.shape) = 4, shape.rotation % len(shape.shape) = 3
                            # eg: shape.shape = T, shape.rotation = 4, len(shape.shape) = 4, shape.rotation % len(shape.shape) = 0
                            # eg: shape.shape = T, shape.rotation = 5, len(shape.shape) = 4, shape.rotation % len(shape.shape) = 1
                            # eg: shape.shape = T, shape.rotation = 6, len(shape.shape) = 4, shape.rotation % len(shape.shape) = 2

    for i, line in enumerate(format_shape):
        # this will loop through the shape list and draw the shape

        row = list(line) 
            # this will convert the string into a list 
            # eg: '..0..' --> ['.', '.', '0', '.', '.']

        for j, column in enumerate(row):
            # this will loop through the list and draw the shape

            if column == '0':
                # if the column is equal to 0, draw the shape

                pygame.draw.rect(surface, shape.color, (sx + j*block_size, sy + i*block_size, block_size, block_size), 0)
                # this will draw the shape in the next shape box
                # surface = the surface that the shape is being drawn on
                # shape.color = the color of the shape
                # (sx + j*block_size, sy + i*block_size, block_size, block_size) = the coordinates of the shape

    surface.blit(label, (sx + 10, sy - 30))
        # this will draw the label of the box

# _______________________________________________________

def update_score(nscore):

    '''
    this function will update the score in the text file
    it will read the score in the text file and compare it to the current score

    parameters:
        nscore = the current score of the game

    global variables:
        none

    returns:
        none
    
    '''

    # with open('scores.txt', 'r') as f:
    #     # open text file in read mode, refer to as f
    #     lines = f.readlines()
    #     # read each line of the text file
    #     score = lines[0].strip()
    #     # remove backslash ends (automatically adds \n for new line)
    
    score = max_score()

    with open('scores.txt', 'w') as f:
        # this will open the text file in write mode and refer to it as f

        if int(score) > nscore:
            # if the score in the text file is more than the current score of the game, update the score in the text file

            f.write(str(score))
            # write the score in the text file as a string

        else:
            # if the score in the text file is less than the current score of the game, update the score in the text file

            f.write(str(nscore))
            # write the current score of the game in the text file as a string

# _______________________________________________________

def max_score():
    '''
    this function will read the score in the text file and return the score. 
    it is used to compare the score in the text file to the current score of the game


    parameters:
        none

    global variables:
        none

    returns:
        score = the score in the text file
    '''
    with open('scores.txt', 'r') as f:
        # open text file in read mode, refer to as f
        
        lines = f.readlines()
        # read each line of the text file

        score = lines[0].strip()
        # remove backslash ends (automatically adds \n for new line)
        # this will set the score to the first line of the text file
    
    return score

# _______________________________________________________

def draw_window(surface, grid, score=0, last_score = 0):
    '''
    this function will draw the window of the game
    it works by drawing the grid, score, last score and the next shape box on the surface (canvas)

    this function is used in draw_window below

    it works by:
        for each row in the grid
            for each column in the row
                draw a rectangle on the surface
                the rectangle will be the colour of the grid   
                the rectangle will be drawn at the top left position of the grid
                the rectangle will be drawn at the size of the block
                the rectangle will be drawn at the block size

    draw grid objects onto screen using
        find column (j) location and * by block size = X position to draw
        find row (i) location and * by block size = Y position to draw

    parameters:
        surface = the surface that the game is being drawn on
        grid = the grid of the game
        score = the current score of the game
        last_score = the last score of the game

    global variables:
        none

    returns:
        none

    '''

    # --- FILL THE SURFACE
    surface.fill((0,0,0))
    # surface: drawing the grid on surface (canvas)
    # change the surface to black

    # --- DRAW THE GRID
    pygame.font.init()
    font = pygame.font.SysFont('arial', 60)
    label = font.render('Kristy\'s Tetris', 1, (255,255,255))
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

    # ---- Current Score:
    font = pygame.font.SysFont('arial', 30)
    label = font.render('Score:' + str(score), 1, (255,255,255))
        # set the font and title of the score field

    sx = top_left_x + play_width + 50
    sy = top_left_y + play_height/2 -100
    # will place the score box to the right of the game-play area

    surface.blit(label, (sx + 20, sy + 160))

    # ---- High Score:
    font = pygame.font.SysFont('arial', 30)
    label = font.render('High Score:' + str(last_score), 1, (255,255,255))
        # set the font and title of the score field

    sx = top_left_x - 200
    sy = top_left_y + 200

    surface.blit(label, (sx + 20, sy + 160))

    # ---- Next Shape:

    for i in range(len(grid)):
        # grid_block_y_axis = i
        # this will loop through each row in the grid to draw the grid
        # it works by:
            # for each row in the grid
                # for each column in the row
                    # draw a rectangle on the surface
                    # the rectangle will be the colour of the grid  
                    # the rectangle will be drawn at the top left position of the grid
                    # the rectangle will be drawn at the size of the block
                    # the rectangle will be drawn at the block size

        for j in range(len(grid[i])):
            # grid_block_x_axis = j
            # this will loop through each column in the row to draw the grid

            pygame.draw.rect(surface, grid[i][j], (top_left_x + j*block_size, top_left_y+ i*block_size, block_size, block_size), 0)

                # color of block = grid[i][j]
                # position of block = top_left_x + j*block_size, top_left_y+ i*block_size
                # width, height = block_size, block_size
                # fill shape (not just border) = 0 --> leave off if just border
    
    # ---- Draw Grid and Border

    pygame.draw.rect(surface, (255,0,0), (top_left_x, top_left_y, play_width, play_height), 4)
        # draw red rectangle that represents play area with border size of 4

    draw_grid(surface, grid)
    # call function to draw

    # pygame.display.update()
    # removed an placed in main after draw_next_shape

# _______________________________________________________

def main(win):
    '''
    the function will be used to call all other functions and run the game
    
    it works by:   
        1. setting up the grid
        2. setting up the score
        3. setting up the current piece
        4. setting up the next piece
        5. setting up the clock
        6. setting up the fall time
        7. setting up the level time
        8. setting up the score
        9. setting up the run variable

    parameters:
        win = the window that the game is being played on

    global variables:
        none

    returns:
        none
    '''

    # ---- Set up the grid:

    last_score = max_score()
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
    fall_speed = 0.27
        # how long it takes before each shape starts falling
    level_time =  0
        # how much time has passed --> level will go up and speed will increase to also increase difficulty
    score = 0
        # sets the initial score

    #---- Main Loop:

    while run:
        # while run is True

        grid = create_grid(locked_positions)
            # everytime the piece moves, we could add something to locked_positions
        fall_time += clock.get_rawtime()
            # rawtime = gets the amount of time since the clock got ticked
            # milliseconds
        level_time += clock.get_rawtime()
            # increase level time at the same rate as rawtime
        clock.tick()
            # default tick = 0
            # in the next iteration it is going to see how long it took for the while loop to run and add that amount (rawtime)
        
        # ---- Increase Level to Increase Difficulty:

        if level_time / 1000 > 5:
            # every 5 seconds increase the speed
            level_time = 0

            # ---- Increase Speed:

            if fall_speed > 0.12:
                # this is the speed at which we stop increasing time
                fall_speed -= 0.005
                # this is fast
                # how quickly the speed increases
        
        # --- Move Piece Down:

        if fall_time/1000 > fall_speed:
            fall_time = 0 # reset
            current_piece.y += 1 #move the piece down one

            # --- Check if Piece Hit Bottom:

            if not(valid_space(current_piece, grid)) and current_piece.y > 0:
                # if the piece is going to move in a valid spot and is out of the screen
                current_piece.y -= 1
                # reverse move (illegal move)
                change_piece = True
                # if we move down, it means we hit the bottom of the screen or hit another piece --> ready for another piece to play

        # ---- Check for Events (quit, move left, move right, rotate):

        for event in pygame.event.get():
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
                        current_piece.x += 1
                        # change the position back to where it was

                if event.key == pygame.K_RIGHT:
                    # if right is hit, move one position right
                    current_piece.x += 1

                    if not(valid_space(current_piece, grid)):
                        # if the space where the current piece is going to be moved to is not valid
                        current_piece.x -= 1
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
                        current_piece.rotation -= 1
        
        # ---- Draw the Shape:

        shape_pos = convert_shape_format(current_piece)
        # check the positions of all the pieces that have fallen to see if they need to be converted or if they need to be locked

        # --- Draw the Next Piece:

        for i in range(len(shape_pos)):
        # check the grid and shape positions and if they exist and are on the screen, draw the color associated to that shape
            x, y = shape_pos[i]
            if y > -1:
                grid[y][x] = current_piece.color
        
        # ---- If Piece Hit Bottom:

        if change_piece:
            # checks to see if we are at the bottom or if we have moved a piece

            for pos in shape_pos:
                p = (pos[0], pos[1])
                locked_positions[p] = current_piece.color
                # locked positions will look like this: {(1,2):(255,0,0)} <-- dict of position and color
                # allows us to get each locked_position within the grid and update the color

            # ---- Get New Piece:

            current_piece = next_piece # moving onto the next piece as previous piece is complete
            next_piece = get_shape()
            change_piece = False # looking at new piece that will spawn at top of screen
            score += clear_rows(grid, locked_positions) * 10 # finds the number of cleared rows and multiplies by 10. eg: 10 points per row cleared 

        # ---- Draw the Window, Grid, Score, Next Piece:

        draw_window(win, grid, score, last_score)
        # uses win created (as global out of this function), to pop up display game window
        # score added to display in window

        draw_next_shape(next_piece, win)
        # uses next piece and win created (as global out of this function) to draw the next shape on the right of screen in popup window

        pygame.display.update()

        # ---- Check if Lost:
        if check_lost(locked_positions):
            draw_text_middle(win, "YOU LOST!", 80, (255,255,255))
            pygame.display.update()
            pygame.time.delay(1500) # keeps the text up for 1.5 seconds to look at the message, then will divert to main menu
            run = False
            update_score(score)
    
    # pygame.display.quit()

# _______________________________________________________

def main_menu(win):
    '''
    this function will run the main menu
    
    the run variable is set to True
    while run is True, the screen will be black and the text 'Press Any Key To Play' will be displayed
    when a key is hit, the main function will be called and the game will start

    parameters:
        win = pygame.display.set_mode((s_width, s_height))

    returns:
        none
    '''
    run = True
    while run:
        win.fill((0,0,0))
        draw_text_middle(win, 'Press Any Key To Play', 60, (255,255,255))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False # tells the game to stop running when QUIT event happens (removed quit function in main)
                pygame.display.quit()
            if event.type ==pygame.KEYDOWN:
                main(win)
                # at the beginning of a game, hit any key and game will start

    pygame.display.quit()

# _______________________________________________________

win = pygame.display.set_mode((s_width, s_height))
    # creates pop up game-play screen

pygame.display.set_caption('Tetris')
    # creates a name for the display created

main_menu(win)  # start game