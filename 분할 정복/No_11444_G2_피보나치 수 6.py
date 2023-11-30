import sys

M = int(sys.stdin.readline())
basic_matrix = [[1, 1], [1, 0]]


def make_matrix(matrix_a, matrix_b):
    basic = [[0, 0], [0, 0]]
    for i in range(2):
        for j in range(2):
            for k in range(2):
                basic[i][j] += matrix_a[i][k] * matrix_b[k][j] % 1000000007
    return basic


def make_mulitply(matrix, square):
    if square == 1:
        return matrix
    B = make_mulitply(matrix, square // 2)
    if square % 2 == 0:
        return make_matrix(B, B)
    else:
        return make_matrix(make_matrix(B, B), matrix)


answer = make_mulitply(basic_matrix, M)
print(answer[0][1] % 1000000007)
