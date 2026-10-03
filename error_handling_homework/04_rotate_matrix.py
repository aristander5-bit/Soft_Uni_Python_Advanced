class MatrixContentError(Exception):
    pass

class MatrixSizeError(Exception):
    pass

def rotate_matrix(matrix):
    matrix_length = len(matrix)

    for i in range(matrix_length):
        for j in range(i, matrix_length):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    for i in range(matrix_length):
        matrix[i].reverse()

mtrx = []

while True:
    line = input().split()

    if not line:
        break

    for item in line:
        try:
            int(item)
        except ValueError:
            raise MatrixContentError("The matrix must consist of only integers")

    mtrx.append(line)

matrix_rows = len(mtrx)
if not mtrx or any(len(row) != matrix_rows for row in mtrx):
    raise MatrixSizeError("The size of the matrix is not a perfect square")

rotate_matrix(mtrx)

for row in mtrx:
    print(*row, sep=" ")
