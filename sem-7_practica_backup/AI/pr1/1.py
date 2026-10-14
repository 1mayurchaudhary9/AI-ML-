# Tic-Tac-Toe Game
# Experiment No. 1

def display_board(board):
    print("\n")
    print("-------------")
    for i in range(3):
        print("|", board[i][0], "|", board[i][1], "|", board[i][2], "|")
        print("-------------")


def check_win(board, player):
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


def check_draw(board):
    for row in board:
        for cell in row:
            if cell == " ":
                return False
    return True


def tic_tac_toe():
    board = [[" " for _ in range(3)] for _ in range(3)]
    player = "X"

    print("===== TIC-TAC-TOE GAME =====")
    print("Player 1: X")
    print("Player 2: O")

    while True:
        display_board(board)

        print("Player", player, "turn")

        try:
            row = int(input("Enter row (1-3): ")) - 1
            col = int(input("Enter column (1-3): ")) - 1
        except ValueError:
            print("Invalid input! Enter numbers only.")
            continue

        # Move validation
        if row < 0 or row > 2 or col < 0 or col > 2:
            print("Invalid position! Choose row and column from 1 to 3.")
            continue

        if board[row][col] != " ":
            print("Cell already occupied! Choose another cell.")
            continue

        # Make move
        board[row][col] = player

        # Check winner
        if check_win(board, player):
            display_board(board)
            print("Player", player, "wins!")
            break

        # Check draw
        if check_draw(board):
            display_board(board)
            print("The game is a draw!")
            break

        # Change player
        if player == "X":
            player = "O"
        else:
            player = "X"


tic_tac_toe()