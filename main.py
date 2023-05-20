# Define the agent player
from Board import check_winner, col_full, make_move, board
from minimax import minimax
from AlphaBeta import alpha_beta
import time

def agent_player_minimax(board, depth):
    # depth = 4
    col, minimax_score = minimax(board, depth, True)
    board = make_move(board, col, 1)
    print("Agent player choose column", col + 1)
    return board


def agent_player_alpha_beta(board, depth):
    # depth = 4
    alpha = -float('inf')
    beta = float('inf')
    col, minimax_score = alpha_beta(board, depth, True, alpha, beta)
    board = make_move(board, col, 1)
    print("Agent player choose column", col + 1)
    return board


# Define the computer player
def computer_player(board):
    import random
    col = random.choice([col for col in range(7) if  (col, board)])
    board = make_move(board, col, 2)
    print("Computer player choose column", col + 1)
    return board


# Play the game
game_over = False
turn = 2
print('What Algorithm you want the agent use the minimax or alpha beta pruning ')
print('Select option 1 or 2 respectively')
choice = input()

print('What is the Level of Difficulty(H,M,E) ')
Depth = input()
if Depth == 'H':
    depth = 7
elif Depth == 'M':
    depth = 4
else:  # Depth='E'
    depth = 2

start_time = time.time()
if choice == '1':
    while not game_over:
        if turn == 1:
            # Agent player
            agentBoard = agent_player_minimax(board, depth)
            print(board)
            if check_winner(board) != 0:
                print("Agent player wins!")
                game_over = True
            turn = 2
        else:
            # Computer player
            ComputerBoard = computer_player(board)
            print(board)
            if check_winner(board) != 0:
                print("Computer player wins!")
                game_over = True
            turn = 1

elif (choice == '2'):
    while not game_over:
        if turn == 1:
            # Agent player
            agentBoard = agent_player_alpha_beta(board, depth)
            print(board)
            if check_winner(board) != 0:
                print("Agent player wins!")
                game_over = True
            turn = 2
        else:
            # Computer player
            ComputerBoard = computer_player(board)
            print(board)
            if check_winner(board) != 0:
                print("Computer player wins!")
                game_over = True
            turn = 1
else:
    print("It is an invalid option please choose from 1 or 2")
end_time = time.time()
print("Time Taken:", end_time - start_time)