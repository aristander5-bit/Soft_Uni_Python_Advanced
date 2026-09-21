n = int(input())

matrix = []

for _ in range(n):
    data = list(input())
    matrix.append(data)

searched_symbol = input()

position = None
is_found = False

for index_row in range(n):
    for index_col in range(n):
        if matrix[index_row][index_col] == searched_symbol:
            position = (index_row, index_col)
            is_found = True
            break
    if is_found:
        break

if position:
    print(position)
else:
    print(f"{searched_symbol} does not occur in the matrix")