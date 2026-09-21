n = int(input())

matrix = []

bunny_r = bunny_c = 0

for r in range(n):
    row = input().split()
    if 'B' in row:
        bunny_r, bunny_c = r, row.index('B')
    matrix.append(row)

DIRECTIONS = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1)
}

max_eggs = -float('inf')
best_direction = ''
best_path = []

for direction, (dr, dc) in DIRECTIONS.items():
    eggs = 0
    current_path = []

    r, c = bunny_r + dr, bunny_c + dc

    while 0 <= r < n and 0 <= c < len(matrix[0]):
        if matrix[r][c] == 'X':
            break

        eggs += int(matrix[r][c])
        current_path.append([r, c])

        r += dr
        c += dc

    if eggs > max_eggs and current_path:
        max_eggs = eggs
        best_direction = direction
        best_path = current_path

print(best_direction)
print(*best_path, sep='\n')
print(max_eggs)

