def check_row_winner(board, current_sign):
    for row in board:
        if row.count(current_sign) == 3:
            return True
    return False


def check_col_winner(board, current_sign):
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] == current_sign:
            return True
    return False


def check_diagonal_winner(board, current_sign):
    if board[0][0] == board[1][1] == board[2][2] == current_sign:
        return True
    if board[0][2] == board[1][1] == board[2][0] == current_sign:
        return True
    return False


def check_for_winner(board, current_sign):
    if (
        check_row_winner(board, current_sign)
        or check_col_winner(board, current_sign)
        or check_diagonal_winner(board, current_sign)
    ):
        return True
    return False


def print_board(board):
    for row in board:
        print(f"| {' | '.join(row)} |")

board = [[" ", " ", " "] for _ in range(3)]
mapper = {
    1: (0, 0), 2: (0, 1), 3: (0, 2),
    4: (1, 0), 5: (1, 1), 6: (1, 2),
    7: (2, 0), 8: (2, 1), 9: (2, 2),
}

player_one_name = input("Player One: ")
player_two_name = input("Player Two: ")

player_one_sign = input(f"{player_one_name}: would you like 'X' or 'O'? ").upper()
while player_one_sign not in ["X", "O"]:
    print("Please enter either 'X' or 'O'.")
    player_one_sign = input(f"{player_one_name}: would you like 'X' or 'O'? ").upper()

player_two_sign = "O" if player_one_sign == "X" else "X"

print("\nThis is the numeration of the board:")
print("| 1 | 2 | 3 |")
print("| 4 | 5 | 6 |")
print("| 7 | 8 | 9 |")

print(f"\n{player_one_name} starts first!\n")

turn = 1
free_positions = set(range(1, 10))

while turn <= 9:
    current_player = player_one_name if turn % 2 != 0 else player_two_name
    current_sign = player_one_sign if turn % 2 != 0 else player_two_sign

    try:
        position = int(input(f"{current_player} choose a free position [1-9]: "))
    except ValueError:
        print("Invalid input! Please enter a number between 1 and 9.")
        continue

    if position not in free_positions:
        print("This position is invalid or already taken. Try again!")
        continue

    r, c = mapper[position]
    board[r][c] = current_sign
    free_positions.remove(position)

    print_board(board)

    if check_for_winner(board, current_sign):
        print(f"\n🎉 Congratulations! {current_player} won!")
        break

    turn += 1
else:
    print("\n It's a draw!")



while True:
    current_player = player_one_name if turn % 2 != 0 else player_two_name
    current_sign = player_one_sign if turn % 2 != 0 else player_two_sign

    try:
        position = int(input(f"{current_player} please choose a free position between [1-9]: "))
    except ValueError:
        print("Please enter are valid number.")
        continue

    if not (1 <= position <= 9):
        print("Please enter a valid number, between 1 and 9.")
        continue

    row,col = mapper[position]
    if board[row][col] != " ":
        print("This position is already occupied.")
        continue

    board[row][col] = current_sign

    if turn >= 5:
        check_for_winner(board, current_sign)

    #TODO check if position is empty if not continue
    # place sign on the given position, check for winner

    turn += 1
    print_board(board)

