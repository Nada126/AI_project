import Board

def alpha_beta(board, depth, max_player, alpha, beta):
    # Check if the game is over or if we've reached the maximum depth
    winner = Board.check_winner(board)
    if winner != 0 or depth == 0:
        if winner == 1:
            return None, 100000000000000
        elif winner == 2:
            return None, -100000000000000
        else:
            return None, 0

    # Calculate the best move for the current player
    if max_player:
        best_move = None
        best_score = -100000000000000
        for col in range(7):
            if Board.col_full(board, col):
                temp_board = [row[:] for row in board]
                temp_board = Board.make_move(temp_board, col, 1)
                score = alpha_beta(temp_board, depth-1, False, alpha, beta)[1]
                if score > best_score:
                    best_score = score
                    best_move = col
                alpha = max(alpha, best_score)
                if alpha >= beta:
                    break  # Alpha-beta pruning
        return best_move, best_score
    else:
        best_move = None
        best_score = 100000000000000
        for col in range(7):
            if Board.col_full(board, col):
                temp_board = [row[:] for row in board]
                temp_board = Board.make_move(temp_board, col, 2)
                score = alpha_beta(temp_board, depth-1, True, alpha, beta)[1]
                if score < best_score:
                    best_score = score
                    best_move = col
                beta = min(beta, best_score)
                if alpha >= beta:
                    break  # Alpha-beta pruning
        return best_move, best_score
