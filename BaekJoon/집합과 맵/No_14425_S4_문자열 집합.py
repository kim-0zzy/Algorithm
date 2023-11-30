import sys

N, M = map(int, sys.stdin.readline().split())
N_dict = {}
M_list = list()
cnt = 0

for i in range(N):
    N_dict[sys.stdin.readline()] = 0

for j in range(M):
    M_list.append(sys.stdin.readline())

for k in range(M):
    if M_list[k] in N_dict:
        cnt += 1
print(cnt)
