n = int(input())

matrix = []
knights = []

for r in range(n):
    row = list(input())
    for c in range(n):
        if row[c] == 'K':
            knights.append([r, c])
    matrix.append(row)

KNIGHT_MOVES = ((-2, -1), (-2, 1), (-1, -2), (-1, 2), (1, -2), (1, 2), (2, -1), (2, 1))

removed_knights = 0

while True:
    max_hits = 0
    max_knight = None
    for k_r, k_c in knights:
        hits = 0
        for dr, dc in KNIGHT_MOVES:
            nr, nc = k_r + dr, k_c + dc
            if 0 <= nr < n and 0 <= nc < n and matrix[nr][nc] == 'K':
                hits += 1

        if hits > max_hits:
            max_hits = hits
            max_knight = [k_r, k_c]

    if max_hits == 0:
        break
    knights.remove(max_knight)
    matrix[max_knight[0]][max_knight[1]] = "0"
    removed_knights += 1

print(removed_knights)
