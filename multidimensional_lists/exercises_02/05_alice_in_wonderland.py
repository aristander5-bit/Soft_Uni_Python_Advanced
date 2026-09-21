n = int(input())

matrix = []
alice_row, alice_col = 0, 0

for row in range(n):
    matrix.append(input().split())
    for col in range(n):
        if matrix[row][col] == 'A':
            alice_row, alice_col = row, col
            matrix[row][col] = '*'

DIRECTIONS = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1)
}

tea_bags = 0

while tea_bags < 10:
    dr, dc = DIRECTIONS[input()]
    row, col = alice_row + dr, alice_col + dc

    if not(0 <= row < n and 0 <= col < n):
        break

    curr_cell = matrix[row][col]
    matrix[row][col] = '*'
    alice_row, alice_col = row, col

    if curr_cell == 'R':
        break
    if curr_cell.isdigit():
        tea_bags += int(curr_cell)

if tea_bags >= 10:
    print("She did it! She went to the party.")
else:
    print("Alice didn't make it to the tea party.")
for row in matrix:
    print(*row)