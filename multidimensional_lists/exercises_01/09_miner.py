n = int(input())
commands = input().split()

matrix = []
m_row, m_col = 0, 0
total_coal = 0

for r in range(n):
    row_data = input().split()
    matrix.append(row_data)

    for c in range(n):
        if row_data[c] == 's':
            m_row, m_col = r, c
        elif row_data[c] == 'c':
            total_coal += 1

directions = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1)
}

for command in commands:
    move_r, move_c = directions[command]
    next_r = m_row + move_r
    next_c = m_col + move_c

    if 0 <= next_r < n and 0 <= next_c < n:
        m_row, m_col = next_r, next_c

        cell = matrix[m_row][m_col]

        if cell == 'c':
            total_coal -= 1
            matrix[m_row][m_col] = '*'

            if total_coal == 0:
                print(f"You collected all coal! ({m_row}, {m_col})")
                exit()

        elif cell == "e":
            print(f"Game over! ({m_row}, {m_col})")
            exit()

print(f"{total_coal} pieces of coal left. ({m_row}, {m_col})")
