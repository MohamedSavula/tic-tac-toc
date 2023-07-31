board = [[' ' for _ in range(3)] for _ in range(3)]
players = ['X', 'O']
player_index = 0

# طباعة لوحة اللعبة
def print_board():
    for row in board:
        print(' | '.join(row))
        print('-' * 5)

# التحقق من الفوز
def check_win(player):
    for i in range(3):
        if all(board[i][j] == player for j in range(3)):
            return True
        if all(board[j][i] == player for j in range(3)):
            return True
    if all(board[i][i] == player for i in range(3)) or all(board[i][2-i] == player for i in range(3)):
        return True
    return False

# التحقق من التعادل
def is_board_full():
    return all(all(square != ' ' for square in row) for row in board)

# حلقة اللعبة
while True:
    # طباعة لوحة اللعبة
    print_board()

    current_player = players[player_index]
    move = input(f"Player {current_player}, enter your move (row[1-3] col[1-3]): ")
    row, col = map(int, move.split())

    if board[row-1][col-1] == ' ':
        board[row-1][col-1] = current_player

        # التحقق من الفوز
        if check_win(current_player):
            print(f"Player {current_player} wins!")
            break

        # التحقق من التعادل
        if is_board_full():
            print("It's a tie!")
            break

        player_index = 1 - player_index
    else:
        print("Invalid move. Try again.")
