import sys

N_count = int(sys.stdin.readline())
N_card = sys.stdin.readline().split()

M_count = int(sys.stdin.readline())
M_card = sys.stdin.readline().split()
M_card_dict = {}

for i in range(M_count):
    M_card_dict[M_card[i]] = 0

for j in range(N_count):
    if N_card[j] in M_card_dict:
        M_card_dict[N_card[j]] += 1

for v in M_card:
    print(M_card_dict[v], end=" ")
