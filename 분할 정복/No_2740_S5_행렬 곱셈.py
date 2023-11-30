import sys

N, M = map(int, sys.stdin.readline().split())
A = [0 for i in range(N)]
for i in range(len(A)):
    A[i] = list(map(int, sys.stdin.readline().strip().split()))

M, K = map(int, sys.stdin.readline().split())
B = [0 for i in range(M)]
for i in range(len(B)):
    B[i] = list(map(int, sys.stdin.readline().strip().split()))

C = [[0 for i in range(K)]for j in range(N)]


for i in range(N):
    for j in range(K):
        for k in range(M):
            C[i][j] += A[i][k] * B[k][j]

for c in C:
    for cc in c:
        print(cc, end=" ")
    print()
