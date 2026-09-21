SIZE = 5
matrix = []
my_row, my_col = 0, 0
targets = 0

for row in range(SIZE):
    matrix.append(input().split())
    for col in range(SIZE):
        if matrix[row][col] == "A":
            my_row, my_col = row, col
        elif matrix[row][col] == "x":
            targets += 1

DIRECTIONS = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1)
}

targets_down = []

for _ in range(int(input())):
    action, direction, *steps = input().split()
    dr, dc = DIRECTIONS[direction]

    if action == "shoot":
        row = my_row + dr
        col = my_col + dc

        while 0 <= row < SIZE and 0 <= col < SIZE:
            if matrix[row][col] == "x":
                matrix[row][col] = "."
                targets -= 1
                targets_down.append([row, col])
                break
            row += dr
            col += dc

        if targets == 0:
            print(f"Training completed! All {len(targets_down)} targets hit.")
            break

    elif action == "move":
        steps_count = int(steps[0])
        row = my_row + dr * steps_count
        col = my_col + dc * steps_count

        if 0 <= row < SIZE and 0 <= col < SIZE and matrix[row][col] == ".":
            matrix[my_row][my_col] = "."
            matrix[row][col] = "A"
            my_row, my_col = row, col

if targets > 0:
    print(f"Training not completed! {targets} targets left.")

for target in targets_down:
    print(target)

