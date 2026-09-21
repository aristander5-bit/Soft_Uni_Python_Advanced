presents = int(input())
n = int(input())

matrix = []
santa_r, santa_c = 0, 0
total_nice_kids = 0

for r in range(n):
    row = input().split()
    matrix.append(row)
    for c in range(n):
        if row[c] == 'S':
            santa_r, santa_c = r, c
        elif row[c] == 'V':
            total_nice_kids += 1

nice_kids_left = total_nice_kids

DIRECTIONS = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1)
}

while True:
    command = input()
    if command == "Christmas morning":
        break

    dr, dc = DIRECTIONS[command]
    next_r = santa_r + dr
    next_c = santa_c + dc

    matrix[santa_r][santa_c] = '-'
    santa_r, santa_c = next_r, next_c

    cell = matrix[santa_r][santa_c]

    if cell == 'V':
        presents -= 1
        nice_kids_left -= 1
        matrix[santa_r][santa_c] = '-'


    elif cell == 'C':
        matrix[santa_r][santa_c] = '-'
        for dr_c, dc_c in DIRECTIONS.values():
            adj_r = santa_r + dr_c
            adj_c = santa_c + dc_c

            if matrix[adj_r][adj_c] in ('V', 'X'):
                if matrix[adj_r][adj_c] == 'V':
                    nice_kids_left -= 1

                presents -= 1
                matrix[adj_r][adj_c] = '-'

                if presents == 0:
                    break

    matrix[santa_r][santa_c] = 'S'

    if presents == 0 or nice_kids_left == 0:
        break

if presents == 0 and nice_kids_left > 0:
    print("Santa ran out of presents!")

for row in matrix:
    print(*row)

if nice_kids_left == 0:
    print(f"Good job, Santa! {total_nice_kids} happy nice kid/s.")
else:
    print(f"No presents for {nice_kids_left} nice kid/s.")

