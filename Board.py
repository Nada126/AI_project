# Define the game board as a 6x7 grid
board = [[0] * 7 for _ in range(6)]

# Check if a move is valid (i.e., if a column is not full)
def col_full(board, col):
    return board[0][col] == 0

# Make a move on the board
#loading from the bottom start from 5 to -1
def make_move(board, col, player):
    for row in range(5, -1, -1):
        if board[row][col] == 0:
            board[row][col] = player
            return board

# Check if there is a winner on the board
def check_winner(board):
    # Check horizontal
    for row in range(6):
        for col in range(4):
            if board[row][col] == board[row][col+1] == board[row][col+2] == board[row][col+3] != 0:
                return board[row][col]

    # Check vertical
    for row in range(3):
        for col in range(7):
            if board[row][col] == board[row+1][col] == board[row+2][col] == board[row+3][col] != 0:
                return board[row][col]

    # Check diagonal (down-right)
    for row in range(3):
        for col in range(4):
            if board[row][col] == board[row+1][col+1] == board[row+2][col+2] == board[row+3][col+3] != 0:
                return board[row][col]

    # Check diagonal (up-right)
    for row in range(3, 6):
        for col in range(4):
            if board[row][col] == board[row-1][col+1] == board[row-2][col+2] == board[row-3][col+3] != 0:
                return board[row][col]

    # No winner
    return 0

