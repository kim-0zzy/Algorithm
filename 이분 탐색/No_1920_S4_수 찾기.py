import sys


def binary_search(target, start, end):
    if start > end:
        return 0
    mid = (start + end) // 2
    if target == N_list[mid]:
        return 1
    elif target > N_list[mid]:
        return binary_search(target, mid + 1, end)
    else:
        return binary_search(target, start, mid - 1)


N = int(sys.stdin.readline())
N_list = list(map(int, sys.stdin.readline().strip().split()))
N_list = sorted(N_list)

M = int(sys.stdin.readline())
M_list = list(map(int, sys.stdin.readline().strip().split()))


for i in range(M):
    print(binary_search(M_list[i], 0, N - 1))
