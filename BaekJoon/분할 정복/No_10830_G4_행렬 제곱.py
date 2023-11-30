import sys

N, M = map(int, sys.stdin.readline().split())
A = [0 for i in range(N)]
for i in range(len(A)):
    A[i] = list(map(int, sys.stdin.readline().strip().split()))


def make_matrix(a, b):
    C = [[0 for i in range(N)] for j in range(N)]
    for i in range(N):
        for j in range(N):
            for k in range(N):
                C[i][j] += a[i][k] * b[k][j] % 1000
    return C


def make_mulitply(a, b):
    if b == 1:
        return a
    B = make_mulitply(a, b // 2)
    if b % 2 == 0:
        return make_matrix(B, B)
    else:
        return make_matrix(make_matrix(B, B), a)


answer = make_mulitply(A, M)
for a in answer:
    for aa in a:
        print(aa % 1000, end=" ")
    print()

