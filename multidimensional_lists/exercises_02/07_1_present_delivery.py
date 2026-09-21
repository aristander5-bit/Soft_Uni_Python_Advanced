presents = int(input())
n = int(input())

matrix = []
santa_r, santa_c = 0, 0
nice_kids = 0

for row in range(n):
    matrix.append(input().split())
    for col in range(n):
        if matrix[row][col] == 'S':
            santa_r, santa_c = row, col
        elif matrix[row][col] == 'V':
            nice_kids += 1

nice_kids_gifted = 0

DIRECTIONS = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1)
}

while presents > 0:
    command = input()
    if command == "Christmas morning":
        break

    dr, dc = DIRECTIONS[command]
    r, c = santa_r + dr, santa_c + dc

    if 0 <= r < n and 0 <= c < n:
        matrix[santa_r][santa_c] = '-'
        santa_r, santa_c = r, c

        if matrix[santa_r][santa_c] == 'V':
            presents -= 1
            nice_kids_gifted += 1
        elif matrix[santa_r][santa_c] == 'C':
            for d_r, d_c in DIRECTIONS.values():
                if presents == 0:
                    break
                next_r, nex_c = santa_r + d_r, santa_c + d_c
                if 0 <= next_r < n and 0 <= nex_c < n and matrix[next_r][nex_c] in "VX":
                    presents -= 1
                    if matrix[next_r][nex_c] == 'V':
                        nice_kids_gifted += 1
                    matrix[next_r][nex_c] = '-'

        matrix[santa_r][santa_c] = 'S'

        if nice_kids_gifted == nice_kids:
            break

remaining_kids = nice_kids - nice_kids_gifted

if presents == 0 and remaining_kids > 0:
    print("Santa ran out of presents!")

for line in matrix:
    print(*line)

if remaining_kids > 0:
    print(f"No presents for {remaining_kids} nice kid/s.")
else:
    print(f"Good job, Santa! {nice_kids_gifted} happy nice kid/s.")