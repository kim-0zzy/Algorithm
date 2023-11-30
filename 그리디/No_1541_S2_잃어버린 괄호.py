import sys

A = sys.stdin.readline().strip().split('-')
B = list()
for a in A:
    a = a.split('+')
    sum_1 = 0
    for aa in a:
        sum_1 += int(aa)
    B.append(sum_1)

sum_2 = B[0]
for i in range(1, len(B)):
    sum_2 -= B[i]
print(sum_2)
