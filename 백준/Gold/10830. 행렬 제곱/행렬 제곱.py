import sys

N, B = map(int, sys.stdin.readline().strip().split())
matrix = list()
for i in range(N):
    matrix.append(list(map(int, sys.stdin.readline().strip().split())))

def matrix_multiple(mat1, mat2):
    new_matrix = list()
    for _ in range(N):
        rows = list()
        for _ in range(N):
            rows.append(-1)
        new_matrix.append(rows)
    for i in range(N):
        for j in range(N):
            element = 0
            for l in range(N):
                element += mat1[i][l] * mat2[l][j]
            element %= 1000
            new_matrix[i][j] = element
    return new_matrix 
    

def matrix_square(mat):
    return matrix_multiple(mat, mat)

def func(matrix, B):
    if B == 1:
        return matrix
    elif (B % 2) == 0:
        return matrix_square(func(matrix, B // 2))
    else:
        return matrix_multiple(matrix_square(func(matrix, B // 2)), matrix)

final_matrix = func(matrix, B)

for i in range(N):
    for j in range(N):
        if final_matrix[i][j] == 1000:
            final_matrix[i][j] = 0

for i in range(N):
    for j in range(N):
        print(func(matrix, B)[i][j], end=' ')
    print()