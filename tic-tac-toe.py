import math

# Function to print the Tic-Tac-Toe board
def print_board(board):
    for row in board:
        print("|".join(row))
    print()

# Check for a win, loss, or draw
def check_winner(board):
    # Check rows and columns
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] and board[i][0] != ' ':
            return board[i][0]
        if board[0][i] == board[1][i] == board[2][i] and board[0][i] != ' ':
            return board[0][i]

    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != ' ':
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != ' ':
        return board[0][2]

    # Check for draw
    if all(cell != ' ' for row in board for cell in row):
        return 'Draw'

    return None

# Minimax algorithm with Alpha-Beta Pruning
def minimax(board, depth, is_maximizing, alpha, beta):
    winner = check_winner(board)
    if winner == 'X':  # Human wins
        return -10 + depth
    elif winner == 'O':  # AI wins
        return 10 - depth
    elif winner == 'Draw':
        return 0

    if is_maximizing:
        max_eval = -math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    board[i][j] = 'O'
                    eval = minimax(board, depth + 1, False, alpha, beta)
                    board[i][j] = ' '
                    max_eval = max(max_eval, eval)
                    alpha = max(alpha, eval)
                    if beta <= alpha:
                        break
        return max_eval
    else:
        min_eval = math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    board[i][j] = 'X'
                    eval = minimax(board, depth + 1, True, alpha, beta)
                    board[i][j] = ' '
                    min_eval = min(min_eval, eval)
                    beta = min(beta, eval)
                    if beta <= alpha:
                        break
        return min_eval

# AI's move
def best_move(board):
    best_score = -math.inf
    move = None
    for i in range(3):
        for j in range(3):
            if board[i][j] == ' ':
                board[i][j] = 'O'
                score = minimax(board, 0, False, -math.inf, math.inf)
                board[i][j] = ' '
                if score > best_score:
                    best_score = score
                    move = (i, j)
    return move

# Main game loop
def tic_tac_toe():
    board = [[' ' for _ in range(3)] for _ in range(3)]
    print("Welcome to Tic-Tac-Toe!")
    print_board(board)

    while True:
        # Human player's move
        while True:
            try:
                move = input("Enter your move (row and column: e.g., 1 1 for top-left): ")
                row, col = map(int, move.split())
                if board[row][col] == ' ':
                    board[row][col] = 'X'
                    break
                else:
                    print("Cell already occupied. Choose another!")
            except (ValueError, IndexError):
                print("Invalid input. Please enter row and column as two numbers (0-2).")

        print_board(board)

        # Check if human player wins
        result = check_winner(board)
        if result:
            if result == 'X':
                print("Congratulations! You win!")
            elif result == 'Draw':
                print("It's a draw!")
            break

        # AI's move
        print("AI's turn...")
        ai_move = best_move(board)
        if ai_move:
            board[ai_move[0]][ai_move[1]] = 'O'

        print_board(board)

        # Check if AI wins
        result = check_winner(board)
        if result:
            if result == 'O':
                print("AI wins! Better luck next time.")
            elif result == 'Draw':
                print("It's a draw!")
            break

# Start the game
tic_tac_toe()


