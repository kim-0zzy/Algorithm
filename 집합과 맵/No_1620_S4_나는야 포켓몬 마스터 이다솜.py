import sys

N, M = map(int, sys.stdin.readline().split())
N_dict = {}
N_dict_2 = {}

for i in range(N):
    ept = sys.stdin.readline().strip()
    N_dict[ept] = str(i+1)
    N_dict_2[str(i+1)] = ept

for j in range(M):
    quiz = sys.stdin.readline().strip()
    if quiz in N_dict.keys():
        print(N_dict.get(quiz))
    else:
        print(N_dict_2.get(quiz))
