# Tic-Tac-Toe using Minimax Algorithm

def display_board(board):
    print("\n")
    print("-------------")

    for i in range(3):
        print("|", board[i][0], "|", board[i][1], "|", board[i][2], "|")
        print("-------------")


def check_winner(board, player):
    # Check rows
    for row in board:
        if row[0] == player and row[1] == player and row[2] == player:
            return True

    # Check columns
    for col in range(3):
        if board[0][col] == player and \
           board[1][col] == player and \
           board[2][col] == player:
            return True

    # Check diagonals
    if board[0][0] == player and \
       board[1][1] == player and \
       board[2][2] == player:
        return True

    if board[0][2] == player and \
       board[1][1] == player and \
       board[2][0] == player:
        return True

    return False


def is_full(board):
    for row in board:
        for cell in row:
            if cell == " ":
                return False
    return True


def minimax(board, is_maximizing):
    # Computer wins
    if check_winner(board, "X"):
        return 1

    # Human wins
    if check_winner(board, "O"):
        return -1

    # Draw
    if is_full(board):
        return 0

    if is_maximizing:
        best_score = -float("inf")

        for i in range(3):
            for j in range(3):

                if board[i][j] == " ":
                    board[i][j] = "X"

                    score = minimax(board, False)

                    board[i][j] = " "

                    best_score = max(best_score, score)

        return best_score

    else:
        best_score = float("inf")

        for i in range(3):
            for j in range(3):

                if board[i][j] == " ":
                    board[i][j] = "O"

                    score = minimax(board, True)

                    board[i][j] = " "

                    best_score = min(best_score, score)

        return best_score


def find_best_move(board):
    best_score = -float("inf")
    best_move = None

    for i in range(3):
        for j in range(3):

            if board[i][j] == " ":
                board[i][j] = "X"

                score = minimax(board, False)

                board[i][j] = " "

                if score > best_score:
                    best_score = score
                    best_move = (i, j)

    return best_move


def play_game():
    board = [[" " for _ in range(3)] for _ in range(3)]

    print("===== TIC-TAC-TOE USING MINIMAX =====")
    print("Computer: X")
    print("Human: O")

    while True:

        # Computer's turn
        move = find_best_move(board)

        if move is not None:
            board[move[0]][move[1]] = "X"

        display_board(board)

        if check_winner(board, "X"):
            print("Computer wins!")
            break

        if is_full(board):
            print("Game Draw!")
            break

        # Human's turn
        print("Your turn (O)")

        try:
            row = int(input("Enter row (1-3): ")) - 1
            col = int(input("Enter column (1-3): ")) - 1
        except ValueError:
            print("Invalid input! Enter numbers only.")
            continue

        if row < 0 or row > 2 or col < 0 or col > 2:
            print("Invalid position! Choose values from 1 to 3.")
            continue

        if board[row][col] != " ":
            print("Cell already occupied! Choose another cell.")
            continue

        board[row][col] = "O"

        if check_winner(board, "O"):
            display_board(board)
            print("Human wins!")
            break

        if is_full(board):
            display_board(board)
            print("Game Draw!")
            break


play_game()