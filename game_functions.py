
import random

def init_game():
    board = [[0 for _ in range(4)] for _ in range(4)]
    for _ in range(2):
        x, y = random.randint(0, 3), random.randint(0, 3)
        while board[x][y] != 0:
            x, y = random.randint(0, 3), random.randint(0, 3)
        board[x][y] = 2
    return board

def add_new_two(board):
    empty_cells = [(x, y) for x in range(4) for y in range(4) if board[x][y] == 0]
    if not empty_cells:
        return board
    x, y = random.choice(empty_cells)
    board[x][y] = 2
    return board

def compress(board):
    new_board = [[0 for _ in range(4)] for _ in range(4)]
    for i in range(4):
        position = 0
        for j in range(4):
            if board[i][j] != 0:
                new_board[i][position] = board[i][j]
                position += 1
    return new_board

def merge(board):
    for i in range(4):
        for j in range(3):
            if board[i][j] == board[i][j + 1] and board[i][j] != 0:
                board[i][j] *= 2
                board[i][j + 1] = 0
    return board

def reverse(board):
    new_board = []
    for i in range(4):
        new_board.append([])
        for j in range(4):
            new_board[i].append(board[i][3 - j])
    return new_board

def transpose(board):
    new_board = [[board[j][i] for j in range(4)] for i in range(4)]
    return new_board

def move_left(board):
    board = compress(board)
    board = merge(board)
    board = compress(board)
    return board

def move_right(board):
    board = reverse(board)
    board = move_left(board)
    board = reverse(board)
    return board

def move_up(board):
    board = transpose(board)
    board = move_left(board)
    board = transpose(board)
    return board

def move_down(board):
    board = transpose(board)
    board = move_right(board)
    board = transpose(board)
    return board

def check_win(board):
    return any(2048 in row for row in board)

def check_no_moves(board):
    if any(0 in row for row in board):
        return False
    for i in range(3):
        for j in range(3):
            if board[i][j] == board[i + 1][j] or board[i][j] == board[i][j + 1]:
                return False
    return True
