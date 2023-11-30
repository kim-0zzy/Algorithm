import sys

N, M = map(int, sys.stdin.readline().split())
N_list = list(sys.stdin.readline().strip().split())
N_list = list(map(int, N_list))

non_sum = 0
prefix_sum = [0]
for n in N_list:
    non_sum += n
    prefix_sum.append(non_sum)

for i in range(M):
    A, B = map(int, sys.stdin.readline().split())
    print(prefix_sum[B] - prefix_sum[A-1])
