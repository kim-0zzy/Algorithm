import sys

num_list = list(range(1, int(sys.stdin.readline()) + 1))

T_F = 0
cnt_2 = 0
f = num_list[cnt_2]
b = num_list[-1]

while cnt_2 != len(num_list) - 1:
    if T_F == 0:
        cnt_2 += 1
        T_F = 1
        f = num_list[cnt_2]
    else:
        num_list.append(num_list[cnt_2])
        cnt_2 += 1
        T_F = 0
        b = num_list[-1]

print(f)
