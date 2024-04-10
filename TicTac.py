def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)


def check_winner(board):
    # Check rows and columns
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != ' ' or board[0][i] == board[1][i] == board[2][i] != ' ':
            return True

    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] != ' ' or board[0][2] == board[1][1] == board[2][0] != ' ':
        return True

    return False



def tic_tac_toe():
    board = [[' ' for _ in range(3)] for _ in range(3)]
    current_player = 'X'

    while True:
        print_board(board)

        # Get player move
        row = int(input(f"Player {current_player}, enter row (0, 1, or 2): "))
        col = int(input(f"Player {current_player}, enter column (0, 1, or 2): "))

        # Check if the cell is empty
        if board[row][col] == ' ':
            board[row][col] = current_player

            # Check for a winner
            if check_winner(board):
                print_board(board)
                print(f"Player {current_player} wins!")
                break

            # Check for a tie
            if is_board_full(board):
                print_board(board)
                print("It's a tie!")
                break

            # Switch player
            current_player = 'O' if current_player == 'X' else 'X'
        else:
            print("That cell is already taken. Try again.")

if __name__ == "__main__":
    tic_tac_toe()
