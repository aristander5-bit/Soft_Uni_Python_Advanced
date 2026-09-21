n = int(input())

matrix = [[int(x) for x in input().split()] for _ in range(n)]

bombs_input = input().split()
bombs = []

for bomb in bombs_input:
    row, col = map(int, bomb.split(','))
    bombs.append((row, col))

for r, c in bombs:
    bomb_value = matrix[r][c]

    if bomb_value > 0:
        for row in range(r - 1, r + 2):
            for col in range(c - 1, c + 2):
                if 0 <= row < n and 0 <= col < n:
                    if matrix[row][col] > 0:
                        matrix[row][col] -= bomb_value

alive_cells = 0
total_sum = 0

for row in matrix:
    for cell in row:
        if cell > 0:
            alive_cells += 1
            total_sum += cell

print(f"Alive cells: {alive_cells}")
print(f"Sum: {total_sum}")

for row in matrix:
    print(*row)
