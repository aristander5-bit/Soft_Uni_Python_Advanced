n = int(input())

matrix =[]
bee_row, bee_col = 0, 0

for row in range(n):
    line = list(input())
    if "B" in line:
        bee_r, bee_c = row, line.index("B")
        line[bee_c] = "-"
    matrix.append(line)

energy = 15
energy_restored = False
min_nectar = 30
nectar = 0

DIRECTIONS = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1)
}

while True:
    energy -= 1
    dr, dc = DIRECTIONS[input()]
    bee_r = (bee_r + dr) % n
    bee_c = (bee_c + dc) % n

    cell = matrix[bee_r][bee_c]

    if cell.isdigit():
        nectar += int(cell)
        matrix[bee_r][bee_c] = "-"
    elif cell == "H":
        if nectar >= min_nectar:
            print(f"Great job, Beesy! The hive is full. Energy left: {energy}")
        else:
            print(f"Beesy did not manage to collect enough nectar.")

        break

    if energy <= 0:
        if not energy_restored and nectar >= min_nectar:
            energy += nectar - min_nectar
            energy_restored = True
            nectar = min_nectar
        else:
            print("This is the end! Beesy ran out of energy.")
            break

matrix[bee_r][bee_c] = "B"
for row in matrix:
    print("".join(row))

