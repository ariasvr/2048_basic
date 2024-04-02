from random import randint
import keyboard

board = [[0, 0, 0, 0], 
         [0, 0, 0, 0], 
         [0, 0, 0, 0], 
         [0, 0, 0, 0]]

is_continue = False

def print_board(board):
    for row in board:
        print(row)

def generate_2(width, heigth):
    col = randint(0, width - 1)
    row = randint(0, heigth - 1)
    return col, row

def move_down(board):
    global heigth, width
    for col in range(width):
        for row in range(heigth):
            curr_row = heigth - row - 1
            for i in range(curr_row): # i is previous row index
                if board[curr_row][col] != 0 and board[curr_row - i - 1][col] != board[curr_row][col] and board[curr_row - i - 1][col] != 0:
                    break
                else:
                    board[curr_row][col] += board[curr_row - i - 1][col]
                    board[curr_row - i - 1][col] = 0

def move_up(board):
    global heigth, width
    for col in range(width):
        for row in range(heigth):
            for i in range(heigth - row - 1): # i is previous row index
                if board[row][col] != 0 and board[row + i + 1][col] != board[row][col] and board[row + i + 1][col] != 0:
                    break
                else:
                    board[row][col] += board[row + i + 1][col]
                    board[row + i + 1][col] = 0                    

def move_left(board):
    global heigth, width
    for row in range(heigth):
        for col in range(width):
            for i in range(width - col - 1):
                if board[row][col] != 0 and board[row][col + i + 1] != board[row][col] and board[row][col + i + 1] != 0:
                    break
                else:
                    board[row][col] += board[row][col + i + 1]
                    board[row][col + i + 1] = 0     

def move_right(board):
    global heigth, width
    for row in range(heigth):
        for col in range(width):
            curr_col = width - col - 1
            for i in range(curr_col):
                if board[row][curr_col] != 0 and board[row][curr_col - i - 1] != board[row][curr_col] and board[row][curr_col - i - 1] != 0:
                    break
                else:
                    board[row][curr_col] += board[row][curr_col - i - 1]
                    board[row][curr_col - i - 1] = 0      

def make_a_move(key, board):
    if key == '1' or key == "up":
        move_up(board)

    if key == '2' or key == "down":
        move_down(board)
    
    if key == '3' or key == "left":
        move_left(board)

    if key == '4' or key == "right":
        move_right(board)

width = len(board[0])
heigth = len(board)

while True:
    row, col = generate_2(width, heigth)
    board[row][col] = 2
    print_board(board)
    # print('Choose a movement:')
    # print('1. Up')
    # print('2. Down')
    # print('3. Left')
    # print('4. Right')
    # move_num = input('Your choice:')
    key = keyboard.read_key()
    print(key)
    make_a_move(key, board)