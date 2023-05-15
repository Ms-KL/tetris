# ___________________ Continue Tutorial From: https://youtu.be/zfvxp7PgQ6c?t=4682

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

# _______________________________________________________

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

# _______________________________________________________

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

# _______________________________________________________

def convert_shape_format(shape):
    '''
    converts the list of shapes and rotation into a form that the computer can read.
    * generate list of positions
    * based on position... check, draw etc.
    * if a 0 exists, provide position, else provide nothing

    1) get the shape from shape list and index... return the list within list. eg: get T, index to find the first position (0) and return the element
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
    '''

    positions = []
    # goal = to create a list of positions

    format_shape = shape.shape[shape.rotation % len(shape.shape)]
    # goal = to get the element within sublist --> list = T, sublist = ['.....','..0..','.000.','.....','.....'], element = '..0..'

    # using modulus provides the remainder --> use the modulus to index against list and return the shape in corresponding index
        # eg: look at current shape.shape (shape list and current index of that shape)... 
            # eg: shape.shape[shape.rotation] = 0... returns the shape/rotation at index 0 of shape list --> this will increase/decrease based on arrow logic
                # if current shape.shape[shape.rotation] > the length of the shape.shape list... then the remainder ( % ) is used to index.
                    # eg: shape.shape[shape.rotation] = 4 and the len of the list is 3... then the remainder 1 is used to index in the 0 position of the list
            # modulus provides the remainder, which is how the list is indexed again.
    
    for i, line in enumerate(format_shape):
        row = list(line) # row is the a list of the line --> returns the current line --> eg: '..0..'
        for j, column in enumerate(row):
            # eg: '..0..' = row / line
                # FIRST LOOP --> j = 0, column = .
                # SECOND LOOP --> j = 1, column = .
                # THIRD LOOP --> j = 2, column = '0'
            if column == '0':
            # looks at the column within the current row and asks if the column is 0
                positions.append((shape.x + j, shape.y + i))
                # if it is a 0, add the index of that location to the positions list
                # shape.x/y = current x/y value of shape --> add the j(column) value to shape.x position (same with i(row) + shape.y position)

    for i, pos in enumerate(positions):
        positions[i] = (pos[0] - 2, pos[1] - 4)
        # positionslist[index] = currentposition in loop - 2
        # used to offset the position location and take 2 from every x value and 4 from every Y value
        # moves to left and up
        # TODO: I don't fully follow this... need to revisit: https://youtu.be/XGf2GcyHPhc?t=12010

    
    return positions

# _______________________________________________________

def valid_space(shape, grid):
    '''
    check grid to see if we are moving into a valid space
    '''
    accepted_pos = [[(j, i) for j in range(10) if grid[i][j] == (0,0,0)] for i in range(20)] # only allows if the position is empty. 0 color = empty
    accepted_pos = [j for sub in accepted_pos for j in sub] # will look like this: [(),()]

    # takes all positions in the existing list and overriding into a one dimensional list
    # eg: flattens list: turns the accepted_pos list from this: [[(0,1)], [(2,3)]] to --> [(0,1),(2,3)]

    # convert shape into a position:
    formatted_shape = convert_shape_format(shape) # will look like this: [(),()]

    for pos in formatted_shape:
        if pos not in accepted_pos:
            if pos[1] > -1:
                return False
    return True
    # all pieces start off screen and automatically invalid. Will ask once the piece has passed -1 position before asking for validation

# _______________________________________________________

def check_lost(positions):
    '''
    check to see if any of the pieces are above the screen
    if y = 0 then the positon is lost / above screen
    '''

    for pos in positions:
        x, y = pos # split tuple
        if y < 1:
            return True

    return False

# _______________________________________________________

def get_shape():
    '''
    picks a random shape from the shapes list
    Uses the Piece() function to create piece
    5 = x position = column
    0 = y position = row --> top of screen --> can start in neg position to be above screen
    '''
    return Piece(5, 0, random.choice(shapes))

# _______________________________________________________

def draw_text_middle(surface, text, size, color, ):
    font = pygame.font.SysFont("arial", size, bold=True)
    label = font.render(text, 1, color)

    surface.blit(label, (top_left_x + play_width /2 - (label.get_width()/2), top_left_y + play_height /2 - label.get_height() / 2))
    # enables drawing a message in the middle of the screen

# _______________________________________________________

def draw_grid(surface, grid):
    
    '''
    draw grey lines over the top of each block
    '''

    sx = top_left_x
    sy = top_left_y
    # start x, start y

    for i in range(len(grid)):
    # i = y = row

        pygame.draw.line(surface, (128,128,128), (sx, sy + i*block_size), (sx+play_width, sy+ i*block_size))
        # draw horizontal lines
        # draw 20 vertical lines: X location stays the same (same column every time), y location changes (moved down each row within the column)
        # where, colour, location
        
        for j in range(len(grid[i])):
        # j = x = column

            pygame.draw.line(surface, (128,128,128), (sx + j * block_size, sy), (sx + j * block_size, sy + play_height))
            # draw vertical lines

# _______________________________________________________
# REFERENCE: https://youtu.be/zfvxp7PgQ6c?t=3872

def clear_rows(grid, locked):
    inc = 0 #increment
    for i in range(len(grid)-1, -1, -1):
        # loop through grid list BACKWARDS (remember when indexing)
            # prevents overwriting key in the dictionary when locked positions move down
            # moves bottom ones down first and the ones above can't overwrite

        row = grid[i]
        # set row to every iteration / row in the grid

        if (0,0,0) not in row:
            # if black blocks don't exist = grid is full of locked pieces, needs to clear

            inc += 1 # as a row is deleted, add to inc to find out how many rows to shift down and how many to add at top of grid
            ind = i
            for j in range(len(row)):
                # get all block positions that are not 0,0,0
                try:
                    del locked[(j,i)]
                    # delete the non-black positions from the locked positions list
                    # this deletes the whole row from the grid (because grid is made up of locked pieces and draw-grid elements)
                    # need to now shift grid down and add a new empty row at top to replace deleted row
                except:
                    continue
        
        if inc > 0:
            for key in sorted(list(locked), key = lambda x:x[1])[::-1]:
                # for every key, sorted in the list of locked positions --> sorts based on the order of y value
                # eg: given this list: 
                    # list = [(x,y), (x,y)]
                    # locked_positions = [(0,1), (0,0)]
                    # sorted = [(0,0), (0,1)]

                x, y = key #gets x and y from locked_positions list
                if y < ind: # if y/row value is above the current index in the loop (row), shift the rows above the y down
                    newKey = (x, y + inc) # adds the number of deleted rows to y
                    locked[newKey] = locked.pop(key)
        
        return inc
        # increment (how many rows cleared --> used for score)


# _______________________________________________________

def draw_next_shape(shape, surface):
    font = pygame.font.SysFont('arial', 30)
    label = font.render('Next Shape', 1, (255,255,255))
        # set the font and title of the box "next shape"

    sx = top_left_x + play_width + 50
    sy = top_left_y + play_height/2 -100
    # will place the shape to the right of the game-play area

    format_shape = shape.shape[shape.rotation % len(shape.shape)]
    # goal = to get the element within sublist --> list = T, sublist = ['.....','..0..','.000.','.....','.....'], element = '..0..'

    # using modulus provides the remainder --> use the modulus to index against list and return the shape in corresponding index
        # eg: look at current shape.shape (shape list and current index of that shape)... 
            # eg: shape.shape[shape.rotation] = 0... returns the shape/rotation at index 0 of shape list --> this will increase/decrease based on arrow logic
                # if current shape.shape[shape.rotation] > the length of the shape.shape list... then the remainder ( % ) is used to index.
                    # eg: shape.shape[shape.rotation] = 4 and the len of the list is 3... then the remainder 1 is used to index in the 0 position of the list
            # modulus provides the remainder, which is how the list is indexed again.

    for i, line in enumerate(format_shape):
        row = list(line)
        for j, column in enumerate(row):
            if column == '0':
                pygame.draw.rect(surface, shape.color, (sx + j*block_size, sy + i*block_size, block_size, block_size), 0)

    surface.blit(label, (sx + 10, sy - 30))

# _______________________________________________________

def draw_window(surface, grid, score=0):
    surface.fill((0,0,0))
    # surface: drawing the grid on surface (canvas)
    # change the surface to black

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

    # Score Box:
    font = pygame.font.SysFont('arial', 30)
    label = font.render('Score:' + str(score), 1, (255,255,255))
        # set the font and title of the score field

    sx = top_left_x + play_width + 50
    sy = top_left_y + play_height/2 -100
    # will place the score box to the right of the game-play area

    surface.blit(label, (sx + 20, sy + 160))
    
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

    # pygame.display.update()
    # removed an placed in main after draw_next_shape

# _______________________________________________________

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
    fall_speed = 0.27
        # how long it takes before each shape starts falling
    level_time =  0
        # how much time has passed --> level will go up and speed will increase to also increase difficulty
    score = 0
        # sets the initial score

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
        
        if level_time / 1000 > 5:
            # every 5 seconds increase the speed
            level_time = 0
            if fall_speed > 0.12:
                # this is the speed at which we stop increasing time
                fall_speed -= 0.005
                # this is fast
                # how quickly the speed increases
        
        if fall_time/1000 > fall_speed:
            fall_time = 0 # reset
            current_piece.y += 1 #move the piece down one

            if not(valid_space(current_piece, grid)) and current_piece.y > 0:
                # if the piece is going to move in a valid spot and is out of the screen
                current_piece.y -= 1
                # reverse move (illegal move)
                change_piece = True
                # if we move down, it means we hit the bottom of the screen or hit another piece --> ready for another piece to play

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
        
        shape_pos = convert_shape_format(current_piece)
        # check the positions of all the pieces that have fallen to see if they need to be converted or if they need to be locked

        for i in range(len(shape_pos)):
        # check the grid and shape positions and if they exist and are on the screen, draw the color associated to that shape
            x, y = shape_pos[i]
            if y > -1:
                grid[y][x] = current_piece.color
        
        if change_piece:
            # checks to see if we are at the bottom or if we have moved a piece
            for pos in shape_pos:
                p = (pos[0], pos[1])
                locked_positions[p] = current_piece.color
                # locked positions will look like this: {(1,2):(255,0,0)} <-- dict of position and color
                # allows us to get each locked_position within the grid and update the color

            current_piece = next_piece # moving onto the next piece as previous piece is complete
            next_piece = get_shape()
            change_piece = False # looking at new piece that will spawn at top of screen
            score += clear_rows(grid, locked_positions) * 10 # finds the number of cleared rows and multiplies by 10. eg: 10 points per row cleared 

        draw_window(win, grid, score)
        # uses win created (as global out of this function), to pop up display game window
        # score added to display in window

        draw_next_shape(next_piece, win)
        # uses next piece and win created (as global out of this function) to draw the next shape on the right of screen in popup window

        pygame.display.update()

        if check_lost(locked_positions):
            draw_text_middle(win, "YOU LOST!", 80, (255,255,255))
            pygame.display.update()
            pygame.time.delay(1500) # keeps the text up for 1.5 seconds to look at the message, then will divert to main menu
            run = False
    
    pygame.display.quit()

# _______________________________________________________

def main_menu(win):
    main(win)

# _______________________________________________________

win = pygame.display.set_mode((s_width, s_height))
    # creates pop up game-play screen

pygame.display.set_caption('Tetris')
    # creates a name for the display created

main_menu(win)  # start game