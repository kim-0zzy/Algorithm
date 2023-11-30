import sys

A_cnt, B_cnt = map(int, sys.stdin.readline().split())
cnt = 0

A_dict = {string: 0 for string in sys.stdin.readline().split()}
B_dict = {string: 0 for string in sys.stdin.readline().split()}

for key, value in A_dict.items():
    if key not in B_dict.keys():
        cnt += 1

for key, value in B_dict.items():
    if key not in A_dict.keys():
        cnt += 1

print(cnt)
