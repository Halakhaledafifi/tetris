import random
import time
import os

# define shape of tetris pieces
SHAPES=[
    [['....',
      '####',
      '....',
      '....'],
     ['..#.',
      '..#.',
      '..#.',
      '..#.']],
    [['....',
      '.##.',
      '.##.',
      '....']],
    [['....',
      '..#.',
      '###.',
      '....'],
     ['....',
      '.#..',
      '.##.',
      '.#..'],
     ['....',
      '....',
      '###.',
      '#...'],
     ['....',
      '..#.',
      '.##.',
      '..#.']]
]

# size of board
BOARD_WIDTH=10
BOARD_HEIGHT=20

# function bet create el board
def create_board():
    return [['.' for _ in range(BOARD_WIDTH)] for _ in range(BOARD_HEIGHT)]

# prints el board
def print_board(board):
    os.system('cls' if os.name == 'nt' else 'clear')
    for row in board:
        print(''.join(row))
    print()

# check if valid position
def is_valid_position(board, shape, offset):
    off_x, off_y=offset
    for y, row in enumerate(shape):
        for x, cell in enumerate(row):
            if cell == '#':
                if x + off_x < 0 or x + off_x >= BOARD_WIDTH or y + off_y >= BOARD_HEIGHT:
                    return False
                if board[y + off_y][x + off_x] != '.':
                    return False
    return True

def place_shape(board, shape, offset):
    off_x, off_y=offset
    for y, row in enumerate(shape):
        for x, cell in enumerate(row):
            if cell == '#':
                board[y + off_y][x + off_x]='#'

def remove_completed_lines(board):
    new_board=[row for row in board if '.' in row]
    while len(new_board) < BOARD_HEIGHT:
        new_board.insert(0, ['.' for _ in range(BOARD_WIDTH)])
    return new_board

def play_game():
    board=create_board()
    score=0

    while True:
        shape=random.choice(SHAPES)[0]
        offset=[BOARD_WIDTH // 2 - 2, 0]

        if not is_valid_position(board, shape, offset):
            break

        while is_valid_position(board, shape, (offset[0], offset[1] + 1)):
            offset[1] += 1
            print_board(board)
            time.sleep(0.1)

        place_shape(board, shape, offset)
        board=remove_completed_lines(board)
        score += 10

        print_board(board)
        time.sleep(0.1)

    print(f'stop {score}')

if __name__ == "__main__":
    play_game()
