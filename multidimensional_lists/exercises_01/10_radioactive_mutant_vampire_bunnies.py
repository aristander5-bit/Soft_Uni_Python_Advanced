rows, cols = map(int, input().split())

matrix = []
p_row, p_col = 0, 0
bunnies = set()

for row in range(rows):
    matrix.append(list(input()))
    for col in range(cols):
        if matrix[row][col] == 'P':
            p_row, p_col = row, col
            matrix[row][col] = '.'
        elif matrix[row][col] == 'B':
            bunnies.add((row, col))

commands = input()

has_won = False

MOVES = {
    'U': (-1, 0),
    'D': (1, 0),
    'L': (0, -1),
    'R': (0, 1),
}

def spread_bunnies(mat, bunnies_set):
    new_bunnies_set = set()
    for b_row, b_col in bunnies_set:
        for d_row, d_col in MOVES.values():
            new_row, new_col = b_row + d_row, b_col + d_col
            if 0 <= new_row < rows and 0 <= new_col < cols:
                mat[new_row][new_col] = 'B'
                new_bunnies_set.add((new_row, new_col))
    bunnies_set.update(new_bunnies_set)

for command in commands:
    dr, dc = MOVES[command]
    new_p_row, new_p_col = p_row + dr, p_col + dc

    spread_bunnies(matrix, bunnies)

    if not (0 <= new_p_row < rows and 0 <= new_p_col < cols):
        has_won = True
        break

    p_row, p_col = new_p_row, new_p_col

    if matrix[p_row][p_col] == 'B':
        break

[print(''.join(row)) for row in matrix]
print(f"{'won' if has_won else 'dead'}: {p_row} {p_col}")